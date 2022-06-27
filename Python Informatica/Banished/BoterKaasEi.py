#Thomas Jansen
#thomas@ronmix.com

#Test

import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
turtle.title("Boter, Kaas en Eieren")
t.speed(0)
t.hideturtle()
t.pencolor("white")
t.pensize(5)


t.penup()
t.goto(-150,-150)

t.pendown()
t.goto(150,-150)
t.goto(150,-50)
t.goto(-150,-50)
t.goto(-150,50)
t.goto(150,50)
t.goto(150,150)
t.goto(-150,150)

t.goto(-150,-150)
t.goto(-50,-150)
t.goto(-50,150)
t.goto(50,150)
t.goto(50,-150)
t.goto(150,-150)
t.goto(150,150)
t.penup()

numlist = [(-140, 130),(-40, 130),(60, 130),(-140, 30),(-40, 30),(60, 30),(-140, -70),(-40, -70),(60, -70)]

for nummer in range(1,10):
    t.goto(numlist[nummer-1])
    t.write(nummer, align='center')


t.goto (0, 200)
t.write("We spelen dit spel met 2 spelers. Maak eerst onderling uit wie O is en wie X is.", align='center')
t.goto (0, 180)
t.write("Wie gaat er beginnen O of X?", align='center')

start = turtle.textinput("Wie begint?", "O of X")

if start == "O" or start == "o" or start == "0":
    Speler1 = int(turtle.numinput(" ", "Speler 1 waar wil jij je X neerzetten?", 0, minval=1, maxval=9))

elif start == "X" or start == "x":
    Speler2 = int(turtle.numinput(" ", "Speler 2 waar wil jij je X neerzetten?", 0, minval=1, maxval=9))

else: #probleem het herhaald maar 1 keer en niet oneindig totdat het goed is.
    start = turtle.textinput("Wie begint?", "O of X")

coords = [(-100, 75),(0, 75),(100, 75),(-100, -25),(0, -25),(100, -25),(-100, -125),(0, -125),(100, -125)]

if Speler1 < 10 or Speler1 > 0:
    t.goto(coords[Speler1 - 1])
    t.pendown()
    t.circle(25)
    t.penup()

if Speler2 < 10 or Speler2 > 0:
    t.goto(coords[Speler2 - 1]) # iets van plus 5 zodat het kruis fatsoenlijk gemaakt kan worden
    t.pendown()
    t.circle(25)
    t.penup()

# het input systeem moet nog een beetje gereworked worden want dit werkt niet geweldig

turtle.done()