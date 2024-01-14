# ./type_hierarchy_validator.py
# This file contains the TypeHierarchyValidator class. This class is designed to load a JSON
# file representing a hierarchy of types and provide methods to validate a sequence of types 
# against this hierarchy and to retrieve the allowed children for a given type. It includes 
# comprehensive error checking and logging.

import json
import logging

# Setting up logging
logging.basicConfig(filename='type_hierarchy.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TypeHierarchyValidator:
    def __init__(self, json_file):
        """
        Initializes the TypeHierarchyValidator class by loading the type hierarchy from a JSON file.
        """
        self.type_hierarchy = None
        try:
            with open(json_file) as f:
                self.type_hierarchy = json.load(f)
            logging.info("Type hierarchy loaded successfully from {}".format(json_file))
        except FileNotFoundError:
            logging.error("JSON file not found: {}".format(json_file))
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the file: {}".format(json_file))
            raise
        except Exception as e:
            logging.error("An error occurred while loading the type hierarchy: {}".format(str(e)))
            raise

    def validate_hierarchy(self, note_types):
        """
        Validates if a sequence of note types adheres to the defined type hierarchy.
        Returns True if valid, False otherwise.
        """
        try:
            for i in range(len(note_types) - 1):
                parent, child = note_types[i], note_types[i + 1]
                if child not in self.type_hierarchy['types'][parent]['children']:
                    logging.warning("Invalid hierarchy: '{}' cannot be a child of '{}'".format(child, parent))
                    return False
            logging.info("Hierarchy validation successful for {}".format(note_types))
            return True
        except KeyError as e:
            logging.error("Invalid type encountered in the hierarchy validation: {}".format(str(e)))
            return False
        except Exception as e:
            logging.error("An error occurred during hierarchy validation: {}".format(str(e)))
            return False

# Example usage:
# validator = TypeHierarchyValidator('type_hierarchy.json')
# note_types = ['PROJECT', 'FILE', 'CLASS', 'METHOD']
# if validator.validate_hierarchy(note_types):
#     print("Note types are valid.")
# else:
#     print("Invalid note types.")