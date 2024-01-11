# ./notes_routes.py
"""
Notes Routes Module
-------------------
Defines the Flask routes for notes-related operations. It handles the addition,
updating, and deletion of notes, interfacing with the NotesManager class. Each operation is
secured with API key authentication and includes detailed logging for monitoring and debugging.

Functions:
- add_note: Adds a new note to the specified notes file.
- update_note: Updates an existing note in the specified notes file.
- delete_note: Deletes a note from the specified notes file.
- get_notes: Retrieves notes from the specified file, optionally in Markdown format.

Dependencies:
- NotesManager: Class from notes_manager module for managing note operations.
- MarkdownConverter: Class for converting JSON data to Markdown format.
- require_api_key: Decorator from api_authenticator for API key validation.
"""

from flask import Blueprint, request, jsonify
from notes_manager import NotesManager
from markdown_converter import MarkdownConverter
from api_authenticator import api_auth_instance
import logging

notes_blueprint = Blueprint('notes_routes', __name__)

@notes_blueprint.route('/<project_name>', methods=['GET'])
@api_auth_instance.require_api_key
def get_notes(project_name):
    """
    Retrieves notes from the specified file, optionally formatted in Markdown.

    Args:
        project_name (str): The project_name of the notes file.

    Returns:
        JSON or Markdown formatted string of the notes, or an error message.

    This endpoint checks for a query parameter 'format'. If 'format=md' is specified,
    the notes are returned in Markdown format. Otherwise, the notes are returned in JSON format.
    """
    format_type = request.args.get('format', 'json')  # Get the format type from query parameters
    notes_manager = NotesManager(f"notes/{project_name}.json", "notes/backups/")
    notes_data = notes_manager.read_notes()  # Fetch notes data

    if notes_data is None:
        logging.error(f"Notes file {project_name} not found")
        return jsonify({'error': 'Notes file not found'}), 404

    if format_type == 'md':
        markdown_converter = MarkdownConverter()
        markdown_content = markdown_converter.convert_to_markdown(notes_data)  # Convert notes data to Markdown
        return markdown_content, 200, {'Content-Type': 'text/markdown'}

    return jsonify(notes_data), 200  # Default return format is JSON

@notes_blueprint.route('/<project_name>/add', methods=['POST'])
@api_auth_instance.require_api_key
def add_note(project_name):
    """
    Adds a new note to the specified notes file.

    Args:
        project_name (str): The project_name of the notes file to add the note to.

    Returns:
        JSON response indicating the success or failure of the operation.
    """
    notes_manager = NotesManager(f"notes/{project_name}.json", "notes/backups/")
    data = request.json
    note_content = data.get('content')
    level = data.get('level')
    identifier = data.get('identifier')
    note_id = notes_manager.add_note(note_content, level, identifier)
    
    logging.info(f"Note added to {project_name}: {note_id}")
    return jsonify({"message": "Note added successfully", "note_id": note_id}), 200

@notes_blueprint.route('/<project_name>/update', methods=['PUT'])
@api_auth_instance.require_api_key
def update_note(project_name):
    """
    Updates an existing note in the specified notes file.

    Args:
        project_name (str): The project_name of the notes file to update the note in.

    Returns:
        JSON response indicating the success or failure of the operation.
    """
    notes_manager = NotesManager(f"notes/{project_name}.json", "notes/backups/")
    data = request.json
    note_id = data.get('note_id')
    updated_content = data.get('content')
    level = data.get('level')
    identifier = data.get('identifier')
    
    success = notes_manager.update_note(note_id, updated_content, level, identifier)
    if success:
        logging.info(f"Note updated in {project_name}: {note_id}")
        return jsonify({"message": "Note updated successfully"}), 200
    else:
        logging.error(f"Failed to update note in {project_name}: {note_id}")
        return jsonify({"error": "Note not found or update failed"}), 404

@notes_blueprint.route('/<project_name>/delete', methods=['DELETE'])
@api_auth_instance.require_api_key
def delete_note(project_name):
    """
    Deletes a note from the specified notes file.

    Args:
        project_name (str): The project_name of the notes file to delete the note from.

    Returns:
        JSON response indicating the success or failure of the operation.
    """
    notes_manager = NotesManager(f"notes/{project_name}.json", "notes/backups/")
    data = request.json
    note_id = data.get('note_id')
    level = data.get('level')
    identifier = data.get('identifier')
    
    success = notes_manager.delete_note(note_id, level, identifier)
    if success:
        logging.info(f"Note deleted from {project_name}: {note_id}")
        return jsonify({"message": "Note deleted successfully"}), 200
    else:
        logging.error(f"Failed to delete note in {project_name}: {note_id}")
        return jsonify({"error": "Note not found or deletion failed"}), 404
