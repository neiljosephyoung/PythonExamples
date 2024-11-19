
to_do_list = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        to_do_list.append(task)
        print("Task added!")
    elif choice == "2":
        print("To-Do List:")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        task_number = int(input("Enter task number to remove: "))
        if 0 < task_number <= len(to_do_list):
            removed_task = to_do_list.pop(task_number - 1)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid task number!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
