# notes_routes.py
"""
Blueprint Initialization: Initializes a Flask Blueprint for managing note-related routes.
Validator and Authenticator Initialization: Sets up instances of TypeHierarchyValidator and APIAuthenticator for use in the routes.
Route Functions: Each route corresponds to an operation (add, update, delete, retrieve) on notes. They interact with the NotesManager class to perform the required actions.
Error Handling: Each route includes a try-except block to handle potential exceptions and log errors.
Authentication: The @api_auth.require_api_key decorator ensures that each route is protected by API key authentication.
JSON Responses: Responses are returned as JSON, with appropriate HTTP status codes.
"""
from flask import Blueprint, request, jsonify
from notes_manager import NotesManager
from type_hierarchy_validator import TypeHierarchyValidator
from api_authenticator import APIAuthenticator
import logging

# Initialize Flask Blueprint for notes routes
notes_blueprint = Blueprint('notes_routes', __name__)

# Initialize TypeHierarchyValidator
validator = TypeHierarchyValidator('./config/type_hierarchy.json')

# API Authenticator instance
api_auth = APIAuthenticator()

@notes_blueprint.route('/<project_name>/add', methods=['POST'])
@api_auth.require_api_key
def add_note_route(project_name):
    try:
        identifier = request.args.get('identifier', '')
        content = request.json.get('content', '')
        api_key = request.headers.get('X-API-Key')

        # Initialize NotesManager with the path to the project's notes file
        notes_manager = NotesManager(f'./notes/{project_name}.json', validator)

        # Call the add_note method of NotesManager
        if notes_manager.add_note(identifier, content, api_key):
            return jsonify({"message": "Note added successfully"}), 201
        else:
            return jsonify({"error": "Failed to add note"}), 400
    except Exception as e:
        logging.error(f"Error in adding note: {e}")
        return jsonify({"error": "An error occurred"}), 500


@notes_blueprint.route('/<project_name>/update/<note_id>', methods=['PUT'])
@api_auth.require_api_key
def update_note(project_name, note_id):
    """
    Updates an existing note for the specified project.

    Args:
        project_name (str): The name of the project.
        note_id (str): The unique ID of the note to update.

    Returns:
        A JSON response indicating success or failure.
    """
    try:
        # Extract data from request
        identifier = request.args.get('identifier', '')
        updates = request.json
        notes_manager = NotesManager(f'./notes/{project_name}.json', validator)

        # Update the note
        if notes_manager.update_note(note_id, identifier, updates):
            return jsonify({"message": "Note updated successfully"}), 200
        else:
            return jsonify({"error": "Failed to update note"}), 400
    except Exception as e:
        logging.error(f"Error in updating note: {e}")
        return jsonify({"error": "An error occurred"}), 500

@notes_blueprint.route('/<project_name>/delete/<note_id>', methods=['DELETE'])
@api_auth.require_api_key
def delete_note(project_name, note_id):
    """
    Deletes a note for the specified project.

    Args:
        project_name (str): The name of the project.
        note_id (str): The unique ID of the note to delete.

    Returns:
        A JSON response indicating success or failure.
    """
    try:
        # Extract identifier from request
        identifier = request.args.get('identifier', '')
        notes_manager = NotesManager(f'./notes/{project_name}.json', validator)

        # Delete the note
        if notes_manager.delete_note(note_id, identifier):
            return jsonify({"message": "Note deleted successfully"}), 200
        else:
            return jsonify({"error": "Failed to delete note"}), 400
    except Exception as e:
        logging.error(f"Error in deleting note: {e}")
        return jsonify({"error": "An error occurred"}), 500

@notes_blueprint.route('/<project_name>/<identifier>', methods=['GET'])
@api_auth.require_api_key
def get_notes_by_identifier(project_name, identifier):
    """
    Retrieves notes based on the specified identifier for a project.

    Args:
        project_name (str): The name of the project.
        identifier (str): The hierarchical identifier of the notes.

    Returns:
        A JSON response containing the notes or an error message.
    """
    try:
        notes_manager = NotesManager(f'./notes/{project_name}.json', validator)

        # Retrieve notes
        notes = notes_manager.get_notes_by_note_type(identifier)
        if notes:
            return jsonify(notes), 200
        else:
            return jsonify({"error": "No notes found"}), 404
    except Exception as e:
        logging.error(f"Error in retrieving notes: {e}")
        return jsonify({"error": "An error occurred"}), 500


@notes_blueprint.route('/<project_name>/get/<note_id>', methods=['GET'])
@api_auth.require_api_key
def get_notes_by_id(project_name, note_id):
    """
    Retrieves notes based on the specified identifier for a project.

    Args:
        project_name (str): The name of the project.
        identifier (str): The hierarchical identifier of the notes.

    Returns:
        A JSON response containing the notes or an error message.
    """
    try:
        # Extract identifier from request
        identifier = request.args.get('identifier', '')
        notes_manager = NotesManager(f'./notes/{project_name}.json', validator)

        note = notes_manager.get_note_by_id(note_id,identifier)
        if note:
            return jsonify(note), 200
        else:
            return jsonify({"error": "Note not found"}), 404
    except Exception as e:
        logging.error(f"Error in retrieving note: {e}")
        return jsonify({"error": "An error occurred"}), 500


