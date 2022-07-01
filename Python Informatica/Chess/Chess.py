#Thomas Jansen
#thomas@ronmix.com

from cmath import rect
from pydoc import cli
from shutil import move
from tkinter.messagebox import YES
import pygame
import time
import os

#initializes every module
pygame.init()

#makes the screen and makes it have the right properties
WIDTH, HEIGHT = 800, 660
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

#Chess pieces
Bischop_B = pygame.image.load(os.path.join("Chess_Pieces","Bischop_B.png"))
Bischop_W = pygame.image.load(os.path.join("Chess_Pieces","Bischop_W.png"))
Queen_B = pygame.image.load(os.path.join("Chess_Pieces","Queen_B.png"))
Queen_W = pygame.image.load(os.path.join("Chess_Pieces","Queen_W.png"))
King_B = pygame.image.load(os.path.join("Chess_Pieces","King_B.png"))
King_W = pygame.image.load(os.path.join("Chess_Pieces","King_W.png"))
Pawn_B = pygame.image.load(os.path.join("Chess_Pieces","Pawn_B.png"))
Pawn_W = pygame.image.load(os.path.join("Chess_Pieces","Pawn_W.png"))
Queen_B = pygame.image.load(os.path.join("Chess_Pieces","Queen_B.png"))
Queen_W = pygame.image.load(os.path.join("Chess_Pieces","Queen_W.png"))
Rook_B = pygame.image.load(os.path.join("Chess_Pieces","Rook_B.png"))
Rook_W = pygame.image.load(os.path.join("Chess_Pieces","Rook_W.png"))

#list of coordinates for the position of the pieces
coords = []
coordsX = [90, 170, 250, 330, 410, 490, 570, 650, 999, 90]
coordsY = [20, 100, 180, 260, 340, 420, 500, 580, 999, 20]


#Function for making the list of coordinates needed for the right placements
def list_maker():
    for y in range(0, 640, 80):
        for x in range(0, 640, 80):
            coords.append((90+x, 20+y))
list_maker()

#variables
cellSize = 80
FPS = 60
x = 0
y = 0


move_made = 0

clicked_square_x, clicked_square_y = 0, 0


lst_Bischop_B_1 = []
lst_Bischop_B_2 = []
lst_Bischop_W_1 = []
lst_Bischop_W_2 = []

lst_Queen_B_1 = []
lst_Queen_B_2 = []
lst_Queen_W_1 = []
lst_Queen_W_2 = []

lst_Rook_B_1 = []
lst_Rook_B_2 = []
lst_Rook_W_1 = []
lst_Rook_W_2 = []

lst_King_B = []
lst_King_W = []

lst_Queen_B = []
lst_Queen_W = []

lst_Pawn_B_1 = []
lst_Pawn_B_2 = []
lst_Pawn_B_3 = []
lst_Pawn_B_4 = []
lst_Pawn_B_5 = []
lst_Pawn_B_6 = []
lst_Pawn_B_7 = []
lst_Pawn_B_8 = []

lst_Pawn_W_1 = []
lst_Pawn_W_2 = []
lst_Pawn_W_3 = []
lst_Pawn_W_4 = []
lst_Pawn_W_5 = []
lst_Pawn_W_6 = []
lst_Pawn_W_7 = []
lst_Pawn_W_8 = []



First_Bischop_B_1, First_Bischop_B_2 = 0, 0
Captured_Bischop_B_1, Captured_Bischop_B_2 = 0, 0
Bischop_B_1_x, Bischop_B_1_y = 0, 0
Bischop_B_2_x, Bischop_B_2_y = 0, 0

First_Bischop_W_1, First_Bischop_W_2 = 0, 0
Captured_Bischop_W_1, Captured_Bischop_W_2 = 0, 0
Bischop_W_1_x, Bischop_W_1_y = 0, 0
Bischop_W_2_x, Bischop_W_2_y = 0, 0
#-----------------------------------------------
First_Queen_B_1, First_Queen_B_2 = 0, 0
Captured_Queen_B_1, Captured_Queen_B_2 = 0, 0
Queen_B_1_x, Queen_B_1_y = 0, 0
Queen_B_2_x, Queen_B_2_y = 0, 0

First_Queen_W_1, First_Queen_W_2 = 0, 0
Captured_Queen_W_1, Captured_Queen_W_2 = 0, 0
Queen_W_1_x, Queen_W_1_y = 0, 0
Queen_W_2_x, Queen_W_2_y = 0, 0
#-----------------------------------------------
First_Rook_B_1, First_Rook_B_2 = 0, 0
Captured_Rook_B_1, Captured_Rook_B_2 = 0, 0
Rook_B_1_x, Rook_B_1_y = 0, 0
Rook_B_2_x, Rook_B_2_y = 0, 0

First_Rook_W_1, First_Rook_W_2 = 0, 0
Captured_Rook_W_1, Captured_Rook_W_2 = 0, 0
Rook_W_1_x, Rook_W_1_y = 0, 0
Rook_W_2_x, Rook_W_2_y = 0, 0
#-----------------------------------------------
First_King_B= 0
Captured_King_B = 0
King_B_x, King_B_y = 0, 0

First_King_W = 0
Captured_King_W_1 = 0
King_W_x, King_W_y = 0, 0
#-----------------------------------------------
First_Queen_B= 0
Captured_Queen_B = 0
Queen_B_x, Queen_B_y = 0, 0

First_Queen_W = 0
Captured_Queen_W_1 = 0
Queen_W_x, Queen_W_y = 0, 0
#-----------------------------------------------
#Pawns
#-----------------------------------------------
First_Rook_B_1, First_Rook_B_2 = 0, 0
Captured_Rook_B_1, Captured_Rook_B_2 = 0, 0
Rook_B_1_x, Rook_B_1_y = 0, 0
Rook_B_2_x, Rook_B_2_y = 0, 0

First_Rook_W_1, First_Rook_W_2 = 0, 0
Captured_Rook_W_1, Captured_Rook_W_2 = 0, 0
Rook_W_1_x, Rook_W_1_y = 0, 0
Rook_W_2_x, Rook_W_2_y = 0, 0

First_Rook_B_3, First_Rook_B_4 = 0, 0
Captured_Rook_B_3, Captured_Rook_B_4 = 0, 0
Rook_B_3_x, Rook_B_3_y = 0, 0
Rook_B_4_x, Rook_B_4_y = 0, 0

First_Rook_W_3, First_Rook_W_4 = 0, 0
Captured_Rook_W_3, Captured_Rook_W_4 = 0, 0
Rook_W_3_x, Rook_W_3_y = 0, 0
Rook_W_4_x, Rook_W_4_y = 0, 0

First_Rook_B_5, First_Rook_B_6 = 0, 0
Captured_Rook_B_5, Captured_Rook_B_6 = 0, 0
Rook_B_5_x, Rook_B_5_y = 0, 0
Rook_B_6_x, Rook_B_6_y = 0, 0

First_Rook_W_5, First_Rook_W_6 = 0, 0
Captured_Rook_W_5, Captured_Rook_W_6 = 0, 0
Rook_W_5_x, Rook_W_5_y = 0, 0
Rook_W_6_x, Rook_W_6_y = 0, 0

First_Rook_B_7, First_Rook_B_8 = 0, 0
Captured_Rook_B_7, Captured_Rook_B_8 = 0, 0
Rook_B_7_x, Rook_B_7_y = 0, 0
Rook_B_8_x, Rook_B_8_y = 0, 0

First_Rook_W_7, First_Rook_W_8 = 0, 0
Captured_Rook_W_7, Captured_Rook_W_8 = 0, 0
Rook_W_7_x, Rook_W_7_y = 0, 0
Rook_W_8_x, Rook_W_8_y = 0, 0
#-----------------------------------------------







# Colors
black = (0, 0, 0)
white = (255, 255, 255)
tile_black = (128, 0, 0)
tile_white = (255, 255, 255)
bg_grey = (48, 44, 52)



#makes a surface so I can call the whole board easy
board = pygame.Surface((cellSize * 8, cellSize * 8))
pygame.Surface.fill(board, tile_black)

#Colors the background
win.fill(bg_grey)


#Function for drawing the chess board
def draw_board():
    #loop for moving from row to row
    for x in range (0, 8, 2):
        #loop for the moving in the row
        for y in range (0, 8, 2):
            pygame.draw.rect(board, tile_white, (x*cellSize, y*cellSize, 80, 80))
    
    for x in range (1, 8, 2):
        #loop for the moving in the row
        for y in range (1, 8, 2):
            pygame.draw.rect(board, tile_white, (x*cellSize, y*cellSize, 80, 80))
    #A nice border around the board
    pygame.draw.rect(win, black, pygame.Rect(73, 3, cellSize * 8 + 14, cellSize * 8 + 14))
    win.blit(board, (80, 10))


def Clicked ():
    global clicked_square_x, clicked_square_y, move_made
    global Captured_Bischop_B_1

    k = 0
    g = 0
    ClickedX = 0
    ClickedY = 0

    while ClickedX == 0:
        if 40 + coordsX[k] < x:
            k += 1
        else:
            ClickedX = 1
            if x - (40 + coordsX[k-1]) <= (40 + coordsX[k]) - x:
                clicked_square_x = coordsX[k-1]
            else:
                clicked_square_x = coordsX[k]

    
    while ClickedY == 0:
        if 40 + coordsY[g] < y:
            g += 1
        else:
            ClickedY = 1
            if y - (40 + coordsY[g-1]) <= (40 + coordsY[g]) - y:
                clicked_square_y = coordsY[g-1]
            else:
                clicked_square_y = coordsY[g] 

    if Bischop_B_1_x == clicked_square_x and Bischop_B_1_y == clicked_square_y:
        Captured_Bischop_B_1 = 1

#function for displaying everything
def draw_window():
    global clicked_square_x, clicked_square_y, move_made
    global Bischop_B_1_x, Bischop_B_1_y, Bischop_B_2_x, Bischop_B_2_y, First_Bischop_B_1, First_Bischop_B_2
    global Bischop_W_1_x, Bischop_W_1_y, Bischop_W_2_x, Bischop_W_2_y, First_Bischop_W_1, First_Bischop_W_2


    if move_made == 1:

        if First_Bischop_B_1 == 3 and Captured_Bischop_B_1 == 0:
            win.blit(Bischop_B, (Bischop_B_1_x, Bischop_B_1_y))
        else:
            win.blit(Bischop_B, (1000, 0))
        
        if First_Bischop_B_2 == 3:
            win.blit(Bischop_B, (Bischop_B_2_x, Bischop_B_2_y))

        if First_Bischop_W_1 == 3:
            win.blit(Bischop_W, (Bischop_W_1_x, Bischop_W_1_y))
        
        if First_Bischop_W_2 == 3:
            win.blit(Bischop_W, (Bischop_W_2_x, Bischop_W_2_y))

    move_made = 0


    if First_Bischop_B_1 == 0:
        lst_Bischop_B_1.append(win.blit(Bischop_B, (coords[2])))
        Bischop_B_1_x, Bischop_B_1_y = coords[2][0], coords[2][1]
    
    if First_Bischop_B_1 == 2:
        lst_Bischop_B_1[0] = win.blit(Bischop_B, (clicked_square_x, clicked_square_y))
        Bischop_B_1_x, Bischop_B_1_y = clicked_square_x, clicked_square_y



    if First_Bischop_B_2 == 0:
        lst_Bischop_B_2.append(win.blit(Bischop_B, (coords[5])))
        Bischop_B_2_x, Bischop_B_2_y = coords[5][0], coords[5][1]

    if First_Bischop_B_2 == 2:
        lst_Bischop_B_2[0] = win.blit(Bischop_B, (clicked_square_x, clicked_square_y))
        Bischop_B_2_x, Bischop_B_2_y = clicked_square_x, clicked_square_y

    #---------------------
    if First_Bischop_W_1 == 0:
        lst_Bischop_W_1.append(win.blit(Bischop_W, (coords[58])))
        Bischop_W_1_x, Bischop_W_1_y = coords[58][0], coords[58][1]
    
    if First_Bischop_W_1 == 2:
        lst_Bischop_W_1[0] = win.blit(Bischop_W, (clicked_square_x, clicked_square_y))
        Bischop_W_1_x, Bischop_W_1_y = clicked_square_x, clicked_square_y



    if First_Bischop_W_2 == 0:
        lst_Bischop_W_2.append(win.blit(Bischop_W, (coords[61])))
        Bischop_W_2_x, Bischop_W_2_y = coords[61][0], coords[61][1]

    if First_Bischop_W_2 == 2:
        lst_Bischop_W_2[0] = win.blit(Bischop_W, (clicked_square_x, clicked_square_y))
        Bischop_W_2_x, Bischop_W_2_y = clicked_square_x, clicked_square_y

    First_Bischop_B_1 = 3
    First_Bischop_B_2 = 3
    First_Bischop_W_1 = 3
    First_Bischop_W_2 = 3

    pygame.display.update()

def main():
    global p, x, y, move_made
    global First_Bischop_B_1, First_Bischop_B_2, First_Bischop_W_1, First_Bischop_W_2

    aantalKliks_B_1 = 0
    aantalKliks_B_2 = 0
    aantalKliks_W_1 = 0
    aantalKliks_W_2 = 0

    #makes the game run at 60 fps so it doesnt use too many computer resources
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if any(rect.collidepoint(x, y) for rect in lst_Bischop_B_1):
                    aantalKliks_B_1 += 1
                elif aantalKliks_B_1 == 1:
                    aantalKliks_B_1 = 0
                    Clicked()
                    First_Bischop_B_1 = 2
                    move_made = 1
                    draw_board()
                    

                if any(rect.collidepoint(x, y) for rect in lst_Bischop_B_2):
                    aantalKliks_B_2 += 1
                elif aantalKliks_B_2 == 1:
                    aantalKliks_B_2 = 0
                    Clicked()
                    First_Bischop_B_2 = 2
                    move_made = 1
                    draw_board()
#----------------
                if any(rect.collidepoint(x, y) for rect in lst_Bischop_W_1):
                    aantalKliks_W_1 += 1
                elif aantalKliks_W_1 == 1:
                    aantalKliks_W_1 = 0
                    Clicked()
                    First_Bischop_W_1 = 2
                    move_made = 1
                    draw_board()

                if any(rect.collidepoint(x, y) for rect in lst_Bischop_W_2):
                    aantalKliks_W_2 += 1
                elif aantalKliks_W_2 == 1:
                    aantalKliks_W_2 = 0
                    Clicked()
                    First_Bischop_W_2 = 2
                    move_made = 1
                    draw_board()       

        draw_window()

    pygame.quit()

draw_board()
main()