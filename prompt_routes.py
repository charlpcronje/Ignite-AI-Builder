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
