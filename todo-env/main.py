from tasks import Task
from storage import save_tasks, load_tasks

tasks = load_tasks()

def add_task():
    title = input("Enter task title: ")
    task = Task(title)
    tasks.append(task)
    save_tasks(tasks)

def show_tasks():
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def update_task():
    show_tasks()
    idx = int(input("Enter task number to toggle complete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx].completed = not tasks[idx].completed
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def delete_task():
    show_tasks()
    idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        save_tasks(tasks)
    else:
        print("Invalid task number.")

while True:
    print("\n1. Add Task\n2. Show Tasks\n3. Toggle Complete\n4. Delete Task\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        save_tasks(tasks)
        break
    else:
        print("Invalid choice.")
