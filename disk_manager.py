# disk_manager.py
import os
import json
import yaml
import logging
import shutil
from datetime import datetime
from conversion_module import convert_json_to_markdown

class DiskManager:
    def __init__(self, base_path='./disk'):
        self.base_path = base_path

    def read_file(self, project_name, file_path, format_type):
        file_extension = '.' + format_type
        full_path = os.path.join(self.base_path, project_name, file_path + file_extension)

        if not os.path.exists(full_path):
            logging.error(f"File not found: {full_path}")
            raise FileNotFoundError(f"File not found: {full_path}")

        try:
            with open(full_path, 'r', encoding='utf-8') as file:
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
        file_extension = '.' + format_type
        full_path = os.path.join(self.base_path, project_name, file_path + file_extension)

        # Create a backup of the existing file
        self._create_backup(full_path)

        try:
            with open(full_path, 'w', encoding='utf-8') as file:
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
        if os.path.exists(full_path):
            backup_dir = os.path.join(os.path.dirname(full_path), 'backups')
            os.makedirs(backup_dir, exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            backup_path = os.path.join(backup_dir, os.path.basename(full_path) + '-' + timestamp)
            shutil.copy(full_path, backup_path)