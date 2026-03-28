from utils import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        save_tasks(self.tasks)
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index - 1)
            save_tasks(self.tasks)
            print(f"Deleted: {removed}")
        except:
            print("Invalid task number")
