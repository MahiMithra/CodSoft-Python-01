def display_tasks(tasks):
    if not tasks:
        print("No tasks to show!")
    else:
        print("Tasks:")
        for index, (task, completed) in enumerate(tasks, start=1):
            status = "Done" if completed else "Pending"
            print(f"{index}. {task} [{status}]")

def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append((task, False))
    print("Task added.")

def remove_task(tasks):
    display_tasks(tasks)
    if tasks:
        task_number = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks.pop(task_number)
            print("Task removed.")
        else:
            print("Invalid task number!")

def mark_task_completed(tasks):
    display_tasks(tasks)
    if tasks:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            task, _ = tasks[task_number]
            tasks[task_number] = (task, True)
            print("Task marked as completed.")
        else:
            print("Invalid task number!")

def main():
    tasks = []
    
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_task_completed(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
