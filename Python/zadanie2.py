#Narysuj Domek za pomocą turtle

import time
import turtle
import math

t = turtle.Turtle()
t.speed(2)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def prostokat(a,b):
    for i in range(2):
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)

while True:
    #Główna figura
    go(-100,-100)
    prostokat(200,200)

    #Dach
    go(-100,100)
    prostokat(200,100)

    #Lewy dach
    t.left(180)
    t.forward(100)
    t.right(135)
    t.forward(math.sqrt(20000))
    t.right(45)

    #Prawy dach
    go(100,100)
    t.forward(100)
    t.left(135)
    t.forward(math.sqrt(20000))
    t.left(45)

    #Okno
    go(-50,10)
    t.left(180)
    prostokat(25,25)
    t.forward(25)
    prostokat(25,25)
    t.left(90)
    t.forward(25)
    t.right(90)
    prostokat(25,25)
    t.back(25)
    prostokat(25,25)

    #Drzwi
    go(40,-100)
    prostokat(40, 70)

    #Klamka
    go(75,-75)
    t.circle(5)

    #Komin
    go(30,200)
    prostokat(35, 50)

    go(150,300)
    t.circle(50)


    time.sleep(10)
    t.clear()
    
