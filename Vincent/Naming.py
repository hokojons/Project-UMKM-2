class ToDoList:
    def __init__(self):  # Fixed: double underscores
        self.tasks = []

    def add_task(self, task):
        """Add a new task"""
        self.tasks.append(task)
        print(f"Task added: {task}")

    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks yet!")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def remove_task(self, task_number):
        """Remove a task by number"""
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number!")

todo = ToDoList()

while True:
    print("\nOptions: 1. Add Task  2. View Tasks  3. Remove Task  4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        new_task = input("Enter task: ")
        todo.add_task(new_task)
    elif choice == "2":
        todo.view_tasks()
    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        todo.remove_task(num)
    elif choice == "4":
        break
    else:
        print("Invalid choice, try again!")