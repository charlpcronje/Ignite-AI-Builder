# task_manager.py
# This module is responsible for extracting specific tasks or subtasks from JSON data.

import logging

class TaskManager:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)


    def extract_task_data(self, data, task_number):
        """
        Extracts and returns specific task or subtask data from JSON.
        Args:
        - data (dict): The JSON data.
        - task_number (str): The task number to extract, which can include subtasks like '1.1'.

        Returns:
        - dict: The extracted task or subtask data.
        """
        try:
            if '.' in task_number:
                sub_task = task_number
                main_task = task_number.split('.', 1)[0]
                print(f"sub_task: {sub_task}, main_task: {main_task}")
                task_data = data['tasks'][main_task][sub_task] 
                return {'tasks': {task_number: task_data}}
            else:
                return {'tasks': {task_number: data['tasks'][task_number]}}
        except KeyError as e:
            logging.error(f"Task or subtask not found: {task_number}. Error: {e}")
            return None