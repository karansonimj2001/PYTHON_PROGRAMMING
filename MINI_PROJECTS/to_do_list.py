tasks = []

while True:
    print("\nTODO LIST:")
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} - {'Done' if task['completed'] else 'Pending'}")

    print("\nCOMMANDS:")
    print("1. Add task")
    print("2. Delete task")
    print("3. Mark task as completed")
    print("0. Exit")

    choice = input("Enter your choice (0-3): ")

    if choice == '1':
        title = input("Enter task title: ")
        tasks.append({'title': title, 'completed': False})
        print(f"Task '{title}' added.")
    elif choice == '2':
        index = int(input("Enter task index to delete: "))
        if 1 <= index <= len(tasks):
            deleted_task = tasks.pop(index - 1)
            print(f"Task '{deleted_task['title']}' deleted.")
        else:
            print("Invalid task index.")
    elif choice == '3':
        index = int(input("Enter task index to mark as completed: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")