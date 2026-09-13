#!/usr/bin/env python3
import sys
from TaskManager import TaskManager

def print_help():
    """Prints the CLI use instructions"""
    print("\n\033[1mTask Tracker CLI - How to use\033[0m")
    print("-" * 50)
    print("task-cli help                             Shows this 'How to use' section")
    print("task-cli add \"<description>\"              Adds a new task")
    print("task-cli update <id> \"<description>\"      Updates a task description")
    print("task-cli delete <id>                      Deletes a task")
    print("task-cli mark-todo <id>                   Marks a task as 'todo'")
    print("task-cli mark-in-progress <id>            Marks a task as 'in-progress'")
    print("task-cli mark-done <id>                   Marks a task as 'done'")
    print("task-cli list [status]                    Lists tasks (optional: done, todo, in-progress)\n")

def main():
    args = sys.argv[1:]

    if not args or args[0] in ('-h', '--help', 'help'):
        print_help()
        return

    manager = TaskManager()

    try:
        match args:
            # Captures: task-cli help
            case ['help']:
                print_help()

            # Captures: task-cli add \"<descrição>\"
            case ['add', description] if description.strip():
                manager.add_task(description)

            case ['add']:
                print('\033[31mError: Missing description.')

            # Captures: task-cli update <id> \"<descrição>\"
            case ['update', id, new_description] if new_description.strip():
                manager.update_task_description(int(id), new_description)

            case ['update']:
                print('\033[31mError: Missing parameter(s) (id and/or description).')

            # Captures: task-cli delete <id>
            case ['delete', id]:
                manager.delete_task(int(id))
            
            # Captures: task-cli mark-todo <id>
            case ['mark-todo', id]:
                manager.update_task_status(int(id), 'todo')

            # Captures: task-cli mark-in-progress <id>
            case ['mark-in-progress', id]:
                manager.update_task_status(int(id), 'in-progress')

            # Captures: task-cli mark-done <id>
            case ['mark-done', id]:
                manager.update_task_status(int(id), 'done')

            # Captures: task-cli list [status]
            case ['list', status]:
                manager.list_tasks(status)

            case ['list']:
                manager.list_tasks()

            # Default case: uknkown command
            case [command, *_]:
                print(f"\033[31mCommand '{command}' is unknown.\033[0m")
                print_help()

    except ValueError:
        print('\033[31mErro: Task id must be invalid.\033[0m')

    manager.save_tasks()

if __name__ == '__main__':
    main() 