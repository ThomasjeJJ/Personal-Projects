import turtle
from random import randint
#de benodigde libraries importeren

t = turtle.Turtle()
turtle.bgcolor("black") # de achtergrond heb ik zwart gemaakt omdat ik dat mooier vond
t.speed(0) # zorgt ervoor dat de turtel niet ellendig lang duurt
turtle.title("Ster") # het venster een passende naam geven
turtle.colormode(255)
t.hideturtle()# zodat er geen pijltje staat



for i in range(250):
    R = randint(0,255)
    G = randint(0,255)
    B = randint(0,255)
    t.pencolor(R,G,B) # om de kleur random te bepalen
    t.goto(randint(-200,200), randint(-200,200))# geeft random x en y coordinaten
    t.goto(0,0)# zorgt ervoor dat er constant vanaf 0,0 word begonnen

turtle.done() # zorgt ervoor dat het programma goed afsluit
