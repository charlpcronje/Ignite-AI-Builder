## File: file_handler.py
```py
# ./file_handler.py
# This module handles file operations, including reading JSON files.

import json
import logging
import fcntl

class FileHandler:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def read_json_file(self, file_path):
        """
        Reads and returns the content of a JSON file, also locks the file so that it cannot be modified. 
        This is to prevent concurrent access to the file.
        Args:
        - file_path (str): The path to the JSON file.

        Returns:
        - dict: The content of the JSON file if successful, None otherwise.
        """
        try:
            with open(file_path, 'r') as file:
                fcntl.flock(file, fcntl.LOCK_SH)  # Shared lock for reading
                data = json.load(file)
                fcntl.flock(file, fcntl.LOCK_UN)  # Unlock the file
                return data
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from {file_path}: {e}")
        except Exception as e:
            logging.error(f"Error reading file {file_path}: {e}")
        return None

    def write_json_file(self, file_path, data):
        """
        Writes the given data to a JSON file, also unlocks the file so that it can be modified.

        Args:
            file_path (str): The path to the JSON file.
            data (dict): The data to write to the file.
        """
        try:
            with open(file_path, 'w') as file:
                fcntl.flock(file, fcntl.LOCK_EX)  # Exclusive lock for writing
                json.dump(data, file, indent=4)
                fcntl.flock(file, fcntl.LOCK_UN)  # Unlock the file
            logging.info(f"Data successfully written to {file_path}")
        except Exception as e:
            logging.error(f"Failed to write data to {file_path}: {e}")
            raise

```

## File: markdown_converter.py
```py
# ./markdown_converter.py
"""
MarkdownConverter Module
------------------------
Responsible for converting JSON data to Markdown format. This module is utilized in 
transforming task data into a readable Markdown format, enhancing the user's understanding 
and interaction with the data.

Classes:
- MarkdownConverter: Converts JSON data to a well-structured Markdown format.

Dependencies:
- logging: To log error messages and informational messages.
"""

import logging

class MarkdownConverter:
    def __init__(self):
        """
        Initializes the MarkdownConverter with basic logging configuration.
        """
        logging.basicConfig(level=logging.INFO)

    def convert_to_markdown(self, data):
        print(data)
        """
        Converts JSON data to Markdown format.

        Args:
            data (dict): The JSON data to be converted.

        Returns:
            str: The converted Markdown string, or an error message in case of failure.
        """
        try:
            md_content = data.get("overview", "") + "\n\n"

            # Check if the data contains a single subtask or multiple tasks
            if 'tasks' in data:
                for task_key, task_info in data["tasks"].items():
                    if 'description' in task_info:
                        # Main task with description and subtasks
                        md_content += f"## [{'x' if task_info['status'] else ' '}] {task_key}. {task_info['description']}\n"
                        for subtask_key, subtask_info in task_info.items():
                            if isinstance(subtask_info, dict) and 'task' in subtask_info:
                                md_content += f"- [{'x' if subtask_info['status'] else ' '}] {subtask_key}. {subtask_info['task']}\n"
                        md_content += "\n"
                    else:
                        # Individual subtask without a main task
                        md_content += f"- [{'x' if task_info['status'] else ' '}] {task_key}. {task_info['task']}\n"
            else:
                # Fallback for unexpected data format
                md_content += "Error: Unrecognized data format for Markdown conversion.\n"

            return md_content
        except Exception as e:
            logging.error(f"Error converting JSON to Markdown: {e}")
            return "Error in Markdown conversion"

# Example usage:
# converter = MarkdownConverter()
# markdown_text = converter.convert_to_markdown(json_data)

```

## File: api_authenticator.py
```py
# ./api_authenticator.py
import json
import functools
from flask import request, jsonify
import logging

class APIAuthenticator:
    def __init__(self):
        """
        Initializes the APIAuthenticator. API keys will be loaded dynamically per request.
        """
        self.api_keys = {}

    def load_api_keys(self, api_keys_file):
        """
        Load API keys from a specified JSON file.

        Args:
            api_keys_file (str): The path to the JSON file containing API keys.
        """
        try:
            with open(api_keys_file, 'r') as file:
                self.api_keys = json.load(file)
        except FileNotFoundError:
            logging.error(f"API keys file not found: {api_keys_file}")
            self.api_keys = {}

    def require_api_key(self, view_function):
        """
        Decorator function to secure routes with API key authentication.

        Args:
            view_function (function): The Flask view function to decorate.

        Returns:
            function: The decorated view function with API key authentication.
        """
        @functools.wraps(view_function)
        def decorated_function(*args, **kwargs):
            # Extract project name from URL path parameter
            project_name = kwargs.get('project_name')
            if project_name:
                api_keys_file = f"./users/{project_name}.json"
                self.load_api_keys(api_keys_file)
            else:
                logging.error("Project name not provided in the URL.")
                return jsonify({"error": "Project name required"}), 400

            api_key = request.headers.get('X-API-Key')
            if api_key and api_key in self.api_keys:
                return view_function(*args, **kwargs)
            else:
                logging.warning("Unauthorized access attempt.")
                return jsonify({"error": "Unauthorized"}), 401

        return decorated_function

# Create an instance
api_auth_instance = APIAuthenticator()

```

## File: task_routes.py
```py
# task_routes.py
"""
Task Routes Module
------------------
Defines the Flask routes for task-related operations. This module interfaces with the FileHandler, 
TaskManager, and MarkdownConverter classes to manage tasks. It includes functionality for 
retrieving, updating, and 'deleting' tasks, with each operation secured through API key authentication 
and detailed logging for monitoring and debugging.

Functions:
- get_task: Retrieves task data from a specified file.
- update_task: Updates the details of a specific task.
- delete_task: Marks a task as deleted in the task file.

Dependencies:
- FileHandler: Module for handling file operations.
- TaskManager: Module for extracting specific tasks or subtasks.
- MarkdownConverter: Module for converting tasks to Markdown format.
- require_api_key: Decorator from api_authenticator for API key validation.
"""

from flask import Blueprint, request, jsonify
from file_handler import FileHandler
from task_manager import TaskManager
from markdown_converter import MarkdownConverter
from api_authenticator import api_auth_instance
import logging
import shutil
from datetime import datetime
import os

# Initialize Blueprint for task routes
task_blueprint = Blueprint('task_routes', __name__)
file_handler = FileHandler()
task_manager = TaskManager()
markdown_converter = MarkdownConverter()

@task_blueprint.route('/<project_name>', methods=['GET'])
@task_blueprint.route('/<project_name>/<task_number>', methods=['GET'])
# @api_auth_instance.require_api_key
def get_task(project_name, task_number=None):
    """
    Retrieves and returns the specified task or subtask data from a JSON file.

    Args:
        project_name (str): The name of the JSON file containing tasks.
        task_number (str, optional): The specific task number to retrieve, can include subtasks like '1.1'.

    Returns:
        JSON or Markdown formatted string of the task data, or an error message.
    """
    format_type = request.args.get('format', 'json')
    file_path = f'tasks/{project_name}.json'

    logging.info(f"Retrieving tasks from {file_path}")
    tasks_data = file_handler.read_json_file(file_path)
    
    if tasks_data is None:
        logging.error("Task file not found")
        return jsonify({'error': 'File not found'}), 404

    if task_number:
        tasks_data = task_manager.extract_task_data(tasks_data, task_number)
        if tasks_data is None:
            logging.error("Specific task or subtask not found")
            return jsonify({'error': 'Task or subtask not found'}), 404

    if format_type == 'md':
        markdown_content = markdown_converter.convert_to_markdown(tasks_data)
        return markdown_content, 200, {'Content-Type': 'text/markdown'}

    return jsonify(tasks_data), 200

@task_blueprint.route('/<project_name>/<task_number>', methods=['PUT'])
def update_task(project_name, task_number):
    data = request.json
    file_path = f'tasks/{project_name}.json'

    # Create a backup before updating
    backup_dir = './tasks/backups/'
    os.makedirs(backup_dir, exist_ok=True)  # Create backups directory if it doesn't exist
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_file_path = f'{backup_dir}datetime_{project_name}_{timestamp}.json'
    shutil.copy(file_path, backup_file_path)
    logging.info(f"Backup created at {backup_file_path}")


    tasks_data = file_handler.read_json_file(file_path)
    if tasks_data is None:
        return jsonify({'error': 'File not found'}), 404

    try:
        if '.' in task_number:
            # Handle subtask
            main_task, subtask_id = task_number.split('.', 1)
            task_data = tasks_data['tasks'][main_task][task_number]
        else:
            # Handle main task
            task_data = tasks_data['tasks'][task_number]

        # Update status and/or description
        if 'status' in data:
            task_data['status'] = data['status']
        if 'description' in data and '.' not in task_number:
            task_data['description'] = data['description']

        # Write the updated data back to the file
        file_handler.write_json_file(file_path, tasks_data)
        return jsonify({"message": "Task updated successfully"}), 200

    except KeyError as e:
        logging.error(f"Task or subtask not found: {e}")
        return jsonify({'error': 'Task or subtask not found'}), 404
    except Exception as e:
        logging.exception(f"An error occurred while updating the task: {e}")
        return jsonify({'error': 'An error occurred while updating the task'}), 500
```

## File: notes_routes.py
```py
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



```

## File: prompt_routes.py
```py
# ./prompt_routes.py
"""
Prompt Routes Module
--------------------
This module defines the Flask routes for retrieving markdown prompt documents. 
It handles requests for specific prompt documents from the 'prompts' directory, 
appending the '.md' extension in the backend. The module ensures secure access 
through API key authentication and maintains detailed logging for each operation.

Functions:
- get_prompt: Retrieves the content of a markdown file based on the project name.

Dependencies:
- prompt_manager: Module for handling the retrieval of markdown files.
- require_api_key: Decorator from api_authenticator for API key validation.
"""

from flask import Blueprint, jsonify
from prompt_manager import PromptManager
from api_authenticator import api_auth_instance
import logging

# Initialize Blueprint for prompt routes
prompt_blueprint = Blueprint('prompt_routes', __name__)
prompt_manager = PromptManager("prompts")

@prompt_blueprint.route('/<project_name>/get', methods=['GET'])
@api_auth_instance.require_api_key
def get_prompt(project_name):
    """
    Retrieves and returns the content of a markdown prompt file based on the project name.

    Args:
        project_name (str): The project name corresponding to the markdown file, without the .md extension.

    Returns:
        The content of the markdown file or an error message.
    """
    filename = f"{project_name}.md"
    content, error = prompt_manager.get_prompt(filename)
    if error:
        logging.error(f"Error retrieving prompt for {filename}: {error}")
        return jsonify({'error': error}), 404
    return content, 200, {'Content-Type': 'text/plain; charset=utf-8'}

```

## File: notes_manager.py
```py
# notes_manager.py
import json
import logging
import uuid
from type_hierarchy_validator import TypeHierarchyValidator, parse_identifier
import datetime

class NotesManager:
    """
    Manages notes stored in a JSON file. Provides functionalities to add, update, delete, and retrieve notes.

    Attributes:
        validator (TypeHierarchyValidator): Validator for note type hierarchy.
        notes_file (str): Path to the notes JSON file.
        notes_data (dict): Data structure containing notes.
    """

    def __init__(self, notes_file, validator):
        """
        Initializes the NotesManager with the notes file path and a hierarchy validator.
        
        Args:
            notes_file (str): Path to the notes JSON file.
            validator (TypeHierarchyValidator): Validator for note type hierarchy.
        """
        self.validator = validator
        self.notes_file = notes_file
        self.notes_data = self._load_notes_data(notes_file)

    def _load_notes_data(self, notes_file):
        """
        Loads the notes data from the specified file.
        
        Args:
            notes_file (str): Path to the notes JSON file.
        
        Returns:
            dict: Data structure containing notes.
        
        Raises:
            Exception: If there is an error in loading the file.
        """
        try:
            with open(notes_file, 'r') as file:
                return json.load(file)
        except Exception as e:
            logging.error(f"Error loading notes data: {e}")
            raise

    def add_note(self, identifier, content, api_key):
        """
        Adds a new note to the notes structure based on the given identifier.

        Args:
            identifier (str): A string representing the hierarchical path of the note.
            content (str): The content of the note.
            api_key (str): The API key associated with the note.

        Returns:
            bool: True if the note is added successfully, False otherwise.
        """
        
        parsed_identifier = parse_identifier(identifier)
        current_level = self.notes_data

        for type, name in parsed_identifier:
            current_level = current_level.setdefault(type, {}).setdefault(name, {})

        new_note_id = self._generate_unique_id()
        created_at = datetime.datetime.now().isoformat()
        current_level['notes'][new_note_id] = {
            "content": content,
            "created_at": created_at,
            "created_by": api_key
        }

        self.save_notes_structure()
        return True, new_note_id

    def update_note(self, note_id, identifier, updates):
        """
        Updates an existing note based on its ID and identifier.

        Args:
            note_id (str): The unique ID of the note to update.
            identifier (str): The hierarchical identifier of the note.
            updates (dict): A dictionary containing the updated fields.

        Returns:
            bool: True if the update is successful, False otherwise.
        """
        parsed_identifier = parse_identifier(identifier)
        current_level = self.notes_data

        for type, name in parsed_identifier:
            current_level = current_level.get(type, {}).get(name, {})

        note_to_update = current_level.get("notes", {}).get(note_id)
        if not note_to_update:
            logging.warning(f"Note with ID {note_id} not found.")
            return False

        note_to_update.update(updates['updates'])
        note_to_update["updated_at"] = datetime.datetime.now().isoformat()

        self.save_notes_structure()
        logging.info(f"Note with ID {note_id} updated successfully.")
        return True

    def delete_note(self, note_id, identifier):
        """
        Deletes a note based on its ID and identifier.

        Args:
            note_id (str): The unique ID of the note to delete.
            identifier (str): The hierarchical identifier of the note.

        Returns:
            bool: True if the deletion is successful, False otherwise.
        """
        parsed_identifier = parse_identifier(identifier)
        current_level = self.notes_data

        for type, name in parsed_identifier:
            current_level = current_level.get(type, {}).get(name, {})

        note_to_delete = current_level.get("notes", {}).get(note_id)
        if not note_to_delete:
            logging.warning(f"Note with ID {note_id} not found.")
            return False

        note_to_delete = current_level.get('notes', {}).get(note_id)

        if note_id not in current_level.get('notes', {}):
            logging.warning(f"Note with ID {note_id} not found.")
            return False

        del current_level['notes'][note_id]
        self.save_notes_structure()
        logging.info(f"Note with ID {note_id} deleted successfully.")
        return True

    def get_note_by_id(self, note_id, identifier):
        """
        Retrieves a note by its ID and identifier.

        Args:
            note_id (str): The unique ID of the note.
            identifier (str): The hierarchical identifier of the note.

        Returns:
            dict or None: The note if found, None otherwise.
        """
        parsed_identifier = parse_identifier(identifier)
        current_level = self.notes_data

        for type, name in parsed_identifier:
            current_level = current_level.get(type, {}).get(name, {})

        if note_id not in current_level.get('notes',{}):
            logging.warning(f"Note with ID {note_id} not found.")
            return False

        return current_level.get('notes',{}).get(note_id)

    def get_notes_by_note_type(self, identifier):
        """
        Retrieves notes based on the note type specified in the identifier.

        Args:
            identifier (str): The hierarchical identifier specifying the note type.

        Returns:
            dict: A dictionary of notes of the specified type.
        """
        note_type = identifier.split(':')[0].lower()
        return self.notes_data.get(note_type, {}).get('notes', {})

    def save_notes_structure(self):
        """
        Saves the current notes structure back to the file.
        """
        try:
            with open(self.notes_file, 'w') as file:
                json.dump(self.notes_data, file, indent=4)
            logging.info("Notes structure saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save notes structure: {e}")

    def _generate_unique_id(self):
        """
        Generates a unique identifier for a note.

        Returns:
            str: A unique UUID string.
        """
        return str(uuid.uuid4())

    def _create_note_heading(self, identifier):
        """
        Creates a formatted heading for a note based on its identifier.

        Args:
            identifier (str): The hierarchical identifier of the note.

        Returns:
            str: Formatted note heading.
        """
        parts = identifier.split('/')
        formatted_parts = [f"{part.split(':')[0].capitalize()}: {part.split(':')[1]}" for part in parts]
        return "# Note for " + ', '.join(formatted_parts)

```

## File: app.py
```py
"""
Main Flask application file for handling tasks, notes, and prompts.

This application provides APIs for task management, notes management, and prompt retrieval. 
It enforces API key authentication for secure access and integrates functionalities in a modular fashion, 
ensuring maintainability and scalability.
"""

from flask import Flask
from cors_module import init_cors  
from dotenv import load_dotenv
import os
from error_handler import init_error_handlers 
from log_middleware import configure_logging, init_log_middleware
from api_authenticator import api_auth_instance 
from task_routes import task_blueprint  
from notes_routes import notes_blueprint 
from prompt_routes import prompt_blueprint  
from disk_routes import disk_blueprint

# Load environment variables from .env file
load_dotenv()
configure_logging()

# Initialize Flask app
app = Flask(__name__)
init_log_middleware(app)
# Initialize Cross-Origin Resource Sharing
init_cors(app)

# Initialize error handlers
init_error_handlers(app)

# Initialize logging middleware
init_log_middleware(app)

# Register blueprints for tasks, notes, and prompts
app.register_blueprint(task_blueprint, url_prefix='/tasks')
app.register_blueprint(notes_blueprint, url_prefix='/notes')
app.register_blueprint(prompt_blueprint, url_prefix='/prompts')
app.register_blueprint(disk_blueprint, url_prefix='/disk')

if __name__ == '__main__':
    # Fetch configuration from environment variables
    host_ip = os.getenv('HOST_IP', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'  # Enable debug mode if FLASK_ENV is 'development'

    # Run the Flask application
    app.run(host=host_ip, port=port, debug=debug)

```

## File: type_hierarchy_validator.py
```py
# ./type_hierarchy_validator.py
# This file contains the TypeHierarchyValidator class. This class is designed to load a JSON
# file representing a hierarchy of types and provide methods to validate a sequence of types 
# against this hierarchy and to retrieve the allowed children for a given type. It includes 
# comprehensive error checking and logging.
import re
import json
import logging

class TypeHierarchyValidator:
    """
    Validates the hierarchy of note types based on a defined JSON structure.

    Attributes:
        type_hierarchy (dict): A dictionary representing the type hierarchy loaded from JSON.

    Methods:
        validate_hierarchy(identifier): Validates if a sequence of note types in the identifier adheres to the hierarchy.
    """

    def __init__(self, json_file):
        """
        Initializes the TypeHierarchyValidator class by loading the type hierarchy from a JSON file.

        Args:
            json_file (str): Path to the JSON file containing the type hierarchy.
        """
        try:
            with open(json_file) as f:
                self.type_hierarchy = json.load(f)
                self.type_hierarchy = self._convert_keys_to_lower(self.type_hierarchy)
            logging.info(f"Type hierarchy loaded successfully from {json_file}")
        except FileNotFoundError:
            logging.error(f"JSON file not found: {json_file}")
            raise
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from the file: {json_file}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading the type hierarchy: {str(e)}")
            raise

    def validate_hierarchy(self, identifier):
        """
        Validates if a sequence of note types in the identifier adheres to the defined type hierarchy.

        Args:
            identifier (str): The hierarchical identifier of the note.

        Returns:
            bool: True if the hierarchy is valid, False otherwise.
        """
        note_types = [segment.split(':')[0].lower() for segment in identifier.split('/') if ':' in segment]

        try:
            for i in range(len(note_types) - 1):
                parent, child = note_types[i], note_types[i + 1]
                if child not in self.type_hierarchy['types'][parent]['children']:
                    logging.warning(f"Invalid hierarchy: '{child}' cannot be a child of '{parent}'")
                    return False
            logging.info("Hierarchy validation successful for " + str(note_types))
            return True
        except KeyError as e:
            logging.error("Invalid type encountered in the hierarchy validation: " + str(e))
            return False
        except Exception as e:
            logging.error("An error occurred during hierarchy validation: " + str(e))
            return False

    def _convert_keys_to_lower(self, data):
        """
        Converts all keys in a nested dictionary to lowercase.

        Args:
            data (dict): The dictionary with string keys.

        Returns:
            dict: The dictionary with all keys converted to lowercase.
        """
        if isinstance(data, dict):
            return {k.lower(): self._convert_keys_to_lower(v) for k, v in data.items()}
        return data


def parse_identifier(identifier):
    """
    Parses the hierarchical identifier of a note into its components.

    Args:
        identifier (str): The hierarchical identifier of the note.

    Returns:
        list of tuples: A list of tuples where each tuple contains a type and a name/path.
    """
    pattern = r'<(\w+):([^>]+)>'
    return re.findall(pattern, identifier)
# Example usage:
# validator = TypeHierarchyValidator('./config/type_hierarchy.json')
# note_types = ['project', 'file', 'class', 'method']
# if validator.validate_hierarchy(note_types):
#     print("Note types are valid.")
# else:
#     print("Invalid note types.")
```

## File: prompt_manager.py
```py
# prompt_manager.py
"""
PromptManager Module
----------------------
This module provides functionality to retrieve and serve markdown files from the
'prompts' directory. It is designed to handle requests for specific prompt documents.

Classes:
- PromptManager: Handles the retrieval of markdown prompt files.
"""

import logging
import os

class PromptManager:
    def __init__(self, prompts_dir):
        self.prompts_dir = prompts_dir
        logging.basicConfig(level=logging.INFO)

    def get_prompt(self, filename):
        file_path = os.path.join(self.prompts_dir, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content, None  # No error
        except Exception as e:
            error = str(e)
            return None, error  # Content is None when there's an error
```

## File: task_manager.py
```py
# task_manager.py
# This module is responsible for extracting specific tasks or subtasks from JSON data.

import logging

class TaskManager:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)


    def extract_task_data(self, data, task_number):
        """
        Extracts and returns specific task or subtask data from JSON.
        Args:
        - data (dict): The JSON data.
        - task_number (str): The task number to extract, which can include subtasks like '1.1'.

        Returns:
        - dict: The extracted task or subtask data.
        """
        try:
            if '.' in task_number:
                sub_task = task_number
                main_task = task_number.split('.', 1)[0]
                print(f"sub_task: {sub_task}, main_task: {main_task}")
                task_data = data['tasks'][main_task][sub_task] 
                return {'tasks': {task_number: task_data}}
            else:
                return {'tasks': {task_number: data['tasks'][task_number]}}
        except KeyError as e:
            logging.error(f"Task or subtask not found: {task_number}. Error: {e}")
            return None
```

## File: disk_routes.py
```py
# disk_routes.py
# Purpose: This module defines routes for handling file operations in different formats. 
# It provides an API endpoint for retrieving files stored on disk in specified formats like JSON, Markdown, etc.

from flask import Blueprint, jsonify, request
from disk_manager import DiskManager
import logging
from conversion import convert_json_to_markdown

# Initialize the Blueprint for disk-related routes
disk_blueprint = Blueprint('disk_routes', __name__)
disk_manager = DiskManager()

@disk_blueprint.route('/<project_name>/<path:file_path>', methods=['GET'])
def get_file(project_name, file_path):
    """
    Route to retrieve a file's content based on the specified project and file path.
    The format of the file content is determined by the 'format' query parameter.
    """
    format_type = request.args.get('format', 'json')  # Default to JSON if format is not specified

    logging.info(f"Request received for project '{project_name}' to retrieve file '{file_path}' in format '{format_type}'.")

    try:
        # Read the file content based on the requested format
        file_content = disk_manager.read_file(project_name, file_path, format_type)
        logging.info(f"File content successfully read for file '{file_path}'.")

        if format_type == 'json':
            # Return content as JSON
            logging.info(f"Returning file content as JSON.")
            return jsonify(file_content)
        elif format_type == 'md':
            # Convert JSON content to Markdown and return
            logging.info(f"Converting JSON content to Markdown format.")
            md_content = convert_json_to_markdown(file_content)
            return md_content, 200, {'Content-Type': 'text/markdown'}
        else: 
            # For other formats like txt, yaml, etc., return as plain text
            logging.info(f"Returning file content as plain text.")
            return file_content, 200, {'Content-Type': 'text/plain; charset=utf-8'}

    except FileNotFoundError:
        logging.error(f"File '{file_path}' not found for project '{project_name}'.")
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        logging.exception(f"An error occurred while retrieving the file '{file_path}': {e}")
        return jsonify({'error': 'An error occurred while processing the request'}), 500

```

## File: disk_manager.py
```py
# disk_manager.py
# Purpose: This module provides functionality for managing disk operations such as reading and writing files. 
# It handles various file formats and ensures the files are accessed and stored correctly.

import os
import json
import yaml
import logging
import shutil
from datetime import datetime
from conversion import convert_json_to_markdown

class DiskManager:
    """
    DiskManager class for handling file operations on the server's disk.
    Supports operations such as reading and writing files in various formats.
    """

    def __init__(self, base_path='./disk'):
        """
        Initializes the DiskManager with a base path for file operations.
        Args:
            base_path (str): The base directory path for file operations.
        """
        self.base_path = base_path
        logging.basicConfig(level=logging.INFO)
        logging.info(f"DiskManager initialized with base path: {base_path}")

    def read_file(self, project_name, file_path, format_type):
        """
        Reads a file from the disk based on the given project name, file path, and format type.
        Args:
            project_name (str): The name of the project folder.
            file_path (str): The relative path of the file within the project folder.
            format_type (str): The format type of the file (e.g., 'json', 'yaml', 'txt').
        Returns:
            The content of the file in the requested format.
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        file_extension = '.' + format_type
        full_path = os.path.join(self.base_path, project_name, file_path + file_extension)

        if not os.path.exists(full_path):
            logging.error(f"File not found: {full_path}")
            raise FileNotFoundError(f"File not found: {full_path}")

        try:
            with open(full_path, 'r', encoding='utf-8') as file:
                logging.info(f"Reading file: {full_path}")
                if format_type == 'json':
                    return json.load(file)
                elif format_type in ['yml', 'yaml']:
                    return yaml.safe_load(file)
                else:
                    return file.read()
        except Exception as e:
            logging.error(f"Error reading file {full_path}: {e}")
            raise

    def write_file(self, project_name, file_path, content, format_type):
        """
        Writes content to a file on the disk based on the given project name, file path, and format type.
        Args:
            project_name (str): The name of the project folder.
            file_path (str): The relative path of the file within the project folder.
            content: The content to be written to the file.
            format_type (str): The format type of the file (e.g., 'json', 'yaml').
        Raises:
            Exception: If there is an error in writing to the file.
        """
        file_extension = '.' + format_type
        full_path = os.path.join(self.base_path, project_name, file_path + file_extension)

        # Create a backup of the existing file
        self._create_backup(full_path)

        try:
            with open(full_path, 'w', encoding='utf-8') as file:
                logging.info(f"Writing to file: {full_path}")
                if format_type == 'json':
                    json.dump(content, file, indent=4)
                elif format_type in ['yml', 'yaml']:
                    yaml.safe_dump(content, file)
                else:
                    file.write(content)
            logging.info(f"File successfully written to {full_path}")
        except Exception as e:
            logging.error(f"Error writing to file {full_path}: {e}")
            raise

    def _create_backup(self, full_path):
        """
        Creates a backup of an existing file.
        Args:
            full_path (str): The full path to the file for which a backup is to be created.
        """
        if os.path.exists(full_path):
            backup_dir = os.path.join(os.path.dirname(full_path), 'backups')
            os.makedirs(backup_dir, exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            backup_path = os.path.join(backup_dir, os.path.basename(full_path) + '-' + timestamp)
            shutil.copy(full_path, backup_path)
            logging.info(f"Backup created for {full_path} at {backup_path}")

```

## File: conversion.py
```py
# conversion_module.py
import json

def convert_json_to_markdown(openapi_json):
    md_content = ""

    # Adding general information
    info = openapi_json.get("info", {})
    md_content += f"# {info.get('title', 'API Documentation')}\n"
    md_content += f"**Version:** {info.get('version', 'N/A')}\n\n"
    md_content += f"{info.get('description', '')}\n\n"

    # Adding server information
    servers = openapi_json.get("servers", [])
    if servers:
        md_content += "## Servers\n"
        for server in servers:
            md_content += f"- URL: {server.get('url', 'N/A')}\n"
        md_content += "\n"

    # Adding paths and operations
    paths = openapi_json.get("paths", {})
    for path, operations in paths.items():
        md_content += f"## Path: `{path}`\n\n"
        for operation, details in operations.items():
            md_content += f"### {operation.upper()}\n"
            md_content += f"**Summary:** {details.get('summary', 'N/A')}\n\n"
            md_content += f"**Description:** {details.get('description', 'N/A')}\n\n"
            md_content += "#### Parameters\n"
            for param in details.get('parameters', []):
                md_content += f"- {param.get('name', 'N/A')} ({param.get('in', 'N/A')}): {param.get('description', 'N/A')}\n"
            md_content += "\n"

            # Responses
            responses = details.get("responses", {})
            md_content += "#### Responses\n"
            for status_code, response_details in responses.items():
                md_content += f"- Status {status_code}: {response_details.get('description', 'N/A')}\n"
                md_content += "\n"


            # Components (Schemas)
            components = openapi_json.get("components", {}).get("schemas", {})
            if components:
                md_content += "## Components (Schemas)\n\n"
                for schema_name, schema_details in components.items():
                    md_content += f"### {schema_name}\n"
                    properties = schema_details.get('properties', {})
                    for prop_name, prop_details in properties.items():
                        md_content += f"- **{prop_name}**: {prop_details.get('type', 'N/A')}\n"
                        if 'description' in prop_details:
                            md_content += f"  - Description: {prop_details['description']}\n"
                    md_content += "\n"

            return md_content


```



<p id="hidden_comment">
    This is a hidden comment. It explains that the following style tag is meant to 
    style HTML content if this Markdown is converted to HTML. This comment should 
    not be visible in most Markdown renderers.
</p>
<style>
    #hidden_comment {
        display: none;
    }
    table {
        width: 100%;
    }
    table tr:first-child {
        font-weight: bold;
    }
    table tr:last-child {
        font-style: italic;
    }
</style>
