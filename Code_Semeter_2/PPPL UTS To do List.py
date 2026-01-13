from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def remove_task(self, index):
        return self.tasks.pop(index)

    def mark_as_done(self, index):
        self.tasks[index]["done"] = True

    def mark_as_undone(self, index):
        self.tasks[index]["done"] = False

    def __str__(self):
        return "\n".join([f"{i+1}. [{'x' if t['done'] else ' '}] {t['task']}" for i, t in enumerate(self.tasks)])

class AddTaskCommand(Command):
    def __init__(self, todo_list, task):
        self.todo_list = todo_list
        self.task = task

    def execute(self):
        self.todo_list.add_task(self.task)

    def undo(self):
        self.todo_list.remove_task(len(self.todo_list.tasks) - 1)

class RemoveTaskCommand(Command):
    def __init__(self, todo_list, index):
        self.todo_list = todo_list
        self.index = index
        self.removed_task = None

    def execute(self):
        self.removed_task = self.todo_list.remove_task(self.index)

    def undo(self):
        self.todo_list.tasks.insert(self.index, self.removed_task)

class MarkAsDoneCommand(Command):
    def __init__(self, todo_list, index):
        self.todo_list = todo_list
        self.index = index

    def execute(self):
        self.todo_list.mark_as_done(self.index)

    def undo(self):
        self.todo_list.mark_as_undone(self.index)

class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def execute_command(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)
        else:
            print("Tidak ada yang bisa di-undo.")

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.undo_stack.append(command)
        else:
            print("Tidak ada yang bisa di-redo.")

def main():
    todo = TodoList()
    manager = CommandManager()

    while True:
        print("\nTodo List:")
        print(todo if todo.tasks else "Belum ada tugas.")
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Tandai Selesai")
        print("4. Undo")
        print("5. Redo")
        print("6. Keluar")

        choice = input("Pilih opsi: ")

        if choice == "1":
            task = input("Masukkan nama tugas: ")
            manager.execute_command(AddTaskCommand(todo, task))
        elif choice == "2":
            index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
            if 0 <= index < len(todo.tasks):
                manager.execute_command(RemoveTaskCommand(todo, index))
            else:
                print("Indeks tidak valid.")
        elif choice == "3":
            index = int(input("Masukkan nomor tugas yang selesai: ")) - 1
            if 0 <= index < len(todo.tasks):
                manager.execute_command(MarkAsDoneCommand(todo, index))
            else:
                print("Indeks tidak valid.")
        elif choice == "4":
            manager.undo()
        elif choice == "5":
            manager.redo()
        elif choice == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
