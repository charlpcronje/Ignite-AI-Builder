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