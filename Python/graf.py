import tkinter as tk

zgoda = 0
niezgoda = 0

window = tk.Tk()
window.geometry("400x400")
window.resizable(False,True)
window.title("Rozmiar Okna Imie I Nazwisko")

def hello(tekst):
    global zgoda
    global niezgoda
    if tekst == "Zgadzam sie":
        zgoda = zgoda + 1
    if tekst == "Nie zgadzam sie":
        niezgoda = niezgoda + 1
    print(tekst)
    print("Ilość zgód: ",zgoda)
    print("Ilość niezgód: ",niezgoda,"\n")


button1 = tk.Button(window, text="Yes", command=lambda:hello('Zgadzam sie')).pack()
button2 = tk.Button(window, text="No", command=lambda:hello('Nie zgadzam sie')).pack()
window.mainloop()