# ./file_handler.py
# This module handles file operations, including reading JSON files.

import json
import logging

class FileHandler:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def read_json_file(self, file_path):
        """
        Reads and returns the content of a JSON file.
        Args:
        - file_path (str): The path to the JSON file.

        Returns:
        - dict: The content of the JSON file if successful, None otherwise.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            return None
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from {file_path}: {e}")
            return None

    def write_json_file(self, file_path, data):
        """
        Writes the given data to a JSON file.

        Args:
            file_path (str): The path to the JSON file.
            data (dict): The data to write to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            logging.info(f"Data successfully written to {file_path}")
        except Exception as e:
            logging.error(f"Failed to write data to {file_path}: {e}")
            raise
