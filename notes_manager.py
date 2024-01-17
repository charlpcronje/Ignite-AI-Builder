# notes_manager.py
import json
import logging
import uuid
from type_hierarchy_validator import TypeHierarchyValidator, parse_identifier
import datetime

class NotesManager:
    """
    Manages notes stored in a JSON file. Provides functionalities to add, update, delete, and retrieve notes.

    Attributes:
        validator (TypeHierarchyValidator): Validator for note type hierarchy.
        notes_file (str): Path to the notes JSON file.
        notes_data (dict): Data structure containing notes.
    """

    def __init__(self, notes_file, validator):
        """
        Initializes the NotesManager with the notes file path and a hierarchy validator.
        
        Args:
            notes_file (str): Path to the notes JSON file.
            validator (TypeHierarchyValidator): Validator for note type hierarchy.
        """
        self.validator = validator
        self.notes_file = notes_file
        self.notes_data = self._load_notes_data(notes_file)

    def _load_notes_data(self, notes_file):
        """
        Loads the notes data from the specified file.
        
        Args:
            notes_file (str): Path to the notes JSON file.
        
        Returns:
            dict: Data structure containing notes.
        
        Raises:
            Exception: If there is an error in loading the file.
        """
        try:
            with open(notes_file, 'r') as file:
                return json.load(file)
        except Exception as e:
            logging.error(f"Error loading notes data: {e}")
            raise

    def add_note(self, identifier, content, api_key):
        """
        Adds a new note to the notes structure based on the given identifier.

        Args:
            identifier (str): A string representing the hierarchical path of the note.
            content (str): The content of the note.
            api_key (str): The API key associated with the note.

        Returns:
            bool: True if the note is added successfully, False otherwise.
        """
        
        parsed_identifier = parse_identifier(identifier)
        current_level = self.notes_data

        for type, name in parsed_identifier:
            current_level = current_level.setdefault(type, {}).setdefault(name, {})

        new_note_id = self._generate_unique_id()
        created_at = datetime.datetime.now().isoformat()
        current_level['notes'][new_note_id] = {
            "content": content,
            "created_at": created_at,
            "created_by": api_key
        }

        self.save_notes_structure()
        return True, new_note_id

    def update_note(self, note_id, identifier, updates):
        """
        Updates an existing note based on its ID and identifier.

        Args:
            note_id (str): The unique ID of the note to update.
            identifier (str): The hierarchical identifier of the note.
            updates (dict): A dictionary containing the updated fields.

        Returns:
            bool: True if the update is successful, False otherwise.
        """
        parsed_identifier = parse_identifier(identifier)
        current_level = self.notes_data

        for type, name in parsed_identifier:
            current_level = current_level.get(type, {}).get(name, {})

        note_to_update = current_level.get("notes", {}).get(note_id)
        if not note_to_update:
            logging.warning(f"Note with ID {note_id} not found.")
            return False

        note_to_update.update(updates['updates'])
        note_to_update["updated_at"] = datetime.datetime.now().isoformat()

        self.save_notes_structure()
        logging.info(f"Note with ID {note_id} updated successfully.")
        return True

    def delete_note(self, note_id, identifier):
        """
        Deletes a note based on its ID and identifier.

        Args:
            note_id (str): The unique ID of the note to delete.
            identifier (str): The hierarchical identifier of the note.

        Returns:
            bool: True if the deletion is successful, False otherwise.
        """
        parsed_identifier = parse_identifier(identifier)
        current_level = self.notes_data

        for type, name in parsed_identifier:
            current_level = current_level.get(type, {}).get(name, {})

        note_to_delete = current_level.get("notes", {}).get(note_id)
        if not note_to_delete:
            logging.warning(f"Note with ID {note_id} not found.")
            return False

        note_to_delete = current_level.get('notes', {}).get(note_id)

        if note_id not in current_level.get('notes', {}):
            logging.warning(f"Note with ID {note_id} not found.")
            return False

        del current_level['notes'][note_id]
        self.save_notes_structure()
        logging.info(f"Note with ID {note_id} deleted successfully.")
        return True

    def get_note_by_id(self, note_id, identifier):
        """
        Retrieves a note by its ID and identifier.

        Args:
            note_id (str): The unique ID of the note.
            identifier (str): The hierarchical identifier of the note.

        Returns:
            dict or None: The note if found, None otherwise.
        """
        parsed_identifier = parse_identifier(identifier)
        current_level = self.notes_data

        for type, name in parsed_identifier:
            current_level = current_level.get(type, {}).get(name, {})

        if note_id not in current_level.get('notes',{}):
            logging.warning(f"Note with ID {note_id} not found.")
            return False

        return current_level.get('notes',{}).get(note_id)

    def get_notes_by_note_type(self, identifier):
        """
        Retrieves notes based on the note type specified in the identifier.

        Args:
            identifier (str): The hierarchical identifier specifying the note type.

        Returns:
            dict: A dictionary of notes of the specified type.
        """
        note_type = identifier.split(':')[0].lower()
        return self.notes_data.get(note_type, {}).get('notes', {})

    def save_notes_structure(self):
        """
        Saves the current notes structure back to the file.
        """
        try:
            with open(self.notes_file, 'w') as file:
                json.dump(self.notes_data, file, indent=4)
            logging.info("Notes structure saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save notes structure: {e}")

    def _generate_unique_id(self):
        """
        Generates a unique identifier for a note.

        Returns:
            str: A unique UUID string.
        """
        return str(uuid.uuid4())

    def _create_note_heading(self, identifier):
        """
        Creates a formatted heading for a note based on its identifier.

        Args:
            identifier (str): The hierarchical identifier of the note.

        Returns:
            str: Formatted note heading.
        """
        parts = identifier.split('/')
        formatted_parts = [f"{part.split(':')[0].capitalize()}: {part.split(':')[1]}" for part in parts]
        return "# Note for " + ', '.join(formatted_parts)
