import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List Application')

        # Listbox to display tasks
        self.tasks = []
        self.listbox_tasks = tk.Listbox(root, height=15, width=50, selectmode=tk.SINGLE)
        self.listbox_tasks.pack(pady=10)

        # Entry widget to add tasks
        self.entry_task = tk.Entry(root, width=52)
        self.entry_task.pack()

        # Frame for buttons
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)

        # Buttons
        self.button_add_task = tk.Button(frame_buttons, text="Add Task", command=self.add_task)
        self.button_add_task.grid(row=0, column=0, padx=5)

        self.button_delete_task = tk.Button(frame_buttons, text="Delete Task", command=self.delete_task)
        self.button_delete_task.grid(row=0, column=1, padx=5)

        self.button_mark_completed = tk.Button(frame_buttons, text="Mark Completed", command=self.mark_completed)
        self.button_mark_completed.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append((task, False))  # Append as tuple (task, not completed)
            self.update_task_list()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "The task cannot be empty.")

    def delete_task(self):
        try:
            task_index = self.listbox_tasks.curselection()[0]
            del self.tasks[task_index]
            self.update_task_list()
        except:
            messagebox.showwarning("Warning", "You must select a task.")

    def mark_completed(self):
        try:
            task_index = self.listbox_tasks.curselection()[0]
            task, completed = self.tasks[task_index]
            self.tasks[task_index] = (task, True)
            self.update_task_list()
        except:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task_list(self):
        self.listbox_tasks.delete(0, tk.END)
        for task, completed in self.tasks:
            task_display = task if not completed else f"{task} - Done"
            self.listbox_tasks.insert(tk.END, task_display)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
