import datetime

FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                title, priority, due_date, status = line.strip().split("|")
                tasks.append({
                    "title": title,
                    "priority": priority,
                    "due_date": due_date,
                    "status": status
                })
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task['title']}|{task['priority']}|{task['due_date']}|{task['status']}\n")

def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Priority (High/Medium/Low): ")
    due_date = input("Due date (YYYY-MM-DD): ")

    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"\nTask {index}")
        print(f"Title    : {task['title']}")
        print(f"Priority : {task['priority']}")
        print(f"Due Date : {task['due_date']}")
        print(f"Status   : {task['status']}")

def mark_completed(tasks):
    view_tasks(tasks)
    choice = int(input("\nEnter task number to mark completed: "))
    if 1 <= choice <= len(tasks):
        tasks[choice - 1]["status"] = "Completed"
        save_tasks(tasks)
        print("✅ Task marked as completed!")
    else:
        print("❌ Invalid choice")

def delete_task(tasks):
    view_tasks(tasks)
    choice = int(input("\nEnter task number to delete: "))
    if 1 <= choice <= len(tasks):
        tasks.pop(choice - 1)
        save_tasks(tasks)
        print("🗑️ Task deleted!")
    else:
        print("❌ Invalid choice")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== TASK MANAGEMENT SYSTEM =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

main()