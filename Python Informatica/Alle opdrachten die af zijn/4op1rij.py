#Thomas Jansen
#thomas@ronmix.com

import turtle

draw_turtle = turtle.Turtle()
draw_turtle.hideturtle()
draw_turtle.speed(0)

red_turtle = turtle.Turtle()
red_turtle.hideturtle()
red_turtle.speed(0)
red_turtle.color("red")
red_turtle.right(90)
red_turtle.up()

yellow_turtle = turtle.Turtle()
yellow_turtle.hideturtle()
yellow_turtle.speed(0)
yellow_turtle.color("yellow")
yellow_turtle.right(90)
yellow_turtle.up()

coords = []
kolom1 = []
kolom2 = []
kolom3 = []
kolom4 = []
kolom5 = []
kolom6 = []
kolom7 = []

def draw_board():
    draw_turtle.color("teal")
    draw_turtle.up()
    draw_turtle.goto(-350,300)
    draw_turtle.begin_fill()
    draw_turtle.goto(350,300)
    draw_turtle.goto(350,-300)
    draw_turtle.goto(-350,-300)
    draw_turtle.goto(-350,300)
    draw_turtle.end_fill()

def draw_holes():
    draw_turtle.goto(-335, 250)
    for collum in range(1,8):
        draw_turtle.color("white")
        draw_turtle.forward(35)
        draw_turtle.left(90)
        draw_turtle.forward(35)
        draw_turtle.write(collum, align='center') # deze moet nog op de goede plek
        draw_turtle.right(180)
        draw_turtle.forward(35)
        draw_turtle.right(90)
        draw_turtle.forward(35)
        draw_turtle.left(90)



        for row in range(0,6):
            coords.append(draw_turtle.pos())
            draw_turtle.begin_fill()
            draw_turtle.circle(35)
            draw_turtle.end_fill()
            draw_turtle.forward(100)
        
        draw_turtle.backward(600)
        draw_turtle.left(90)
        draw_turtle.forward(100)

draw_board()
draw_holes()

kolom1 = coords[0:6]
kolom2 = coords[6:12]
kolom3 = coords[12:18]
kolom4 = coords[18:24]
kolom5 = coords[24:30]
kolom6 = coords[30:36]
kolom7 = coords[36:43]

def red_circle():
    red_turtle.begin_fill()
    red_turtle.circle(35)
    red_turtle.end_fill()

def yellow_circle():
    yellow_turtle.begin_fill()
    yellow_turtle.circle(35)
    yellow_turtle.end_fill()

def ronde():
    move_speler1 = int(turtle.numinput("Speler 1", "Speler 1 in welke kolom wil je je fiche plaatsen?", 0, minval=1, maxval=7))
    if move_speler1 == 1:
        red_turtle.goto(kolom1[-1])
        kolom1.pop()
        red_circle()

    if move_speler1 == 2:
        red_turtle.goto(kolom2[-1])
        kolom2.pop()
        red_circle()

    if move_speler1 == 3:
        red_turtle.goto(kolom3[-1])
        kolom3.pop()
        red_circle()
    
    if move_speler1 == 4:
        red_turtle.goto(kolom4[-1])
        kolom4.pop()
        red_circle()

    if move_speler1 == 5:
        red_turtle.goto(kolom5[-1])
        kolom5.pop()
        red_circle()

    if move_speler1 == 6:
        red_turtle.goto(kolom6[-1])
        kolom6.pop()
        red_circle()

    if move_speler1 == 7:
        red_turtle.goto(kolom7[-1])
        kolom7.pop()
        red_circle()

    move_speler2 = int(turtle.numinput("Speler 2", "Speler 2 in welke kolom wil je je fiche plaatsen?", 0, minval=1, maxval=7))
    if move_speler2 == 1:
        yellow_turtle.goto(kolom1[-1])
        kolom1.pop()
        yellow_circle()

    if move_speler2 == 2:
        yellow_turtle.goto(kolom2[-1])
        kolom2.pop()
        yellow_circle()

    if move_speler2 == 3:
        yellow_turtle.goto(kolom3[-1])
        kolom3.pop()
        yellow_circle()
    
    if move_speler2 == 4:
        yellow_turtle.goto(kolom4[-1])
        kolom4.pop()
        yellow_circle()

    if move_speler2 == 5:
        yellow_turtle.goto(kolom5[-1])
        kolom5.pop()
        yellow_circle()

    if move_speler2 == 6:
        yellow_turtle.goto(kolom6[-1])
        kolom6.pop()
        yellow_circle()

    if move_speler2 == 7:
        yellow_turtle.goto(kolom7[-1])
        kolom7.pop()
        yellow_circle()

    ronde()

ronde()
turtle.done ()