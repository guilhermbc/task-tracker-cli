# 📝 Task Tracker CLI

A simple and efficient Command-Line Interface (CLI) application for daily task management, built with Python using zero third-party dependencies.

This project was built following the [Task Tracker](https://roadmap.sh/projects/task-tracker) project specifications from **roadmap.sh**.

---

## 🚀 About the Project

**Task Tracker CLI** allows you to add, update, delete, and track the status of your tasks directly from your terminal. Data is automatically persisted in a local JSON file (`tasks.json`).

### Key Features

* **Zero External Dependencies:** Built using strictly standard Python libraries (`sys`, `json`, `os`, `datetime`).
* **Object-Oriented Programming (OOP):** Well-structured architecture separating the data model (`Task`), business logic (`TaskManager`), and CLI dispatcher (`main.py`).
* **Clean Terminal Output:** Formatted task list and styled error messages using ANSI escape codes.
* **Local Persistence:** Automatic reading and writing with ISO timestamps for creation (`createdAt`) and updates (`updatedAt`).

---

## 🛠️ Prerequisites

* **Python 3.10** or higher (required for `match/case` syntax support).
* Linux, macOS, or WSL (Windows Subsystem for Linux) environment.

---

## 📦 Local Installation & Running

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. **Run directly with Python:**

   ```bash
   python3 main.py help
   ```

---

## ⚙️ Turning it into a Global Command (task-cli)

To run `task-cli` from anywhere in your terminal without typing `python3 main.py`, follow these steps:

1. **Make the main file executable:**

   ```bash
   chmod +x main.py
   ```

2. **Create a symbolic link in your system's binary directory:**

   ```bash
   sudo ln -sf "$(pwd)/main.py" /usr/local/bin/task-cli
   ```

3. **Done! You can now invoke the app globally using `task-cli`:**

   ```bash
   task-cli help
   ```

---

## 📖 Usage Guide & Commands

1. **Add a new task:**

   ```bash
   task-cli add "Buy milk and eggs"
   ```

2. **List tasks:**

   * List all tasks:

     ```bash
     task-cli list
     ```

   * Filter by status (optional):

     ```bash
     task-cli list todo
     task-cli list in-progress
     task-cli list done
     ```

3. **Update task description:**

   ```bash
   task-cli update 1 "Buy milk, eggs, and bread"
   ```

4. **Change task status:**

   * Mark as "To do":

     ```bash
     task-cli mark-todo 1
     ```

   * Mark as "In progress":

     ```bash
     task-cli mark-in-progress 1
     ```

   * Mark as "Done":

     ```bash
     task-cli mark-done 1
     ```

5. **Delete a task:**

   ```bash
   task-cli delete 1
   ```

---

## ⚙️ 🗂️ Data Storage (`tasks.json`)

Tasks are stored in the project directory using the following JSON format:

```json
{
  "id": 1,
  "description": "Buy milk",
  "status": "in-progress",
  "createdAt": "2026-09-14T10:00:00"
}
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
