class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} [{status}]"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nYour Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task.title}")
        else:
            print("Invalid task number.")


def main():
    manager = TaskManager()

    while True:
        print("\n--- Mini Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.view_tasks()
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                manager.complete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            manager.view_tasks()
            try:
                task_number = int(input("Enter task number to delete: "))
                manager.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()