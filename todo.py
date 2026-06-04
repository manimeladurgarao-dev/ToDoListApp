from tkinter import *

# Functions
def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
        save_tasks()

def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
        save_tasks()
    except:
        pass

def clear_tasks():
    task_listbox.delete(0, END)
    save_tasks()

def save_tasks():
    tasks = task_listbox.get(0, END)

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            for task in tasks:
                task_listbox.insert(END, task.strip())
    except FileNotFoundError:
        pass

# GUI Window
root = Tk()
root.title("To-Do List Application")
root.geometry("400x500")

# Heading
title = Label(root, text="To-Do List", font=("Arial", 18, "bold"))
title.pack(pady=10)

# Entry Box
task_entry = Entry(root, width=30, font=("Arial", 12))
task_entry.pack(pady=10)

# Add Button
add_btn = Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

# Listbox
task_listbox = Listbox(root, width=40, height=15)
task_listbox.pack(pady=10)

# Delete Button
delete_btn = Button(root, text="Delete Selected", command=delete_task)
delete_btn.pack(pady=5)

# Clear Button
clear_btn = Button(root, text="Clear All", command=clear_tasks)
clear_btn.pack(pady=5)

# Load Existing Tasks
load_tasks()

root.mainloop()