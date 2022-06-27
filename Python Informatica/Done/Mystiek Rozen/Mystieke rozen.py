#Thomas Jansen
#thomas@ronmix.com

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
t.goto(0,-300) # Zorgt ervoor dat het midden van de cirkel ook in het midden van de het scherm is
t.pendown()
turtle.colormode(255)

t.pencolor((randint(0,255),randint(0,255),randint(0,255))) # Zorgt ervoor dat de roos een random kleur heeft

coords = [] # Maakt de lijst aan
l = 0 # Maakt l aan

n = int(turtle.numinput("Aantal punten", "Geef een getal tussen de 0 en 25:", 1, minval=1, maxval=25))

start = time.time() # Start de tijd zodat die later uitgerekend kan worden

m = 360/n # Rekent uit hoe groot het stuk tussen de punten moet zijn

for i in range(n):
    t.circle(300,m) # Tekent een cirkel van 300 pixels maar m pixels lang
    t.dot() # Zet een punt neer op zijn huidige positie
    coords.append(t.pos()) # Voegt het punt toe aan de lijst

for i in range(n):
    for o in range(i + 1):
        t.goto(coords[i])
        t.goto(coords[o])
        
#print (coords) # gebruikt voor testen

t.penup()

t.goto(-250,-250) # zorgt ervoor dat de tekst op de goede plek staat
end = time.time()
z = round(end - start, 3)
t.write(f"{z} sec", font=("Verdana", 15, "normal", ), align="center")

t.goto(-250,250)
t.write(f"{n} punten", font=("Verdana", 15, "normal", ), align="center")

t.goto(250,250)

for i in range(n):
    l = l + i # rekent het aantal lijnen uit
t.write(f"{l} lijnen", font=("Verdana", 15, "normal", ), align="center")


turtle.done()