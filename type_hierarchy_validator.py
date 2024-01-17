# ./type_hierarchy_validator.py
# This file contains the TypeHierarchyValidator class. This class is designed to load a JSON
# file representing a hierarchy of types and provide methods to validate a sequence of types 
# against this hierarchy and to retrieve the allowed children for a given type. It includes 
# comprehensive error checking and logging.
import re
import json
import logging

class TypeHierarchyValidator:
    """
    Validates the hierarchy of note types based on a defined JSON structure.

    Attributes:
        type_hierarchy (dict): A dictionary representing the type hierarchy loaded from JSON.

    Methods:
        validate_hierarchy(identifier): Validates if a sequence of note types in the identifier adheres to the hierarchy.
    """

    def __init__(self, json_file):
        """
        Initializes the TypeHierarchyValidator class by loading the type hierarchy from a JSON file.

        Args:
            json_file (str): Path to the JSON file containing the type hierarchy.
        """
        try:
            with open(json_file) as f:
                self.type_hierarchy = json.load(f)
                self.type_hierarchy = self._convert_keys_to_lower(self.type_hierarchy)
            logging.info(f"Type hierarchy loaded successfully from {json_file}")
        except FileNotFoundError:
            logging.error(f"JSON file not found: {json_file}")
            raise
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from the file: {json_file}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading the type hierarchy: {str(e)}")
            raise

    def validate_hierarchy(self, identifier):
        """
        Validates if a sequence of note types in the identifier adheres to the defined type hierarchy.

        Args:
            identifier (str): The hierarchical identifier of the note.

        Returns:
            bool: True if the hierarchy is valid, False otherwise.
        """
        note_types = [segment.split(':')[0].lower() for segment in identifier.split('/') if ':' in segment]

        try:
            for i in range(len(note_types) - 1):
                parent, child = note_types[i], note_types[i + 1]
                if child not in self.type_hierarchy['types'][parent]['children']:
                    logging.warning(f"Invalid hierarchy: '{child}' cannot be a child of '{parent}'")
                    return False
            logging.info("Hierarchy validation successful for " + str(note_types))
            return True
        except KeyError as e:
            logging.error("Invalid type encountered in the hierarchy validation: " + str(e))
            return False
        except Exception as e:
            logging.error("An error occurred during hierarchy validation: " + str(e))
            return False

    def _convert_keys_to_lower(self, data):
        """
        Converts all keys in a nested dictionary to lowercase.

        Args:
            data (dict): The dictionary with string keys.

        Returns:
            dict: The dictionary with all keys converted to lowercase.
        """
        if isinstance(data, dict):
            return {k.lower(): self._convert_keys_to_lower(v) for k, v in data.items()}
        return data


def parse_identifier(identifier):
    """
    Parses the hierarchical identifier of a note into its components.

    Args:
        identifier (str): The hierarchical identifier of the note.

    Returns:
        list of tuples: A list of tuples where each tuple contains a type and a name/path.
    """
    pattern = r'<(\w+):([^>]+)>'
    return re.findall(pattern, identifier)
# Example usage:
# validator = TypeHierarchyValidator('./config/type_hierarchy.json')
# note_types = ['project', 'file', 'class', 'method']
# if validator.validate_hierarchy(note_types):
#     print("Note types are valid.")
# else:
#     print("Invalid note types.")