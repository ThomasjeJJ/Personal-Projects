import turtle
import time
from random import randint

t = turtle.Turtle()
turtle.bgcolor("black")
turtle.title("Mystieke rozen")
t.speed(0)
t.hideturtle()
t.pencolor("white")
t.penup()
t.goto(0,-300)
t.pendown()
turtle.colormode(255)


coords = []
l = 0
a = 1

while a > 0:
    t.penup()
    t.goto(0,-300)
    t.pendown()
    n = randint(3,25)
    t.pencolor((randint(0,255),randint(0,255),randint(0,255)))
    start = time.time()

    m = 360/n

    for i in range(n):
        t.circle(300,m)
        t.dot()
        coords.append(t.pos())

    for i in range(n):
        for o in range(i + 1):
            t.goto(coords[i])
            t.goto(coords[o])

    coords.clear()
    t.clear()

turtle.done()