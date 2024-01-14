# notes_routes.py
from flask import Blueprint, request, jsonify
from NotesManager import NotesManager
from TypeHierarchyValidator import TypeHierarchyValidator
from api_authenticator import api_auth_instance
from file_handler import FileHandler
import logging  

notes_blueprint = Blueprint('notes_routes', __name__)
file_handler = FileHandler()
validator = TypeHierarchyValidator('type_hierarchy.json')

# Initialize NotesManager and TypeHierarchyValidator
validator = TypeHierarchyValidator('type_hierarchy.json')
notes_manager = NotesManager('notes/ignite.json', validator)

# Register Blueprint
app.register_blueprint(notes_blueprint, url_prefix='/notes')

@notes_blueprint.route('/<project_name>/add', methods=['POST'])
@api_auth_instance.require_api_key
def add_note():
    notes_file = f'./notes/{project_name}.json'
    notes_manager = NotesManager(notes_file, validator, file_handler)
    data = request.json
    success = notes_manager.add_note(data['identifier'], data['content'], data['datetime'], data['api_key'])
    if success:
        return jsonify({"message": "Note added successfully"}), 201
    else:
        return jsonify({"error": "Failed to add note"}), 400

@notes_blueprint.route('/<project_name>/update/<note_id>', methods=['PUT'])
@api_auth_instance.require_api_key
def update_note(note_id):
    notes_file = f'./notes/{project_name}.json'
    notes_manager = NotesManager(notes_file, validator, file_handler)
    data = request.json
    success = notes_manager.update_note(note_id, data['identifier'], data.get('updates', {}))
    if success:
        return jsonify({"message": "Note updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to update note"}), 400

@notes_blueprint.route('/<project_name>/delete/<note_id>', methods=['DELETE'])
@api_auth_instance.require_api_key
def delete_note(note_id):
    notes_file = f'./notes/{project_name}.json'
    notes_manager = NotesManager(notes_file, validator, file_handler)
    data = request.json
    success = notes_manager.delete_note(note_id, data['identifier'])
    if success:
        return jsonify({"message": "Note deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to delete note"}), 400

@notes_blueprint.route('/<project_name>/<identifier>', methods=['GET'])
@api_auth_instance.require_api_key
def get_notes_by_identifier(identifier):
    notes_file = f'./notes/{project_name}.json'
    notes_manager = NotesManager(notes_file, validator, file_handler)
    notes = notes_manager.get_notes_by_note_type(identifier)
    if notes:
        return jsonify(notes), 200
    else:
        return jsonify({"error": "No notes found for the given identifier"}), 404