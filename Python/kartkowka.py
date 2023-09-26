import tkinter as tk

from tkinter import ttk


root = tk.Tk()
root.resizable(False,False)
root.title("Kartkówka")


Tytuł = tk.Label(text="Kartkówka",font=("Times New Roman",20)).grid(column=0, row=0, columnspan=2)
text_input = [tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()]


#Zadanie 1


zad1_title = tk.Label(text="Zadanie 1 ",font=("Times New Roman",15)).grid(column=0, row=1)
zad1_content = tk.Label(text="Placeholder ",font=("Times New Roman",10)).grid(column=0, row=2)
zad1_input = tk.Entry(textvariable=text_input[0]).grid(column=0, row=3)
zad1_correct = tk.Label(text="",font=("Times New Roman",10))
zad1_correct.grid(column=1, row=3)

#Zadanie 2


zad2_title = tk.Label(text="Zadanie 2 ",font=("Times New Roman",15)).grid(column=0, row=4)
zad2_content = tk.Label(text="Placeholder ",font=("Times New Roman",10)).grid(column=0, row=5)
zad2_input = tk.Entry(textvariable=text_input[1]).grid(column=0, row=6)
zad2_correct = tk.Label(text="",font=("Times New Roman",10))
zad2_correct.grid(column=1, row=6)

#Zadanie 3


zad3_title = tk.Label(text="Zadanie 3 ",font=("Times New Roman",15)).grid(column=0, row=7)
zad3_content = tk.Label(text="Placeholder ",font=("Times New Roman",10)).grid(column=0, row=8)
zad3_input = tk.Entry(textvariable=text_input[2]).grid(column=0, row=9)
zad3_correct = tk.Label(text="",font=("Times New Roman",10))
zad3_correct.grid(column=1, row=9)

#Zadanie 4


zad4_title = tk.Label(text="Zadanie 4 ",font=("Times New Roman",15)).grid(column=0, row=10)
zad4_content = tk.Label(text="Placeholder ",font=("Times New Roman",10)).grid(column=0, row=11)
zad4_input = tk.Entry(textvariable=text_input[3]).grid(column=0, row=12)
zad4_correct = tk.Label(text="",font=("Times New Roman",10))
zad4_correct.grid(column=1, row=12)

#Zadanie 5


zad5_title = tk.Label(text="Zadanie 5 ",font=("Times New Roman",15)).grid(column=0, row=13)
zad5_content = tk.Label(text="Placeholder ",font=("Times New Roman",10)).grid(column=0, row=14)
zad5_input = tk.Entry(textvariable=text_input[4]).grid(column=0, row=15)
zad5_correct = tk.Label(text="",font=("Times New Roman",10))
zad5_correct.grid(column=1, row=15)

#Zadanie 6


zad6_title = tk.Label(text="Zadanie 6 ",font=("Times New Roman",15)).grid(column=0, row=16)
zad6_content = tk.Label(text="Placeholder ",font=("Times New Roman",10)).grid(column=0, row=17)
zad6_input = tk.Entry(textvariable=text_input[5]).grid(column=0, row=18)
zad6_correct = tk.Label(text="",font=("Times New Roman",10))
zad6_correct.grid(column=1, row=18)

#Zadanie 7


zad7_title = tk.Label(text="Zadanie 7 ",font=("Times New Roman",15)).grid(column=0, row=19)
zad7_content = tk.Label(text="Placeholder ",font=("Times New Roman",10)).grid(column=0, row=20)
zad7_input = tk.Entry(textvariable=text_input[6]).grid(column=0, row=21)
zad7_correct = tk.Label(text="",font=("Times New Roman",10))
zad7_correct.grid(column=1, row=21)

#Zadanie 8

zad8_title = tk.Label(text="Zadanie 8 ",font=("Times New Roman",15)).grid(column=0, row=22)
zad8_content = tk.Label(text="Placeholder ",font=("Times New Roman",10)).grid(column=0, row=23)
zad8_input = tk.Entry(textvariable=text_input[7]).grid(column=0, row=24)
zad8_correct = tk.Label(text="",font=("Times New Roman",10))
zad8_correct.grid(column=1, row=24)

#Zadanie 9

zad9_title = tk.Label(text="Zadanie 9 ",font=("Times New Roman",15)).grid(column=0, row=25)
zad9_content = tk.Label(text="Placeholder ",font=("Times New Roman",10)).grid(column=0, row=26)
zad9_input = tk.Entry(textvariable=text_input[8]).grid(column=0, row=27)
zad9_correct = tk.Label(text="",font=("Times New Roman",10))
zad9_correct.grid(column=1, row=27)

#Zadanie 10

zad10_title = tk.Label(text="Zadanie 10 ",font=("Times New Roman",15)).grid(column=0, row=28)
zad10_content = tk.Label(text="Placeholder ",font=("Times New Roman",10)).grid(column=0, row=29)
zad10_input = tk.Entry(textvariable=text_input[9]).grid(column=0, row=30)
zad10_correct = tk.Label(text="",font=("Times New Roman",10))
zad10_correct.grid(column=1, row=30)

#Sprawdź

odpowiedzi = ["1","2","3","4","5","6","7","8","9","10"]
zadania = {
    0: zad1_correct,
    1: zad2_correct,
    2: zad3_correct,
    3: zad4_correct,
    4: zad5_correct,
    5: zad6_correct,
    6: zad7_correct,
    7: zad8_correct,
    8: zad9_correct,
    9: zad10_correct
}

oceny = {
    10: "6",
    9: "5",
    8: "4",
    7: "3",
    6: "2",
    5: "2",
    4: "1",
    3: "1",
    2: "1",
    1: "1",
    0: "1"
}

def check():
    liczba_dobrych = 0
    for i in range(10):
        if odpowiedzi[i] == text_input[i].get():
            zadania[i].config(text="Dobrze")
            liczba_dobrych = liczba_dobrych + 1
        else:
            zadania[i].config(text="Źle")
    print(liczba_dobrych)
    ocena.config(text=("Twoja ocena to: "+oceny[liczba_dobrych]))

check_button = tk.Button(text="Sprawdź",font=("Times New Roman",15), command=check).grid(column=0, row=31)
ocena = tk.Label(text="",font=("Times New Roman",15))
ocena.grid(column=1, row=31)

tk.mainloop()