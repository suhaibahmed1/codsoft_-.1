import tkinter as tk
from tkinter import simpledialog

tasks = []

def addTask():
    task = simpledialog.askstring("Input", "Enter the name of your task:")
    if task:
        tasks.append(task)
        updateTaskList()

def listTasks():
    if not tasks:
        result.set("No Tasks in the List currently")
    else:
        result.set("\n".join(f"{i+1}. {task}" for i, task in enumerate(tasks)))

def deleteTask():
    listTasks()
    try:
        index = simpledialog.askinteger("Input", "Enter the number of the Task you want to Delete:")
        if index is not None and 0 <= index - 1 < len(tasks):
            tasks.pop(index - 1)
            updateTaskList()
        else:
            result.set(f"Task #{index} was not found")
    except ValueError:
        result.set("Invalid Input")

def updateTaskList():
    listTasksLabel.config(text=result.get())

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List Application")
    root.geometry("400x400")  # Set the initial size of the window

    # Add a custom background color
    root.configure(bg="#008080")

    result = tk.StringVar()

    welcome_label = tk.Label(root, text="Welcome to To-Do List Application", font=("Helvetica", 16), bg="#FFFFF0", fg="black")
    welcome_label.pack(pady=10)

    listTasksLabel = tk.Label(root, textvariable=result, font=("Helvetica", 12), bg="#4682B4")
    listTasksLabel.pack(pady=10)

    add_button = tk.Button(root, text="Add a task", command=addTask, font=("Helvetica", 12), bg="#4682B4", fg="white")
    add_button.pack(pady=5)

    delete_button = tk.Button(root, text="Delete task", command=deleteTask, font=("Helvetica", 12), bg="#4682B4", fg="white")
    delete_button.pack(pady=5)

    list_button = tk.Button(root, text="List tasks", command=listTasks, font=("Helvetica", 12), bg="#4682B4", fg="white")
    list_button.pack(pady=5)

    quit_button = tk.Button(root, text="Quit", command=root.destroy, font=("Helvetica", 12), bg="#4682B4", fg="white")
    quit_button.pack(pady=10)

    root.mainloop()

