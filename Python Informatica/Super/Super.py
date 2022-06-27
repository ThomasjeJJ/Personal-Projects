#Thomas Jansen
#thomas@ronmix.com

import turtle
import os
#os.path.abspath("Assets/continue.gif")

def make_turtles():
    global continue_turtle, startmain, harten, ruiten, schoppen, klaver, speler_turtle1, speler_turtle2, speler_turtle3, speler_turtle4, joker_turtle, schrijf_turtle, niemand_turtle, score_turtle

    win = turtle.Screen()
    win.addshape(r"Assets\harten.gif")
    win.addshape(r"Assets\ruiten.gif")
    win.addshape(r"Assets\schoppen.gif")
    win.addshape(r"Assets\klaver.gif")
    win.addshape(r"Assets\start_game.gif")
    win.addshape(r"Assets\continue.gif")
    win.addshape(r"Assets\niemand.gif")
    win.addshape(r"Assets\volgende_ronde.gif")
    

    harten = turtle.Turtle()
    harten.speed(0)
    harten.penup()
    harten.goto(-200,-50)
    harten.shape(r"Assets\harten.gif")
    harten.hideturtle()

    ruiten = turtle.Turtle()
    ruiten.speed(0)
    ruiten.penup()
    ruiten.goto(-100,-50)
    ruiten.shape(r"Assets\ruiten.gif")
    ruiten.hideturtle()

    schoppen = turtle.Turtle()
    schoppen.speed(0)
    schoppen.penup()
    schoppen.goto(100,-50)
    schoppen.shape(r"Assets\schoppen.gif")
    schoppen.hideturtle()

    klaver = turtle.Turtle()
    klaver.speed(0)
    klaver.penup()
    klaver.goto(200,-50)
    klaver.shape(r"Assets\klaver.gif")
    klaver.hideturtle()

    startmain = turtle.Turtle() #deze moet ook beschikbaar zijn als de namen al bekend zijn
    startmain.speed(0)
    startmain.shape(r"Assets\start_game.gif")
    startmain.penup()
    startmain.goto(-100,100)

    continue_turtle = turtle.Turtle() #moet als eerste komen deze vraagt voor de namen van de spelers
    continue_turtle.speed(0)
    continue_turtle.shape(r"Assets\continue.gif")
    continue_turtle.penup()
    continue_turtle.goto(100,100)

    
    speler_turtle1 = turtle.Turtle()
    speler_turtle1.speed(0)
    speler_turtle1.shape("circle")
    speler_turtle1.turtlesize(2)
    speler_turtle1.penup()
    speler_turtle1.hideturtle()

    speler_turtle2 = turtle.Turtle()
    speler_turtle2.speed(0)
    speler_turtle2.shape("circle")
    speler_turtle2.turtlesize(2)
    speler_turtle2.penup()
    speler_turtle2.hideturtle()

    speler_turtle3 = turtle.Turtle()
    speler_turtle3.speed(0)
    speler_turtle3.shape("circle")
    speler_turtle3.turtlesize(2)
    speler_turtle3.penup()
    speler_turtle3.hideturtle()

    speler_turtle4 = turtle.Turtle()
    speler_turtle4.speed(0)
    speler_turtle4.shape("circle")
    speler_turtle4.turtlesize(2)
    speler_turtle4.penup()
    speler_turtle4.hideturtle()


    joker_turtle = turtle.Turtle()
    joker_turtle.speed(0)
    joker_turtle.penup()
    joker_turtle.hideturtle()

    schrijf_turtle = turtle.Turtle()
    schrijf_turtle.speed(0)
    schrijf_turtle.penup()
    schrijf_turtle.hideturtle()
    schrijf_turtle.goto(0, 100)

    niemand_turtle = turtle.Turtle()
    niemand_turtle.speed(0)
    niemand_turtle.shape(r"Assets\niemand.gif")
    niemand_turtle.penup()
    niemand_turtle.hideturtle()
    niemand_turtle.goto(0, -180)

    score_turtle = turtle.Turtle()
    score_turtle.speed(0)
    score_turtle.penup()
    score_turtle.hideturtle()
    score_turtle.shape(r"Assets\volgende_ronde.gif")

make_turtles()

score_1 = 0
score_2 = 0
score_3 = 0
score_4 = 0

def hide_turtles():
    harten.hideturtle()
    ruiten.hideturtle()
    schoppen.hideturtle()
    klaver.hideturtle()
    niemand_turtle.hideturtle()
    speler_turtle1.hideturtle()
    speler_turtle2.hideturtle()
    speler_turtle3.hideturtle()
    speler_turtle4.hideturtle()
    speler_turtle1.clear()
    speler_turtle2.clear()
    speler_turtle3.clear()
    speler_turtle4.clear()
    schrijf_turtle.clear()


def harten_verdubbelaar(x, y):
    global verdubbelaar
    verdubbelaar = 5
    joker_vraag()

def ruiten_verdubbelaar(x, y):
    global verdubbelaar
    verdubbelaar = 4
    joker_vraag()

def schoppen_verdubbelaar(x, y):
    global verdubbelaar
    verdubbelaar = 3
    joker_vraag()

def klaver_verdubbelaar(x, y):
    global verdubbelaar
    verdubbelaar = 2
    joker_vraag()


def main(x, y):
    global aantal_spelers, score_1, score_2, score_3, score_4, verdubbelaar

    hide_turtles()

    punten1 = 0
    punten2 = 0
    punten3 = 0
    punten4 = 0

    punten1 = int(turtle.numinput(f"Aantal punten {speler1}", f"Vul het aantal punten in van {speler1}"))
    punten2 = int(turtle.numinput(f"Aantal punten {speler2}", f"Vul het aantal punten in van {speler2}"))
    punten3 = int(turtle.numinput(f"Aantal punten {speler3}", f"Vul het aantal punten in van {speler3}"))
   
    if aantal_spelers == 4:
        punten4 = int(turtle.numinput(f"Aantal punten {speler4}", f"Vul het aantal punten in van {speler4}"))

    if punten1 == -500:
        score_1 = score_1 - 500
        verdubbelaar = 2 * verdubbelaar
    if punten1 == -1000:
        score_1 = score_1 - 1000
        verdubbelaar = 2 * verdubbelaar

    if punten2 == -500:
        score_2 = score_2 - 500
        verdubbelaar = 2 * verdubbelaar
    if punten2 == -1000:
        score_2 = score_2 - 1000
        verdubbelaar = 2 * verdubbelaar

    if punten3 == -500:
        score_3 = score_3 - 500
        verdubbelaar = 2 * verdubbelaar
    if punten3 == -1000:
        score_3 = score_3 - 1000
        verdubbelaar = 2 * verdubbelaar

    if punten4 == -500: 
        score_4 = score_4 - 500
        verdubbelaar = 2 * verdubbelaar
    if punten4 == -1000:
        score_4 = score_4 - 1000
        verdubbelaar = 2 * verdubbelaar

    if punten1 == -100:
        score_1 = score_1 - 100
    if punten2 == -100:
            score_2 = score_2 - 100
    if punten3 == -100:
        score_3 = score_3 - 100
    if punten4 == -100:
        score_4 = score_4 - 100

    if punten1 == 500:
        score_1 = score_1 + 500
    if punten2 == 500:
        score_2 = score_2 + 500
    if punten3 == 500:
        score_3 = score_3 + 500
    if punten4 == 500:
        score_4 = score_4 + 500

    if punten1 > 0 and punten1 < 500:
        score_1 = score_1 + punten1 * verdubbelaar
    if punten2 > 0 and punten2 < 500:
        score_2 = score_2 + punten2 * verdubbelaar
    if punten3 > 0 and punten3 < 500:
        score_3 = score_3 + punten3 * verdubbelaar
    if punten4 > 0 and punten4 < 500:
        score_4 = score_4 + punten4 * verdubbelaar

    score_turtle.clear()
    score_turtle.showturtle()

    score_turtle.goto(0, 60)
    score_turtle.write(f"{speler1} heeft nu {score_1} punten", False, align="center", font=("System", 20, "normal", ))
    
    score_turtle.goto(0, 20)
    score_turtle.write(f"{speler2} heeft nu {score_2} punten", False, align="center", font=("System", 20, "normal", ))
    
    score_turtle.goto(0, -20)
    score_turtle.write(f"{speler3} heeft nu {score_3} punten", False, align="center", font=("System", 20, "normal", ))
    
    score_turtle.goto(0, -60)
    if aantal_spelers == 4:
        score_turtle.write(f"{speler4} heeft nu {score_4} punten", False, align="center", font=("System", 20, "normal", ))

    score_turtle.showturtle()
    score_turtle.goto(0, -150)
    score_turtle.onclick(joker_functie)



def joker1 (x, y):
    global score_1
    score_1 = score_1 + (-10 * verdubbelaar)
    print(f"Score van {speler1} is nu {score_1}")
    main(x, y)

def joker2 (x, y):
    global score_2
    score_2 = score_2 + (-10 * verdubbelaar)
    print(f"Score van {speler2} is nu {score_2}")
    main(x, y)

def joker3 (x, y):
    global score_3
    score_3 = score_3 + (-10 * verdubbelaar)
    print(f"Score van {speler3} is nu {score_3}")
    main(x, y)

def joker4 (x, y):
    global score_4
    score_4 = score_4 + (-10 * verdubbelaar)
    print(f"Score van {speler4} is nu {score_4}")
    main(x, y)


def joker_vraag():

    hide_turtles()
    schrijf_turtle.clear()
    schrijf_turtle.write("Wie heeft de gebroken kaart?", False, align="center", font=("System", 20, "normal", ))


    if aantal_spelers == 4:
        speler_turtle4.showturtle()
        speler_turtle4.goto(100,-100)
        speler_turtle4.write(speler4, False, align="center", font=("System", 20, "normal", ))
        speler_turtle4.goto(100, -120)

    speler_turtle1.showturtle()
    speler_turtle1.goto(-100,60)
    speler_turtle1.write(speler1, False, align="center", font=("System", 20, "normal", ))
    speler_turtle1.goto(-100, 40)
    
    speler_turtle2.showturtle()
    speler_turtle2.goto(100,60)
    speler_turtle2.write(speler2, False, align="center", font=("System", 20, "normal", ))
    speler_turtle2.goto(100, 40)
    
    speler_turtle3.showturtle()
    speler_turtle3.goto(-100,-100)
    speler_turtle3.write(speler3, False, align="center", font=("System", 20, "normal", ))
    speler_turtle3.goto(-100, -120)
    

    niemand_turtle.showturtle()
    
    speler_turtle1.onclick(joker1)
    speler_turtle2.onclick(joker2)
    speler_turtle3.onclick(joker3)
    speler_turtle4.onclick(joker4)

    niemand_turtle.onclick(main)


def spelers (x, y):
    global aantal_spelers, speler1, speler2, speler3, speler4, harten, ruiten, schoppen, klaver
    
    startmain.hideturtle()
    continue_turtle.hideturtle()
    
    aantal_spelers = int(turtle.numinput("Aantal spelers", "Geef het aantal spelers minimaal 3 en maximaal 4:", 3, minval=3, maxval=4))

    speler1 = turtle.textinput("Speler 1", "Naam van speler 1:")
    speler2 = turtle.textinput("Speler 2", "Naam van speler 2:")
    speler3 = turtle.textinput("Speler 3", "Naam van speler 3:")   
    if aantal_spelers == 4:
        speler4 = turtle.textinput("Speler 4", "Naam van speler 4:")

    joker_functie(x, y)


def joker_functie(x, y):
    global aantal_spelers, score_1, score_2, score_3, score_4, verdubbelaar
    
    startmain.hideturtle()
    continue_turtle.hideturtle()
    score_turtle.hideturtle()
    score_turtle.clear()

    schrijf_turtle.write("Wat is de gebroken kaart?", False, align="center", font=("System", 20, "normal", ))

    harten.showturtle()
    ruiten.showturtle()
    schoppen.showturtle()
    klaver.showturtle()

    harten.onclick(harten_verdubbelaar)
    ruiten.onclick(ruiten_verdubbelaar)
    schoppen.onclick(schoppen_verdubbelaar)
    klaver.onclick(klaver_verdubbelaar)



startmain.onclick(spelers)
continue_turtle.onclick(joker_functie)


turtle.done()