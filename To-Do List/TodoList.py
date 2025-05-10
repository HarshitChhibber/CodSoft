import datetime
import os

# Lists to store tasks
todo_list = []
completed_tasks = []

# Utility functions

def generate_task_id():
    return len(todo_list) + len(completed_tasks) + 1

def load_tasks_from_files():
    if os.path.exists("todo_list.txt"):
        with open ("todo_list.txt", "r") as file:
            lines = file.readline()[1:]                     # To skip the Header Line
            for line in lines:
                parts = [part.strip() for part in line.strip().split('|')]
                if len(parts) == 4:
                    task = {
                        "Task ID": int (parts [0]),
                        "Task Name": parts [1],
                        "Creation Date": parts [2],
                        "Due Date": parts [3],
                        "Completion Date": None
                    }
                    todo_list.append(task)
    if os.path.exists("completed_tasks.txt"):
        with open ("completed_tasks.txt", "r") as file:
            lines = file.readline()[1:]
            for line in lines:
                parts = [part.strip() for part in line.strip().split('|')]
                if len(parts) == 5:
                    task = {
                        "Task ID": int (parts [0]),
                        "Task Name": parts [1],
                        "Creation Date": parts [2],
                        "Due Date": parts [3],
                        "Completion Date": parts [4]
                    }
                    completed_tasks.append(task)

def write_todo_file():
    with open("todo_list.txt", "w") as file:
        file.write("Task ID | Task Name | Creation Date | Due Date\n")
        for task in sorted(todo_list, key=lambda x: x["Task ID"]):
            file.write(f"{task['Task ID']: <7} | {task['Task Name']: <20} | {task['Creation Date']: <12} | {task['Due Date']: <10}\n")

def write_completed_tasks_file():
    with open("completed_tasks.txt", "w") as file:
        file.write("Task ID | Task Name | Creation Date | Due Date | Completed Date\n")
        for task in sorted(completed_tasks, key=lambda x: x["Task ID"]):
            file.write(f"{task['Task ID']: <7} | {task['Task Name']: <20} | {task['Creation Date']: <12} | {task['Due Date']: <10} | {task['Completed Date']: <14}\n")

def write_all_tasks_file():
    with open("all_tasks.txt", "w", encoding="utf-8") as file:                        # UTF-8 for using Special Characters
        file.write("Task ID | Task Name | Due Date | Status\n")
        all_tasks = todo_list + completed_tasks
        all_tasks_sorted = sorted(all_tasks, key=lambda x: x["Task ID"])
        for task in all_tasks_sorted:
            status = "☑" if task["Completed Date"] else "☐"
            file.write(f"{task['Task ID']: <7} | {task['Task Name']: <20} | {task['Due Date']: <10} | {status}\n")

def check_due_tasks():
    today = datetime.datetime.today().date()
    for task in todo_list:
        try:
            due_date = task['Due Date']
            if len(due_date.split('/')[-1]) == 2:
                due = datetime.datetime.strptime(due_date, "%d/%m/%y").date()
            else:
                due = datetime.datetime.strptime(due_date, "%d/%m/%Y").date()
        except ValueError:
            continue

        days_left = (due - today).days
        if days_left == 0:
            print(f"Reminder: Task '{task['Task Name']}' is due today (Due: {task['Due Date']})")
        elif days_left == 1:
            print(f"Reminder: Task '{task['Task Name']}' is due tomorrow (Due: {task['Due Date']})")

def add_task():
    try:
        n = int(input("How many tasks do you want to add? "))
    except ValueError:
        print("Invalid input.")
        return

    for _ in range(n):
        name = input("Enter the task name: ")
        due_date = input("Enter the due date (dd/mm/yy): ")
        creation_date = datetime.datetime.today().strftime("%d/%m/%Y")
        task = {
            "Task ID": generate_task_id(),
            "Task Name": name,
            "Creation Date": creation_date,
            "Due Date": due_date,
            "Completed Date": None
        }
        todo_list.append(task)
        print(f"Task '{name}' added successfully!")

    write_todo_file()
    write_all_tasks_file()

def mark_task_completed(task_id):
    for task in todo_list:
        if task["Task ID"] == task_id:
            task['Completed Date'] = datetime.datetime.today().strftime("%d/%m/%Y")
            completed_tasks.append(task)
            todo_list.remove(task)
            print(f"Task '{task['Task Name']}' marked as completed!")
            write_todo_file()
            write_completed_tasks_file()
            write_all_tasks_file()
            return
    print("Task ID not found.")

def mark_all_completed():
    confirm = input("Are you sure you want to mark ALL tasks as completed?\n1. Yes\n2. No\nChoose: ")
    if confirm != '1':
        print("Operation cancelled.")
        return
    for task in todo_list[:]:
        task['Completed Date'] = datetime.datetime.today().strftime("%d/%m/%Y")
        completed_tasks.append(task)
        todo_list.remove(task)
    print("All tasks marked as completed!")
    write_todo_file()
    write_completed_tasks_file()
    write_all_tasks_file()

def delete_task(task_id):
    for task in todo_list:
        if task['Task ID'] == task_id:
            todo_list.remove(task)
            print(f"Task '{task['Task Name']}' deleted!")
            write_todo_file()
            write_all_tasks_file()
            return
    print("Task ID not found.")

def view_tasks():
    check_due_tasks()
    if not todo_list:
        print("No tasks to display.")
        return
    print("To-Do Tasks:")
    for task in todo_list:
        print(f"{task['Task ID']}. {task['Task Name']} | Due: {task['Due Date']}")
    while True:
        print("\n1. Mark Task as Completed")
        print("2. Mark All as Completed")
        print("3. Delete Task")
        print("4. Back")
        choice = input("Choose an option: ")
        if choice == '1':
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                mark_task_completed(task_id)
            except ValueError:
                print("Invalid input.")
        elif choice == '2':
            mark_all_completed()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            break
        else:
            print("Invalid option.")

def main():
    load_tasks_from_files()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()