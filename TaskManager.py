import json
import os
from .Task import Task

class TaskManager:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks: list[Task] = []
        self.load_tasks()

    def load_tasks(self):
        """Read the data from tasks.json and convert it to Task objects"""
        pass

    def save_tasks(self):
        """Save the tasks on the tasks.json file"""
        pass

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def list_done_tasks(self):
        pass

    def list_in_progress_tasks(self):
        pass

    def list_not_done_tasks(self):
        pass