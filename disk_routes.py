# disk_routes.py

from flask import Blueprint, jsonify, request
from disk_manager import DiskManager
import logging

disk_blueprint = Blueprint('disk_routes', __name__)
disk_manager = DiskManager()

@disk_blueprint.route('/<project_name>/<path:file_path>', methods=['GET'])
def get_file(project_name, file_path):
    format_type = request.args.get('format', 'json')  # Default to json if not specified
    try:
        file_content = disk_manager.read_file(project_name,file_path, format_type)
        if format_type == 'json':
            return jsonify(file_content)
        else: # For txt, yaml, md, etc.
            return file_content, 200, {'Content-Type': 'text/plain; charset=utf-8'}

    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        logging.exception(f"An error occurred while retrieving the file: {e}")
    return jsonify({'error': 'An error occurred while processing the request'}), 500


@disk_blueprint.route('/<project_name>/<path:file_path>', methods=['GET'])
def get_file(project_name, file_path):
    format_type = request.args.get('format', 'json')

    if format_type == 'md':
        # Assuming the file_path points to a JSON file
        json_content = disk_manager.read_file(project_name, file_path, 'json')
        md_content = convert_json_to_markdown(json_content)
        return md_content, 200, {'Content-Type': 'text/markdown'}