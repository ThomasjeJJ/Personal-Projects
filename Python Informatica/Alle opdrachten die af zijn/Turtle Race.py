import turtle
from random import randint
turtle.bgcolor("black")
turtle.title("Turtle Race")
z = 0
x = 0
y = 0


t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.color("white")
t.goto(-200, 200)

schrijf = turtle.Turtle()
schrijf.speed(0)
schrijf.color("White")
schrijf.hideturtle()
schrijf.penup()

#---- Maakt de turtle die de winnaar volgt ------
win = turtle.Turtle()
win.penup()

#---- Maakt de turtle die geklikt kan worden om het opnieuw te starten
again = turtle.Turtle()
again.penup()
again.color("white")
again.hideturtle()
again.shape("circle")
again.turtlesize(2)
#-----------------------------------------------


#--- Tekent het veld -----
for step in range(21):
    t.write(step, align='center')
    t.right(90)
    t.forward(10)
    t.pendown()
    for i in range (3):
        t.forward(20)
        t.penup()
        t.forward(20)
        t.pendown()
    t.penup()
    t.backward(130)
    t.left(90)
    t.forward(20)


#--- Aanmaak van alle race turtles ---
red = turtle.Turtle()
red.color("red")
red.shape("turtle")
#------------------------
blu = turtle.Turtle()
blu.color("blue")
blu.shape("turtle")
#------------------------
gre = turtle.Turtle()
gre.color("green")
gre.shape("turtle")
#-----------------------
gel = turtle.Turtle()
gel.color("yellow")
gel.shape("turtle")
#-----------------------
pur = turtle.Turtle()
pur.color("purple")
pur.shape("turtle")
#-----------------------

win.color("white")

def main(x, y):
    global z

    red.clear()
    blu.clear()
    gre.clear()
    gel.clear()
    pur.clear()
    again.clear()
    again.hideturtle()
    z = 0

    schrijf.clear()
    schrijf.color("white")
    schrijf.goto(-50,0)
    schrijf.write("De winnaar is:", font=("Verdana", 15, "normal", ), align="center")
    schrijf.goto(80,0)
    
    # turtles op de juiste plek zetten
    red.penup()
    red.goto(-220, 180)
    red.pendown()

    blu.penup()
    blu.goto(-220, 160)
    blu.pendown()

    gre.penup()
    gre.goto(-220, 140)
    gre.pendown()

    gel.penup()
    gel.goto(-220, 120)
    gel.pendown()

    pur.penup()
    pur.goto(-220, 100)
    pur.pendown()

    
    while z == 0:
        xcoords = [red.xcor(), blu.xcor(), gre.xcor(), gel.xcor(), pur.xcor()]
        bigx = max(xcoords)
        
        if xcoords.index(bigx) == 0:
            win.goto(-230, 180)
            
        if xcoords.index(bigx) == 1:
            win.goto(-230, 160)
            
        if xcoords.index(bigx) == 2:
            win.goto(-230, 140)
            
        if xcoords.index(bigx) == 3:
            win.goto(-230, 120)
            
        if xcoords.index(bigx) == 4:
            win.goto(-230, 100)

        
    #---- Het random voortbewegins systeem ------
        a = randint(1,5)
        
        if a == 1:
            red.forward(randint(-2,8))
        
        if a == 2:
            blu.forward(randint(-2,8))
        
        if a == 3:
            gre.forward(randint(-2,8))
            
        if a == 4:
            gel.forward(randint(-2,8))
            
        if a == 5:
            pur.forward(randint(-2,8))


    #---- Winnaars detectie systeem ------------
        if (red.xcor() ) > 200 and z == 0:
            schrijf.color("red")
            schrijf.write("Rood!", font=("Verdana", 15, "normal", ), align="center")
            red.penup()
            red.goto(130, 10)
            z = 1
        if (blu.xcor() ) > 200 and z == 0:
            schrijf.color("blue")
            schrijf.write("Blauw!", font=("Verdana", 15, "normal", ), align="center")
            blu.penup()
            blu.goto(130, 10)
            z = 1
        if (gre.xcor() ) > 200 and z == 0:
            schrijf.color("green")
            schrijf.write("Groen!", font=("Verdana", 15, "normal", ), align="center")
            gre.penup()
            gre.goto(130, 10)
            z = 1
        if (gel.xcor() ) > 200 and z == 0:
            schrijf.color("yellow")
            schrijf.write("Geel!", font=("Verdana", 15, "normal", ), align="center")
            gel.penup()
            gel.goto(130, 10)
            z = 1
        if (pur.xcor() ) > 200 and z == 0:
            schrijf.color("purple")
            schrijf.write("Paars!", font=("Verdana", 15, "normal", ), align="center")
            pur.penup()
            pur.goto(130, 10)
            z = 1
        if z == 1:
            again.goto(0, -150)
            again.write("Klik op de knop om nog een keer te spelen", False, align="center", font=("Yu Gothic UI Semibold", 20, "normal", ))
            again.goto(0, -100)
            again.showturtle()
            again.onclick(main)


main(x, y)

turtle.done()