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
    log_file_path = os.getenv('REQUEST_LOG_PATH', 'default.log') + datetime.now().strftime('%Y%m%d') + '.log'

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

# Ensure this is called once during the application setup
configure_logging()
