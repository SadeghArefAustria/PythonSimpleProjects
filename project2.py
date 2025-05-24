"""
Skills: Lists, file handling, functions, menus.

Description: Create a text-based app where users can:

Add tasks
View tasks
Mark tasks as completed
Save/load tasks from a file
Bonus: Use dictionaries to add due dates or priority.

"""
import json
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks):
    task = input("Enter the task description: ")
    due_date = input("Enter the due date (optional): ")
    priority = input("Enter the priority (optional): ")
    
    task_dict = {
        "description": task,
        "completed": False,
        "due_date": due_date if due_date else None,
        "priority": priority if priority else None
    }
    
    tasks.append(task_dict)
    print("Task added successfully!")
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    
    for index, task in enumerate(tasks):
        status = "✔️" if task["completed"] else "❌"
        due_date = f" (Due: {task['due_date']})" if task['due_date'] else ""
        priority = f" [Priority: {task['priority']}]" if task['priority'] else ""
        print(f"{index + 1}. {status} {task['description']}{due_date}{priority}")   
def mark_task_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def main():
    filename = "tasks.json"
    tasks = load_tasks(filename)
    
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Save and Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            save_tasks(filename, tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid option, please try again.")
if __name__ == "__main__":
    main()
# This code implements a simple task manager that allows users to add, view, and mark tasks as completed.
# It also supports saving and loading tasks from a JSON file, and includes optional due dates and priorities for each task.
# The task manager is text-based and provides a menu for user interaction.
# The code uses functions to organize the logic, making it modular and easy to maintain.    
# The tasks are stored in a list of dictionaries, where each dictionary represents a task with its description, completion status, due date, and priority.
# The program handles file operations safely, ensuring that it can recover from missing or corrupted task files.
# The user interface is simple and intuitive, guiding the user through the available options.
# The code is structured to be easily extendable, allowing for future enhancements such as task editing or deletion.
# The use of JSON for task storage allows for easy readability and portability of the task data.
# The program is designed to be user-friendly, providing clear prompts and feedback for each action.0
    