import tkinter as tk
from tkinter import messagebox, Label

class CBA:
    def __init__(self, root):
        self.rt = root
        self.rt.title("Contact Book")
        self.cons = []
        self.name_label=tk.Label(root,text="NAME")
        self.name_label.grid(row=0,column=1,padx=5,pady=5,sticky="we")
        self.name_e=tk.Entry(root)
        self.name_e.grid(row=0,column=1,padx=5,pady=5,sticky="we")
        self.ph_label=tk.Label(root,text="Phone:")
        self.ph_label.grid(row=1,column=0,padx=5,pady=5,sticky="we")
        self.ph_e=tk.Entry(root)
        self.ph_e.grid(row=1,column=1,padx=5,pady=5)
        self.mail_l=tk.Label(root,text="Email:")
        self.mail_l.grid(row=2,column=0,padx=5,pady=5,sticky="we")
        self.mail_e=tk.Entry(root)
        self.mail_e.grid(row=2,column=1,padx=5,pady=5)
        self.addr_l=tk.Label(root,text="Address:")
        self.addr_l.grid(row=3,column=0,padx=5,pady=5)
        self.addr_e=tk.Entry(root)
        self.addr_e.grid(row=3,column=1,padx=5,pady=5)
        self.add_b=tk.Button(root,text="Add contact",command=self.add_con)
        self.add_b.grid(row=4,column=0,columnspan=2,padx=5,pady=5,sticky="we")
        self.view_button=tk.Button(root,text="View contacts",command=self.view_con)
        self.view_button.grid(row=5,column=0,columnspan=2,padx=5,pady=5,sticky="we")

    def add_con(self):
        name = self.name_e.get()
        phone = self.ph_e.get()
        email = self.mail_e.get()
        address = self.addr_e.get()

        if name and phone:
            contact_info = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.cons.append(contact_info)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entities()
        else:
            messagebox.showerror("Error!", "Name and phone number are required in the empty fields")

    def view_con(self):
        if len(self.cons) > 0:
            con_l = "\n".join([f"Name:{contact['Name']},Phone:{contact['Phone']}" for contact in self.cons])
            messagebox.showinfo("Contacts", con_l)
        else:
            messagebox.showinfo("Contacts", "No contacts found")

    def clear_entities(self):
        self.name_e.delete(0, tk.END)
        self.ph_e.delete(0, tk.END)
        self.mail_e.delete(0, tk.END)
        self.addr_e.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    a = CBA(root)
    root.mainloop()