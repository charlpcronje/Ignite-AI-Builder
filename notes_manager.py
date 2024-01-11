# ./notes_manager.py
"""
Notes Manager Module
--------------------
Manages notes stored in a JSON file within the notes directory. This module provides 
functionalities to read, write, add, update, and delete notes, handling data persistence 
and integrity. It includes error handling and logging to ensure robustness and reliability.

Classes:
- NotesManager: Manages operations related to notes stored in a JSON file.

Dependencies:
- json: For reading and writing JSON data.
- logging: For logging error and informational messages.
- os, datetime, shutil: For handling file operations and timestamp generation.
"""

import json
import logging
import os
from datetime import datetime
from shutil import copy2

class NotesManager:
    def __init__(self, notes_file_path, backup_dir):
        """
        Initializes the NotesManager with paths for notes file and backup directory.

        Args:
            notes_file_path (str): Path to the notes JSON file.
            backup_dir (str): Path to the directory where backups of notes file will be stored.
        """
        self.notes_file_path = notes_file_path
        self.backup_dir = backup_dir
        logging.basicConfig(level=logging.INFO)

    def backup_notes_file(self):
        """
        Creates a backup of the current notes file.
        """
        backup_file = os.path.join(self.backup_dir, f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.json")
        try:
            copy2(self.notes_file_path, backup_file)
            logging.info(f"Backup created: {backup_file}")
        except Exception as e:
            logging.error(f"Failed to backup notes file: {e}")

    def read_notes(self):
        """
        Reads and returns the content of the notes file.

        Returns:
            dict: The content of the notes file.
        """
        try:
            with open(self.notes_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error("Notes file not found.")
            return {}
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
            return {}

    def write_notes(self, notes_data):
        """
        Writes the provided notes data to the notes file.

        Args:
            notes_data (dict): The notes data to write to the file.
        """
        self.backup_notes_file()
        try:
            with open(self.notes_file_path, 'w') as file:
                json.dump(notes_data, file, indent=4)
            logging.info("Notes file updated successfully.")
        except Exception as e:
            logging.error(f"Failed to write to notes file: {e}")

    def add_note(self, note_content, level, identifier=None):
        """
        Adds a new note to the specified level and identifier in the notes file.

        Args:
            note_content (str): The content of the note to be added.
            level (str): The level at which the note is to be added (e.g., project, file).
            identifier (str, optional): A specific identifier within the level (e.g., project_name).

        Returns:
            str: The ID of the added note.
        """
        notes_data = self.read_notes()
        note_id = str(max([int(k) for k in notes_data.get(level, {}).get('notes', {}).keys()], default=0) + 1)
        new_note = {
            "datetime": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "content": note_content
        }

        if level not in notes_data:
            notes_data[level] = {"notes": {}}
        if identifier:
            if identifier not in notes_data[level]:
                notes_data[level][identifier] = {"notes": {}}
            notes_data[level][identifier]['notes'][note_id] = new_note
        else:
            notes_data[level]['notes'][note_id] = new_note

        self.write_notes(notes_data)
        logging.info(f"Note {note_id} added at level {level}, identifier {identifier}.")
        return note_id

    def update_note(self, note_id, updated_content, level, identifier=None):
        """
        Updates an existing note in the notes file.

        Args:
            note_id (str): The ID of the note to be updated.
            updated_content (str): The new content for the note.
            level (str): The level where the note resides.
            identifier (str, optional): A specific identifier within the level.

        Returns:
            bool: True if update was successful, False otherwise.
        """
        notes_data = self.read_notes()
        try:
            if identifier:
                notes_data[level][identifier]['notes'][note_id]['content'] = updated_content
            else:
                notes_data[level]['notes'][note_id]['content'] = updated_content
            self.write_notes(notes_data)
            logging.info(f"Note {note_id} at level {level}, identifier {identifier} updated.")
            return True
        except KeyError:
            logging.error(f"Note {note_id} to update not found at level {level}, identifier {identifier}.")
            return False

    def delete_note(self, note_id, level, identifier=None):
        """
        Deletes a note from the notes file.

        Args:
            note_id (str): The ID of the note to be deleted.
            level (str): The level where the note resides.
            identifier (str, optional): A specific identifier within the level.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        notes_data = self.read_notes()
        try:
            if identifier:
                del notes_data[level][identifier]['notes'][note_id]
            else:
                del notes_data[level]['notes'][note_id]
            self.write_notes(notes_data)
            logging.info(f"Note {note_id} at level {level}, identifier {identifier} deleted.")
            return True
        except KeyError:
            logging.error(f"Note {note_id} to delete not found at level {level}, identifier {identifier}.")
            return False
