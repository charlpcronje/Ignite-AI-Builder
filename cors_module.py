# cors_module.py
from flask_cors import CORS
import json

def init_cors(app, config_path='./config/cors.config.json'):
    """
    Initialize CORS for a Flask application using settings from a JSON configuration file.

    Args:
        app: The Flask application instance.
        config_path (str): Path to the JSON file containing CORS configuration.
    """
    try:
        with open(config_path, 'r') as config_file:
            cors_config = json.load(config_file)
            CORS(app, resources={r"/api/*": cors_config})
            print("CORS initialized with config:", cors_config)
    except FileNotFoundError:
        print(f"CORS config file not found at {config_path}. Using default settings.")
        CORS(app)  # Initialize with default settings if config file is not found
    except json.JSONDecodeError:
        print("Error parsing CORS config JSON. Using default settings.")
        CORS(app)
