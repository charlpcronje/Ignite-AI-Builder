# prompt_manager.py
"""
PromptManager Module
----------------------
This module provides functionality to retrieve and serve markdown files from the
'prompts' directory. It is designed to handle requests for specific prompt documents.

Classes:
- PromptManager: Handles the retrieval of markdown prompt files.
"""

import logging
import os

class PromptManager:
    def __init__(self, prompts_dir):
        self.prompts_dir = prompts_dir
        logging.basicConfig(level=logging.INFO)

    def get_prompt(self, filename):
        file_path = os.path.join(self.prompts_dir, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content, None  # No error
        except Exception as e:
            error = str(e)
            return None, error  # Content is None when there's an error