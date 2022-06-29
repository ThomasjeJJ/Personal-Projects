import turtle
from random import randint
#de benodigde libraries importeren

t = turtle.Turtle()
turtle.bgcolor("black")# de achtergrond heb ik zwart gemaakt omdat ik dat mooier vond
t.speed(0)
turtle.title("Random Circles")# het venster een passende naam geven
turtle.colormode(255)
t.hideturtle()# zodat er geen pijltje staat


for i in range(50):
    R = randint(0,255)
    G = randint(0,255)
    B = randint(0,255)
    t.goto(randint(-200,200), randint(-200,200))# geeft x en y coordinaten
    t.pendown()
    t.pencolor(R,G,B)# om de kleur random te bepalen
    t.circle(randint(5,100))
    t.penup()

turtle.done() # zorgt ervoor dat het programma goed afsluit