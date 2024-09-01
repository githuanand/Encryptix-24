import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x300")

        self.tasks = self.load_tasks()

        self.task_list = tk.Listbox(self.root, width=40, height=10)
        self.task_list.pack(fill="both", expand=True)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill="x")

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side="left")

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side="left")

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side="left")

        self.complete_button = tk.Button(self.button_frame, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(side="left")

        self.load_task_list()

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as f:
                return json.load(f)
        else:
            return []

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def load_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task['description'])

    def add_task(self):
        task_description = simpledialog.askstring("Add Task", "Enter task description")
        if task_description:
            self.tasks.append({'description': task_description, 'completed': False})
            self.save_tasks()
            self.load_task_list()

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            del self.tasks[selected_task[0]]
            self.save_tasks()
            self.load_task_list()

    def update_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task_description = simpledialog.askstring("Update Task", "Enter new task description")
            if task_description:
                self.tasks[selected_task[0]]['description'] = task_description
                self.save_tasks()
                self.load_task_list()

    def complete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.tasks[selected_task[0]]['completed'] = True
            self.save_tasks()
            self.load_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
