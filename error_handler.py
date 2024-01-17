# error_handler.py
from flask import jsonify, request
import logging
from datetime import datetime
import os

# Read the base path for error logs from the environment variable
base_error_log_path = os.getenv('ERROR_LOG_PATH', './logs/error-log-')

# Generate the full log file path with the current date
date_str = datetime.now().strftime('%Y%m%d')
error_log_file_path = f"{base_error_log_path}{date_str}.log"

# Set up the logger
logger = logging.getLogger('error_logger')

# Create the logs directory if it doesn't exist
log_dir = os.path.dirname(error_log_file_path)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up the file handler with the generated log file path
file_handler = logging.FileHandler(error_log_file_path)
logger.addHandler(file_handler)

# Set the desired log level
log_level_str = os.getenv('LOGGER_LEVEL', 'ERROR').upper()
log_level = getattr(logging, log_level_str, logging.ERROR)
logger.setLevel(log_level)

def init_error_handlers(app):
    """
    Initializes error handlers for common HTTP errors.

    Args:
        app: Flask application instance.
    """
    @app.errorhandler(404)
    def handle_404_error(e):
        log_error('404 Not Found', request)
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(500)
    def handle_500_error(e):
        log_error('500 Internal Server Error', request)
        return jsonify({'error': 'Internal server error'}), 500

    @app.errorhandler(400)
    def handle_400_error(e):
        log_error('400 Bad Request', request)
        return jsonify({'error': 'Bad request'}), 400


    @app.errorhandler(401)
    def handle_401_error(e):
        log_error('401 Unauthorized', request)
        return jsonify({'error': 'Unauthorized'}), 401

    @app.errorhandler(403)
    def handle_403_error(e):
        log_error('403 Forbidden', request)
        return jsonify({'error': 'Forbidden'}), 403

    @app.errorhandler(405)
    def handle_405_error(e):
        log_error('405 Method Not Allowed', request)
        return jsonify({'error': 'Method not allowed'}), 405

    @app.errorhandler(408)
    def handle_408_error(e):
        log_error('408 Request Timeout', request)
        return jsonify({'error': 'Request timeout'}), 408

    @app.errorhandler(413)
    def handle_413_error(e):
        log_error('413 Payload Too Large', request)
        return jsonify({'error': 'Payload too large'}), 413

    @app.errorhandler(429)
    def handle_429_error(e):
        log_error('429 Too Many Requests', request)
        return jsonify({'error': 'Too many requests'}), 429

    @app.errorhandler(503)
    def handle_503_error(e):
        log_error('503 Service Unavailable', request)
        return jsonify({'error': 'Service unavailable'}), 503

    def log_error(error_message, request):
        """
        Logs error details to the specified log file.

        Args:
            error_message (str): Description of the error.
            request: Flask request object.
        """
        user_ip = request.remote_addr
        user_agent = request.headers.get('User-Agent', 'Unknown')
        logger.error(f"{datetime.now()} - Error: {error_message}, IP: {user_ip}, User-Agent: {user_agent}")

