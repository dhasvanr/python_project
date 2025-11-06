import json
import os
import sys

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"✅ Added task: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

def complete_task(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"🎯 Completed task: {tasks[index - 1]['title']}")
    except IndexError:
        print("❌ Invalid task number.")

def show_help():
    print("""
Usage:
  python taskmaster.py add "<task>"
  python taskmaster.py list
  python taskmaster.py done <task_number>
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "done":
        complete_task(int(sys.argv[2]))
    else:
        show_help()
