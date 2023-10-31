import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title("Duchy")
root.resizable(False, False)
img = tk.PhotoImage(file="Python\duch.png")

def duchy():
    for i in range(10):
        window = tk.Toplevel(root)
        window.title(f"Duch {i+1}")
        x = random.randint(0, root.winfo_screenwidth() - 200)
        y = random.randint(0, root.winfo_screenheight() - 200)
        window.geometry(f"+{x}+{y}")
        duch = tk.Label(window, image=img).pack()

button = tk.Button(root, text="Sprawdź", width=50, height=10, command=duchy)
button.pack()

tk.mainloop()