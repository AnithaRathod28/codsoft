import json
import os
FILE_PATH = 'tasks.json'
def load_tasks():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []
def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks):
        status = '✔' if task['completed'] else '✘'
        print(f"{idx + 1}. [{status}] {task['title']}: {task['description']} (Due: {task['due_date']})")
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({'title': title, 'description': description, 'due_date': due_date, 'completed': False})
    print("Task added.")
def update_task(tasks):
    list_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to update: ")) - 1
        if 0 <= task_index < len(tasks):
            task = tasks[task_index]
            task['title'] = input(f"Enter new title (current: {task['title']}): ") or task['title']
            task['description'] = input(f"Enter new description (current: {task['description']}): ") or task['description']
            task['due_date'] = input(f"Enter new due date (current: {task['due_date']}): ") or task['due_date']
            task['completed'] = input(f"Mark as completed? (yes/no): ").strip().lower() == 'yes'
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")
def delete_task(tasks):
    list_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. List tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
