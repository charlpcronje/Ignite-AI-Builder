# ./markdown_converter.py
"""
MarkdownConverter Module
------------------------
Responsible for converting JSON data to Markdown format. This module is utilized in 
transforming task data into a readable Markdown format, enhancing the user's understanding 
and interaction with the data.

Classes:
- MarkdownConverter: Converts JSON data to a well-structured Markdown format.

Dependencies:
- logging: To log error messages and informational messages.
"""

import logging

class MarkdownConverter:
    def __init__(self):
        """
        Initializes the MarkdownConverter with basic logging configuration.
        """
        logging.basicConfig(level=logging.INFO)

    def convert_to_markdown(self, data):
        print(data)
        """
        Converts JSON data to Markdown format.

        Args:
            data (dict): The JSON data to be converted.

        Returns:
            str: The converted Markdown string, or an error message in case of failure.
        """
        try:
            md_content = data.get("overview", "") + "\n\n"

            # Check if the data contains a single subtask or multiple tasks
            if 'tasks' in data:
                for task_key, task_info in data["tasks"].items():
                    if 'description' in task_info:
                        # Main task with description and subtasks
                        md_content += f"## [{'x' if task_info['status'] else ' '}] {task_key}. {task_info['description']}\n"
                        for subtask_key, subtask_info in task_info.items():
                            if isinstance(subtask_info, dict) and 'task' in subtask_info:
                                md_content += f"- [{'x' if subtask_info['status'] else ' '}] {subtask_key}. {subtask_info['task']}\n"
                        md_content += "\n"
                    else:
                        # Individual subtask without a main task
                        md_content += f"- [{'x' if task_info['status'] else ' '}] {task_key}. {task_info['task']}\n"
            else:
                # Fallback for unexpected data format
                md_content += "Error: Unrecognized data format for Markdown conversion.\n"

            return md_content
        except Exception as e:
            logging.error(f"Error converting JSON to Markdown: {e}")
            return "Error in Markdown conversion"

# Example usage:
# converter = MarkdownConverter()
# markdown_text = converter.convert_to_markdown(json_data)
