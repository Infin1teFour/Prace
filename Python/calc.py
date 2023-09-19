import tkinter as tk
from tkinter import ttk
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "**": operator.pow,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod
    }

root = tk.Tk()

num1 = tk.StringVar()
num2 = tk.StringVar()

def calculate(symbol):
    x = int(num1.get())
    y = int(num2.get())
    Result.config(text=(x,symbol,y,"=",ops[symbol](x,y)))
    
field1 = tk.Entry(textvariable=num1).grid(column=0, row=0)
Result = tk.Label(text="")
Result.grid(column=1, row=0)
field2 = tk.Entry(textvariable=num2).grid(column=2, row=0)

addition = tk.Button(text="+", command=lambda: calculate("+"),padx=60, pady=20).grid(column=0, row=1)
subtraction = tk.Button(text="-", command=lambda: calculate("-"),padx=60, pady=20).grid(column=1, row=1)
multiplication = tk.Button(text="*",command=lambda: calculate("*"),padx=60, pady=20).grid(column=2, row=1)

power = tk.Button(text="**",command=lambda: calculate("**"),padx=60, pady=20).grid(column=0, row=2)
division = tk.Button(text="/",command=lambda: calculate("/"),padx=60, pady=20).grid(column=1, row=2)
whole_division = tk.Button(text="//",command=lambda: calculate("//"),padx=60, pady=20).grid(column=2, row=2)

modulo = tk.Button(text="%",command=lambda: calculate("%"),padx=60, pady=20).grid(column=1, row=3)
tk.mainloop()