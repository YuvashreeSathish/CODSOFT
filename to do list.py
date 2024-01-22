import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("warning","please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("warning","please select a task to delete.")

def update_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        updated_task = entry.get()
        if updated_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index,updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("warning","please enter an updated task.")
    else:
        messagebox.showwarning("warning","please select a task to update.")


app = tk.Tk()
app.title("To DO LIST")


entry = tk.Entry(app,width=30)
entry.pack(pady=10)


add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)


listbox = tk.Listbox(app,selectmode=tk.SINGLE, width=30, height=10)
listbox.pack(pady=10)


delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)


update_button = tk.Button(app,text="update Task",command=update_task)
update_button.pack(pady=5)


app.mainloop()
