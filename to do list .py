import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(tk.END, f"✓ {task}")
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Task entry
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

add_btn = tk.Button(button_frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT, padx=5)

done_btn = tk.Button(button_frame, text="Mark Done", command=mark_done)
done_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_btn.pack(side=tk.LEFT, padx=5)

# Task list
task_listbox = tk.Listbox(root, font=("Arial", 14), height=15, selectbackground="lightblue")
task_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# start loop
root.mainloop()