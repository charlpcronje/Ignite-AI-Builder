# ./notes_manager.py
"""
Notes Manager Module
--------------------
Manages notes stored in a JSON file within the notes directory. This module provides 
functionalities to read, write, add, update, and delete notes, handling data persistence 
and integrity. It includes error handling and logging to ensure robustness and reliability.

Classes:
- NotesManager: Manages operations related to notes stored in a JSON file.

Dependencies:
- json: For reading and writing JSON data.
- logging: For logging error and informational messages.
- os, datetime, shutil: For handling file operations and timestamp generation.
"""

from flask import Blueprint, request, jsonify
from api_authenticator import api_auth_instance
import logging
import os
from dotenv import load_dotenv
import uuid

class NotesManager:
    def __init__(self, notes_file, validator):
        self.validator = validator
        self.notes_file = notes_file
        self.notes_data = self._load_notes_data(notes_file)

    def _load_notes_data(self, notes_file):
        try:
            with open(notes_file, 'r') as file:
                return json.load(file)
        except Exception as e:
            logging.error(f"Error loading notes data: {e}")
            raise

    def _traverse_to_note(self, identifier, note_id=None, for_deletion=False):
        note_types = identifier.split('>')
        current_level = self.notes_data
        for note_type in note_types:
            if note_type in current_level:
                current_level = current_level[note_type]
            else:
                return None

        if note_id:
            for note in current_level.get('notes', []):
                if note['id'] == note_id:
                    return note if not for_deletion else current_level['notes'].remove(note)
        else:
            return current_level.get('notes', [])

        return None

    def add_note(self, identifier, content, datetime, api_key):
        if not self.validator.validate_hierarchy(identifier.split('>')):
            logging.warning(f"Invalid note type hierarchy: {identifier}")
            return False

        new_note = {
            "id": self._generate_unique_id(),
            "content": content,
            "datetime": datetime,
            "api_key": api_key
        }
        note_types = identifier.split('>')
        current_level = self.notes_data
        for note_type in note_types:
            current_level = current_level.setdefault(note_type, {})
        current_level.setdefault('notes', []).append(new_note)

        self.save_notes_structure()
        return True

    def update_note(self, note_id, identifier, updates):
        note = self._traverse_to_note(identifier, note_id)
        if not note:
            logging.error("Note not found for updating")
            return False

        note.update(updates)
        self.save_notes_structure()
        return True

    def delete_note(self, note_id, identifier):
        self._traverse_to_note(identifier, note_id, for_deletion=True)
        self.save_notes_structure()
        return True

    def get_note_by_id(self, note_id, identifier):
        return self._traverse_to_note(identifier, note_id)

    def get_notes_by_note_type(self, identifier):
        return self._traverse_to_note(identifier)

    def save_notes_structure(self):
        try:
            with open(self.notes_file, 'w') as file:
                json.dump(self.notes_data, file, indent=4)
            logging.info("Notes structure saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save notes structure: {e}")


    def _generate_unique_id(self):
        """
        Generates a unique identifier for a note.
        """
        return str(uuid.uuid4())

# Load environment variables
load_dotenv()
notes_dir = os.getenv('NOTES_DIR')
backup_dir = os.getenv('NOTES_BACK_DIR')

notes_blueprint = Blueprint('notes_routes', __name__)
notes_manager = NotesManager(notes_dir, backup_dir)

@notes_blueprint.route('/notes/<project_name>', methods=['GET'])
@api_auth_instance.require_api_key
def get_notes(project_name):
    api_key = request.headers.get('X-API-Key')
    note_type = request.args.get('type')
    identifier = request.args.get('identifier')

    if note_type:
        note_type_enum = NoteType[note_type.upper()]
        notes = notes_manager.read_notes_filtered_by_api_key(project_name, api_key, note_type_enum, identifier)
    else:
        notes = notes_manager.read_notes_filtered_by_api_key(project_name, api_key)

    return jsonify(notes), 200

@notes_blueprint.route('/notes/<project_name>/add', methods=['POST'])
@api_auth_instance.require_api_key
def add_note(project_name):
    api_key = request.headers.get('X-API-Key')
    data = request.json
    note_content = data.get('content')
    note_type = NoteType[data.get('type').upper()]
    identifier = data.get('identifier')

    note_id = notes_manager.add_note(project_name, note_content, note_type, identifier, api_key)
    return jsonify({"message": "Note added successfully", "note_id": note_id}), 200

@notes_blueprint.route('/notes/<project_name>/update', methods=['PUT'])
@api_auth_instance.require_api_key
def update_note(project_name):
    api_key = request.headers.get('X-API-Key')
    data = request.json
    note_id = data.get('note_id')
    updated_content = data.get('content')
    note_type = NoteType[data.get('type').upper()]
    identifier = data.get('identifier')

    success = notes_manager.update_note(project_name, note_id, updated_content, note_type, identifier, api_key)
    if success:
        return jsonify({"message": "Note updated successfully"}), 200
    else:
        return jsonify({"error": "Note not found or update failed"}), 404

@notes_blueprint.route('/notes/<project_name>/delete', methods=['DELETE'])
@api_auth_instance.require_api_key
def delete_note(project_name):
    api_key = request.headers.get('X-API-Key')
    data = request.json
    note_id = data.get('note_id')
    note_type = NoteType[data.get('type').upper()]
    identifier = data.get('identifier')

    success = notes_manager.delete_note(project_name, note_id, note_type, identifier, api_key)
    if success:
        return jsonify({"message": "Note deleted successfully"}), 200
    else:
        return jsonify({"error": "Note not found or deletion failed"}), 404

# Method to retrieve notes based on note type and identifier
    def get_notes_by_type(self, project_name, note_type, identifier):
        """
        Retrieves notes based on the specified type and identifier.
        Args:
            project_name (str): The name of the project.
            note_type (NoteType): The type of the note.
            identifier (str): The identifier (e.g., file name, class name).
        Returns:
            dict: Notes corresponding to the specified type and identifier.
        """
        notes_data = self.read_notes(project_name)
        if note_type == NoteType.PROJECT:
            return notes_data.get("notes", {})
        elif note_type == NoteType.FILE:
            return notes_data.get("files", {}).get(identifier, {}).get("notes", {})
        else:
            return notes_data.get("files", {}).get(identifier, {}).get(note_type.value, {}).get("notes", {})

    # Function Note Management
    def add_function_note(self, project_name, file_name, function_name, note_content, api_key):
        identifier = f"{file_name}/function/{function_name}"
        return self.add_note(project_name, note_content, NoteType.FUNCTION, identifier, api_key)

    def update_function_note(self, project_name, file_name, function_name, note_id, updated_content, api_key):
        identifier = f"{file_name}/function/{function_name}"
        return self.update_note(project_name, note_id, updated_content, NoteType.FUNCTION, identifier, api_key)

    def delete_function_note(self, project_name, file_name, function_name, note_id, api_key):
        identifier = f"{file_name}/function/{function_name}"
        return self.delete_note(project_name, note_id, NoteType.FUNCTION, identifier, api_key)

    # Class Note Management
    def add_class_note(self, project_name, file_name, class_name, note_content, api_key):
        identifier = f"{file_name}/class/{class_name}"
        return self.add_note(project_name, note_content, NoteType.CLASS, identifier, api_key)

    def update_class_note(self, project_name, file_name, class_name, note_id, updated_content, api_key):
        identifier = f"{file_name}/class/{class_name}"
        return self.update_note(project_name, note_id, updated_content, NoteType.CLASS, identifier, api_key)

    def delete_class_note(self, project_name, file_name, class_name, note_id, api_key):
        identifier = f"{file_name}/class/{class_name}"
        return self.delete_note(project_name, note_id, NoteType.CLASS, identifier, api_key)

    # Method Note Management
    def add_method_note(self, project_name, file_name, class_name, method_name, note_content, api_key):
        identifier = f"{file_name}/class/{class_name}/method/{method_name}"
        return self.add_note(project_name, note_content, NoteType.METHOD, identifier, api_key)

    def update_method_note(self, project_name, file_name, class_name, method_name, note_id, updated_content, api_key):
        identifier = f"{file_name}/class/{class_name}/method/{method_name}"
        return self.update_note(project_name, note_id, updated_content, NoteType.METHOD, identifier, api_key)

    def delete_method_note(self, project_name, file_name, class_name, method_name, note_id, api_key):
        identifier = f"{file_name}/class/{class_name}/method/{method_name}"
        return self.delete_note(project_name, note_id, NoteType.METHOD, identifier, api_key)

     # Closure Note Management
    def add_closure_note(self, project_name, file_name, closure_name, note_content, api_key):
        identifier = f"{file_name}/closure/{closure_name}"
        return self.add_note(project_name, note_content, NoteType.CLOSURE, identifier, api_key)

    def update_closure_note(self, project_name, file_name, closure_name, note_id, updated_content, api_key):
        identifier = f"{file_name}/closure/{closure_name}"
        return self.update_note(project_name, note_id, updated_content, NoteType.CLOSURE, identifier, api_key)

    def delete_closure_note(self, project_name, file_name, closure_name, note_id, api_key):
        identifier = f"{file_name}/closure/{closure_name}"
        return self.delete_note(project_name, note_id, NoteType.CLOSURE, identifier, api_key)

    # Object Note Management
    def add_object_note(self, project_name, file_name, object_name, note_content, api_key):
        identifier = f"{file_name}/object/{object_name}"
        return self.add_note(project_name, note_content, NoteType.OBJECT, identifier, api_key)

    def update_object_note(self, project_name, file_name, object_name, note_id, updated_content, api_key):
        identifier = f"{file_name}/object/{object_name}"
        return self.update_note(project_name, note_id, updated_content, NoteType.OBJECT, identifier, api_key)

    def delete_object_note(self, project_name, file_name, object_name, note_id, api_key):
        identifier = f"{file_name}/object/{object_name}"
        return self.delete_note(project_name, note_id, NoteType.OBJECT, identifier, api_key)

    # Type Note Management
    def add_type_note(self, project_name, file_name, type_name, note_content, api_key):
        identifier = f"{file_name}/type/{type_name}"
        return self.add_note(project_name, note_content, NoteType.TYPE, identifier, api_key)

    def update_type_note(self, project_name, file_name, type_name, note_id, updated_content, api_key):
        identifier = f"{file_name}/type/{type_name}"
        return self.update_note(project_name, note_id, updated_content, NoteType.TYPE, identifier, api_key)

    def delete_type_note(self, project_name, file_name, type_name, note_id, api_key):
        identifier = f"{file_name}/type/{type_name}"
        return self.delete_note(project_name, note_id, NoteType.TYPE, identifier, api_key)

    # Block Note Management
    def add_block_note(self, project_name, file_name, block_name, note_content, api_key):
        identifier = f"{file_name}/block/{block_name}"
        return self.add_note(project_name, note_content, NoteType.BLOCK, identifier, api_key)

    def update_block_note(self, project_name, file_name, block_name, note_id, updated_content, api_key):
        identifier = f"{file_name}/block/{block_name}"
        return self.update_note(project_name, note_id, updated_content, NoteType.BLOCK, identifier, api_key)

    def delete_block_note(self, project_name, file_name, block_name, note_id, api_key):
        identifier = f"{file_name}/block/{block_name}"
        return self.delete_note(project_name, note_id, NoteType.BLOCK, identifier, api_key)

    # Style Note Management
    def add_style_note(self, project_name, file_name, style_name, note_content, api_key):
        identifier = f"{file_name}/style/{style_name}"
        return self.add_note(project_name, note_content, NoteType.STYLE, identifier, api_key)

    def update_style_note(self, project_name, file_name, style_name, note_id, updated_content, api_key):
        identifier = f"{file_name}/style/{style_name}"
        return self.update_note(project_name, note_id, updated_content, NoteType.STYLE, identifier, api_key)

    def delete_style_note(self, project_name, file_name, style_name, note_id, api_key):
        identifier = f"{file_name}/style/{style_name}"
        return self.delete_note(project_name, note_id, NoteType.STYLE, identifier, api_key)