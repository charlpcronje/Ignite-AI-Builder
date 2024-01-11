# ./app.py
"""
Main Flask application file that integrates the modular components for handling tasks, notes, and prompts.

This application provides APIs for task management, notes management, and prompt retrieval. It enforces API key authentication for secure access and integrates various functionalities in a modular fashion, ensuring maintainability and scalability.

Classes:
- Flask: The main class for the Flask application.
"""

from flask import Flask
import logging
from dotenv import load_dotenv
import os
from api_authenticator import api_auth_instance
from task_routes import task_blueprint
from notes_routes import notes_blueprint
from prompt_routes import prompt_blueprint

load_dotenv()
# Initialize Flask app and configure logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Register blueprints for tasks, notes, and prompts
app.register_blueprint(task_blueprint, url_prefix='/tasks')
app.register_blueprint(notes_blueprint, url_prefix='/notes')
app.register_blueprint(prompt_blueprint, url_prefix='/prompts')

if __name__ == '__main__':
    host_ip = os.getenv('HOST_IP', '127.0.0.1')
    port = os.getenv('PORT', 5000)  # You can add PORT to your .env if needed
    debug = os.getenv('FLASK_ENV') == 'development'  # debug is true if FLASK_ENV is 'development'

    app.run(host=host_ip, port=port, debug=debug)
