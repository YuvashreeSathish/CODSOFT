import tkinter as tk 

def on_click(button_text): 
    current_text = entry_var.get() 
    
    if button_text == "=": 
        try:
            result = eval(current_text) 
            entry_var.set(result)
        except Exxeption as e:
            entry_var.set("Error")
    elif button_text == "C": 
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)


root = tk.Tk()
root.title("Calculator")


entry_var = tk.StringVar() 
entry = tk.Entry(root, textvariable=entry_var,justify="right",font=("Helvetica",18)) 
entry.grid(row=0, column=0, columnspan=4, sticky="nsew") 


buttons = [ 
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=",  4, 2), ("+", 4, 3),
    ("C", 5, 0)
]


for (button_text, row, col) in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 14),
                       command=lambda bt=button_text: on_click(bt)) 
    button.grid(row=row,column=col, sticky="nsew") 


for i in range(6): 
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
