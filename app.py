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
