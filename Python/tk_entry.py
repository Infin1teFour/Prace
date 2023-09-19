import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("400x100")

text = tk.StringVar()

def update():
    Label.config(text=text.get())

textinput = tk.Entry(textvariable=text)
button = tk.Button(text="Enter", command=update)
Label = tk.Label(text="")

textinput.grid(column=0, row=0)
button.grid(column=1, row=0)
Label.grid(column=0, row=1)

tk.mainloop()