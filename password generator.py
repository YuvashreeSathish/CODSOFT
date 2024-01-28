import tkinter as tk
from tkinter import Entry, Label, Button, IntVar
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation 
    password=''.join(random.choice(characters) for _ in range(length))
    return password 

def generate_and_display_password():
    length = length_var.get()
    password = generate_password(length)
    password_label.config(text=f"Generated  Password: {password}")


root = tk.Tk()
root.title("Password Generator")

length_label = Label(root, text="Enter  password length:")
length_label.pack(pady=10)

length_var = IntVar()
length_entry = Entry(root, textvariable=length_var)
length_entry.pack(pady=10)

generate_button = Button(root, text="Generate password", command=generate_and_display_password)
generate_button.pack(pady=20)

password_label = Label(root, text="")
password_label.pack()

root.mainloop()
