import tkinter as tk
from tkinter import ttk
import random as r

#Assign ASCII values to all lists
upperlist = []
for i in range(65,90):
    upperlist.append(i)
lowerlist = []
for i in range(97,122):
    lowerlist.append(i)
numberlist = []
for i in range(48,57):
    numberlist.append(i)
speciallist = []
for i in range(33,47):
    speciallist.append(i)
print(upperlist)

#Initialize windows
root = tk.Tk()
root.resizable(False,False)
root.title("Password Generator")

#Declare variables
upper = tk.BooleanVar()
lower = tk.BooleanVar()
number = tk.BooleanVar()
special = tk.BooleanVar()
passlen = tk.StringVar()
password = ""

#Main generate function
def generate():
    global password
    #check if at least 1 checkbox is selected
    if upper.get() == False and lower.get() == False and number.get() == False and special.get() == False:
        password = "Please select at least one checkbox"
        result.config(text=password)
        return

    #check if password length is valid
    try:
        int(passlen.get())
    except:
        password = "Invalid password length"
        result.config(text=password)
        return
    
    #Generation
    while True:
        if len(password) >= int(passlen.get()):
            break
        chartype = r.randint(0,3)
        if chartype == 0 and upper.get() == True:
            password = password + chr(r.choice(upperlist))
        if chartype == 1 and lower.get() == True:
            password = password + chr(r.choice(lowerlist))
        if chartype == 2 and number.get() == True:
            password = password + chr(r.choice(numberlist))
        if chartype == 3 and special.get() == True:
            password = password + chr(r.choice(speciallist))
        print(chartype)
    result.config(text=password)
    password = ""

#Checkboxes
checkupper = tk.Checkbutton(text='Uppercase letters',variable=upper, onvalue=True, offvalue=False).grid(column=0, row=0)
checklower = tk.Checkbutton(text='Lowercase letters',variable=lower, onvalue=True, offvalue=False).grid(column=1, row=0)
checknumber = tk.Checkbutton(text='Numbers',variable=number, onvalue=True, offvalue=False).grid(column=2, row=0)
checkspecial = tk.Checkbutton(text='Special characters',variable=special, onvalue=True, offvalue=False).grid(column=3, row=0)

#password length field
info = tk.Label(text="Provide password length: ").grid(column=0, row=1)
passlenfield = tk.Entry(textvariable=passlen).grid(column=1, row=1)

#result field
result = tk.Label(text="")
result.grid(column=1, row=2)

#generate button
generatebutton = tk.Button(text="Generate", command=generate).grid(column=0, row=2)


tk.mainloop()