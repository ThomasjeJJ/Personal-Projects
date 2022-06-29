import turtle
import random
from random import randint

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
turtle.title("Random Circles")
turtle.colormode(255)
turtle.hideturtle()


for i in range(1000):
    t.goto(randint(-200,200), randint(-200,200))
    t.pencolor((randint(0,255),randint(0,255),randint(0,255)))
    
turtle.done()