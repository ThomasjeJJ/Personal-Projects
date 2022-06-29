import turtle
from random import randint
import time


turtle.bgcolor("black")
turtle.title("Klik Spel")
turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.pencolor("white")
t.penup()
t.shape("circle")

r = turtle.Turtle()
r.speed(0)
r.pencolor("white")
r.penup()
r.shape("circle")
r.hideturtle()

tijds = turtle.Turtle()
bols = turtle.Turtle()

x = 0
y = 0
start = 0


def tijdl(i,j):
    global x, start, tijdlemiet
    if x == 0:
        tijdlemiet = int(turtle.numinput("Aantal seconden", "Geef een getal tussen de 0 en 60:", 1, minval=1, maxval=60))
        tijds.hideturtle()
        bols.hideturtle()
        t.showturtle()
        schrijf.clear()
        start = time.time()
    if x == 1:
        start = time.time()
    if start + tijdlemiet > time.time():
        randomt()
        x = x + 1
        print(x)
    if start + tijdlemiet < time.time():
        t.hideturtle()
        schrijf.color("white")
        schrijf.goto(0,0)
        schrijf.write(f"In {tijdlemiet} seconden heb je {x} bolletjes aangeklikt!", font=("Verdana", 15, "normal", ), align="center")
        a = x / tijdlemiet
        b = round(a, 3)
        schrijf.goto(0, -25)
        schrijf.write(f"Je hebt {b} bolletjes per seconden aangeklikt.", font=("Verdana", 15, "normal", ), align="center")
        startbollen()
        x = 0

def boles(i,j):
    global y, deltastart, aantalbol
    if y == 0:
        aantalbol = int(turtle.numinput("Aantal bolletjes", "Geef een getal tussen de 0 en 60:", 1, minval=1, maxval=60))
        tijds.hideturtle()
        bols.hideturtle()
        r.showturtle()
        schrijf.clear()
    if y == 1:
        deltastart = time.time()
    if y <= aantalbol:
        y = y + 1
        randomr()
    if y > aantalbol:
        deltaeind = time.time()
        deltatijd = deltaeind - deltastart
        r.hideturtle()
        schrijf.color("white")
        z = round(deltatijd, 3)
        schrijf.goto(0,0)
        schrijf.write(f"Je hebt {aantalbol} bolletjes in {z} seconden aangeklikt!", font=("Verdana", 15, "normal", ), align="center")
        a = y / deltatijd
        b = round(a, 3)
        schrijf.goto(0, -25)
        schrijf.write(f"Je hebt {b} bolletjes per seconden aangeklikt", font=("Verdana", 15, "normal", ), align="center")
        startbollen()
        y = 0
        



def randomt():
    R = randint(0,255)
    G = randint(0,255)
    B = randint(0,255)
    t.color(R,G,B)
    t.turtlesize(randint(1,4))
    t.goto(randint(-200,200), randint(-200,200))# geeft x en y coordinaten

def randomr():
    R = randint(0,255)
    G = randint(0,255)
    B = randint(0,255)
    r.color(R,G,B)
    r.turtlesize(randint(1,4))
    r.goto(randint(-200,200), randint(-200,200))# geeft x en y coordinaten

def starttext ():
    global schrijf
    schrijf = turtle.Turtle()
    schrijf.speed(0)
    schrijf.hideturtle()
    schrijf.penup()
    
    schrijf.goto(0, -10)
    schrijf.pencolor("blue")
    schrijf.fillcolor("blue")
    schrijf.write("Je hebt x tijd om zo veel mogelijk bolletjes aan te klikken", font=("Verdana", 15, "normal", ), align="center")

    schrijf.goto(0, -50)
    schrijf.pencolor("red")
    schrijf.fillcolor("red")
    schrijf.write("je moet x aantal bolletjes zo snel mogelijk aanklikken", font=("Verdana", 15, "normal", ), align="center")

def startbollen():
    global tijds, bols
    tijds.showturtle()
    tijds.speed(0)
    tijds.pencolor("blue")
    tijds.fillcolor("blue")
    tijds.penup()
    tijds.goto(-150,80)
    tijds.shape("circle")
    tijds.turtlesize(5)
    tijds.onclick(tijdl)

    bols.showturtle()
    bols.speed(0)
    bols.pencolor("red")
    bols.fillcolor("red")
    bols.penup()
    bols.goto(150,80)
    bols.shape("circle")
    bols.turtlesize(5)
    bols.onclick(boles)

t.onclick(tijdl)
t.hideturtle()
r.onclick(boles)
r.hideturtle()

tijds.onclick(tijdl)
bols.onclick(boles)

starttext()
startbollen()

turtle.done()