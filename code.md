```py
# app.py
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

```py
# log_middleware.py
import logging
import json
import os
from datetime import datetime
from flask import request
import sys

def configure_logging():
    """
    Configures the global logging settings for the application.
    Outputs logs to both a file and the console.
    """
    # Corrected print statement
    print("REQUEST_LOG_PATH:", os.getenv('REQUEST_LOG_PATH'))
    log_file_path = os.getenv('REQUEST_LOG_PATH', '') + datetime.now().strftime('%Y%m%d') + '.log'
    print("LOG_FILE_PATH:", log_file_path)

    # Clear existing handlers
    root_logger = logging.getLogger()
    root_logger.handlers = []

    # Set the logging level
    root_logger.setLevel(logging.DEBUG)

    # Configure file handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)
    # Include filename and line number in the log format
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)d - %(message)s')
    file_handler.setFormatter(file_formatter)
    root_logger.addHandler(file_handler)

    # Configure console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    # Include filename and line number in the log format
    console_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)d - %(message)s')
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)


def init_log_middleware(app):
    """
    Initializes middleware for logging requests and responses in a Flask app.

    Args:
        app: Flask application instance.
    """
    @app.before_request
    def log_request():
        log_details('Request', request)
        if 'debug' in request.args and request.args['debug'] == 'true':
            print('HELLO')
            debug_log_details(request)

    @app.after_request
    def log_response(response):
        log_details('Response', request, response)
        return response

def log_details(log_type, request, response=None):
    """
    Logs request or response details.

    Args:
        log_type (str): Indicates 'Request' or 'Response'.
        request: Flask request object.
        response: Flask response object (optional).
    """
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')
    log_data = f"Type: {log_type}, IP: {user_ip}, User-Agent: {user_agent}"
    if response:
        log_data += f", Status: {response.status_code}"

    logger = logging.getLogger(__name__)
    logger.info(log_data)

def debug_log_details(request):
    """
    Logs detailed request information including query parameters, headers, and body for debugging.
    """
    logger = logging.getLogger(__name__)
    log_data = {
        "Time": datetime.now().isoformat(),
        "Endpoint": request.path,
        "Method": request.method,
        "Query Params": dict(request.args),
        "Headers": dict(request.headers),
        "Body": request.get_json() if request.is_json else None
    }
    logger.debug(f"Debug Request Info: {json.dumps(log_data, indent=4)}")

```