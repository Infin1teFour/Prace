import tkinter as tk

window = tk.Tk()
window.geometry("300x100")
window.resizable(False,False)
window.title("Jan Jakowicki")

tekst = tk.Label(text="Praca z tkinter",fg="blue").grid(column=0, row=0, sticky='w')

button1 = tk.Button(window, text="Ok", padx=40, pady=30).grid(column=0, row=1, sticky='w')
button2 = tk.Button(window, text="Nic", padx=40, pady=30).grid(column=1, row=1, sticky='w')
button3 = tk.Button(window, text="+", padx=40, pady=30).grid(column=2, row=1, sticky='w')

window.mainloop()