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
