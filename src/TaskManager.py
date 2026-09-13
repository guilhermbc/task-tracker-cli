import json
import os
from Task import Task

class TaskManager:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks: list[Task] = []
        self.load_tasks()

    def load_tasks(self):
        """Read the data from tasks.json and convert it to Task objects"""
        if not os.path.exists(self.file_path):
            self.tasks = []
            return
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for item in data:
                    self.tasks.append(Task.from_dict(item))

        except (json.JSONDecodeError, KeyError):
            self.tasks = []

    def save_tasks(self):
        """Saves the tasks on the tasks.json file"""
        data = []

        with open(self.file_path, 'w', encoding='utf-8') as file:
            for task in self.tasks:
                data.append(task.to_dict())
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_task(self, description: str):
        new_id = max([task.id for task in self.tasks], default=0) + 1
        self.tasks.append(Task(id=new_id, description=description))

    def get_task(self, task_id: int) -> Task | None:
            for task in self.tasks:
                if task.id == task_id:
                    return task
            return None

    def update_task_description(self, task_id: int, description: str):
        task = self.get_task(task_id)
        if task:
            task.update_description(description)
        else:
            print("Task does not exist.")

    def update_task_status(self, task_id: int, new_status: str):
        task = self.get_task(task_id)
        if task:
            if new_status == 'todo':
                task.mark_todo()
            elif new_status == 'in-progress':
                task.mark_in_progress()
            else:
                task.mark_done()
        else:
            print("Task does not exist.")

    def delete_task(self, task_id: int):
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(index)
                return
        print("Task does not exist.")

    def list_tasks(self, status_filter: str | None = None):
        """Lists all task or filters by the specified status"""
        filtered_tasks = self.tasks

        if status_filter:
            filtered_tasks = []
            for task in self.tasks:
                if task.status == status_filter:
                    filtered_tasks.append(task)

        if not filtered_tasks:
            print("No tasks found.")
            return

        # Formatted print
        print(f"\n{'ID':<4} {'Status':<15} {'Description':<35}")
        print("-" * 55)
        for task in filtered_tasks:
            print(f"{task.id:<4} {task.status:<15} {task.description}")
        print()
