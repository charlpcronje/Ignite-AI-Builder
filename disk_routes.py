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
            # Return markdown content
            return file_content, 200, {'Content-Type': 'text/markdown'}
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
