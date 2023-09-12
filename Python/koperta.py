import turtle
import math
import random

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

def przekatna(size):
    t.forward(math.sqrt((size**2)*2))
    t.left(135)
    t.forward(size)

def koperta(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

    t.left(45)
    przekatna(size)
    t.left(135)
    przekatna(size)

    t.left(30)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)

for i in range(10):
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.penup()
    t.goto(random.randint(-200,200), random.randint(-150,150))
    t.pendown()
    koperta(random.randint(50,500))
    
turtle.mainloop()