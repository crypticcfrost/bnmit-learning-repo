import time
import os
import tkinter as tk
from tkinter import ttk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dark Task Manager")
        self.root.geometry("500x400")
        self.root.configure(bg="#1E1E1E")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", background="#1E1E1E", foreground="white", font=("Segoe UI", 12))
        self.style.configure("TButton", background="#3C3F41", foreground="white", font=("Segoe UI", 11), padding=6)
        self.style.configure("TEntry", fieldbackground="#3C3F41", foreground="white")
        self.style.configure("Treeview", background="#3C3F41", foreground="white", fieldbackground="#3C3F41")
        self.style.map("TButton", background=[("active", "#5A5D5F")])

        self.create_widgets()

    def create_widgets(self):
        self.task_entry = ttk.Entry(self.root, width=40, font=("Segoe UI", 11))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.add_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.tree = ttk.Treeview(self.root, columns=("#1"), show="headings")
        self.tree.heading("#1", text="Tasks")
        self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.delete_button = ttk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.clear_button = ttk.Button(self.root, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def add_task(self):
        task = self.task_entry.get()
        if task.strip():
            self.tree.insert("", "end", values=(task,))
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)

    def clear_tasks(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
