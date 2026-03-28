from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n==== Task Manager ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            manager.add_task(task)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.view_tasks()
            index = int(input("Enter task number to delete: "))
            manager.delete_task(index)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
