# disk_manager.py
# Purpose: This module provides functionality for managing disk operations such as reading and writing files. 
# It handles various file formats and ensures the files are accessed and stored correctly.

import os
import json
import yaml
import logging
import shutil
from datetime import datetime
from conversion import convert_json_to_markdown

class DiskManager:
    """
    DiskManager class for handling file operations on the server's disk.
    Supports operations such as reading and writing files in various formats.
    """

    def __init__(self, base_path='./disk'):
        """
        Initializes the DiskManager with a base path for file operations.
        Args:
            base_path (str): The base directory path for file operations.
        """
        self.base_path = base_path
        logging.basicConfig(level=logging.INFO)
        logging.info(f"DiskManager initialized with base path: {base_path}")

    def read_file(self, project_name, file_path, format_type):
        """
        Reads a file from the disk based on the given project name, file path, and format type.
        Args:
            project_name (str): The name of the project folder.
            file_path (str): The relative path of the file within the project folder.
            format_type (str): The format type of the file (e.g., 'json', 'yaml', 'txt').
        Returns:
            The content of the file in the requested format.
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        file_extension = '.' + format_type
        full_path = os.path.join(self.base_path, project_name, file_path + file_extension)

        if not os.path.exists(full_path):
            logging.error(f"File not found: {full_path}")
            raise FileNotFoundError(f"File not found: {full_path}")

        try:
            with open(full_path, 'r', encoding='utf-8') as file:
                logging.info(f"Reading file: {full_path}")
                if format_type == 'json':
                    return json.load(file)
                elif format_type in ['yml', 'yaml']:
                    return yaml.safe_load(file)
                else:
                    return file.read()
        except Exception as e:
            logging.error(f"Error reading file {full_path}: {e}")
            raise

    def write_file(self, project_name, file_path, content, format_type):
        """
        Writes content to a file on the disk based on the given project name, file path, and format type.
        Args:
            project_name (str): The name of the project folder.
            file_path (str): The relative path of the file within the project folder.
            content: The content to be written to the file.
            format_type (str): The format type of the file (e.g., 'json', 'yaml').
        Raises:
            Exception: If there is an error in writing to the file.
        """
        file_extension = '.' + format_type
        full_path = os.path.join(self.base_path, project_name, file_path + file_extension)

        # Create a backup of the existing file
        self._create_backup(full_path)

        try:
            with open(full_path, 'w', encoding='utf-8') as file:
                logging.info(f"Writing to file: {full_path}")
                if format_type == 'json':
                    json.dump(content, file, indent=4)
                elif format_type in ['yml', 'yaml']:
                    yaml.safe_dump(content, file)
                else:
                    file.write(content)
            logging.info(f"File successfully written to {full_path}")
        except Exception as e:
            logging.error(f"Error writing to file {full_path}: {e}")
            raise

    def _create_backup(self, full_path):
        """
        Creates a backup of an existing file.
        Args:
            full_path (str): The full path to the file for which a backup is to be created.
        """
        if os.path.exists(full_path):
            backup_dir = os.path.join(os.path.dirname(full_path), 'backups')
            os.makedirs(backup_dir, exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            backup_path = os.path.join(backup_dir, os.path.basename(full_path) + '-' + timestamp)
            shutil.copy(full_path, backup_path)
            logging.info(f"Backup created for {full_path} at {backup_path}")
