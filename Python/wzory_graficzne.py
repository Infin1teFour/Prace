import tkinter as tk
from tkinter import ttk
import math

root = tk.Tk()
root.resizable(False,False)
root.title("Kalkulator wzorów")

font = ("Comic Sans MS",10)

#prostokąt
prostokat_a = tk.StringVar()
prostokat_b = tk.StringVar()

def prostokat_calc():
    try:
        x = int(prostokat_a.get())
        y = int(prostokat_b.get())
    except:
        prostokat_result.config(text="Nieprawidłowe liczby")
    prostokat_result.config(text=((2*x) + (2*y)))

prostokat_info = tk.Label(text="Obwód prostokąta",font=font).grid(column=0, row=0, columnspan=2)

prostokat_ainfo = tk.Label(text="a: ",font=font).grid(column=0, row=1)
prostokat_afield = tk.Entry(textvariable=prostokat_a).grid(column=1, row=1)

prostokat_binfo = tk.Label(text="b: ",font=font).grid(column=0, row=2)
prostokat_bfield = tk.Entry(textvariable=prostokat_b).grid(column=1, row=2)

prostokat_button = tk.Button(text="Oblicz", command=prostokat_calc,font=font).grid(column=0, row=3)
prostokat_result = tk.Label(text="",font=font)
prostokat_result.grid(column=1, row=3)


#Objętość sześcianu
objszescian_a = tk.StringVar()

def objszescian_calc():
    try:
        x = int(objszescian_a.get())
    except:
        objszescian_result.config(text="Nieprawidłowe liczby")
    objszescian_result.config(text=(x**3))

objszescian_info = tk.Label(text="Objętość sześcianu",font=font).grid(column=2, row=0, columnspan=2)

objszescian_ainfo = tk.Label(text="a: ",font=font).grid(column=2, row=1, rowspan=2)
objszescian_afield = tk.Entry(textvariable=objszescian_a).grid(column=3, row=1, rowspan=2)

objszescian_button = tk.Button(text="Oblicz", command=objszescian_calc,font=font).grid(column=2, row=3)
objszescian_result = tk.Label(text="",font=font)
objszescian_result.grid(column=3, row=3)


#Pole koła
kolo_r = tk.StringVar()

def kolo_calc():
    try:
        x = float(kolo_r.get())
    except:
        kolo_result.config(text="Nieprawidłowe liczby")
    kolo_result.config(text=(math.pi*(x**2)))

kolo_info = tk.Label(text="Pole Koła",font=font).grid(column=0, row=4, columnspan=2)

kolo_rinfo = tk.Label(text="r: ",font=font).grid(column=0, row=5, rowspan=2)
kolo_rfield = tk.Entry(textvariable=kolo_r).grid(column=1, row=5, rowspan=2)

kolo_button = tk.Button(text="Oblicz", command=kolo_calc,font=font).grid(column=0, row=7)
kolo_result = tk.Label(text="",font=font)
kolo_result.grid(column=1, row=7)

#Objętość ostrosłupa
objost_h = tk.StringVar()
objost_pp = tk.StringVar()

def objost_calc():
    try:
        x = int(objost_pp.get())
        y = int(objost_h.get())
    except:
        objost_result.config(text="Nieprawidłowe liczby")
    objost_result.config(text=((x/3)*y))

objost_info = tk.Label(text="Objętość ostrosłupa",font=font).grid(column=2, row=4, columnspan=2)

objost_ppinfo = tk.Label(text="Pp: ",font=font).grid(column=2, row=5)
objost_ppfield = tk.Entry(textvariable=objost_pp).grid(column=3, row=5)

objost_hinfo = tk.Label(text="H: ",font=font).grid(column=2, row=6)
objost_hfield = tk.Entry(textvariable=objost_h).grid(column=3, row=6)

objost_button = tk.Button(text="Oblicz", command=objost_calc,font=font).grid(column=2, row=7)
objost_result = tk.Label(text="",font=font)
objost_result.grid(column=3, row=7)


#Objętość walca
objwal_h = tk.StringVar()
objwal_r = tk.StringVar()
def objwal_calc():
    try:
        x = float(objwal_r.get())
        y = float(objwal_h.get())
    except:
        objwal_result.config(text="Nieprawidłowe liczby")
    objwal_result.config(text=((math.pi*(x**2))*y))

objwal_info = tk.Label(text="Objętość walca",font=font).grid(column=4, row=0, columnspan=2)

objwal_rinfo = tk.Label(text="Pp: ",font=font).grid(column=4, row=1)
objwal_rfield = tk.Entry(textvariable=objwal_r).grid(column=5, row=1)

objwal_hinfo = tk.Label(text="H: ",font=font).grid(column=4, row=2)
objwal_hfield = tk.Entry(textvariable=objwal_h).grid(column=5, row=2)

objwal_button = tk.Button(text="Oblicz", command=objwal_calc,font=font).grid(column=4, row=3)
objwal_result = tk.Label(text="",font=font)
objwal_result.grid(column=5, row=3)

tk.mainloop()