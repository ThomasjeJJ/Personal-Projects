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
Horse_B = pygame.image.load(os.path.join("Chess_Pieces","Horse_B.png"))
Horse_W = pygame.image.load(os.path.join("Chess_Pieces","Horse_W.png"))
King_B = pygame.image.load(os.path.join("Chess_Pieces","King_B.png"))
King_W = pygame.image.load(os.path.join("Chess_Pieces","King_W.png"))
Queen_B = pygame.image.load(os.path.join("Chess_Pieces","Queen_B.png"))
Queen_W = pygame.image.load(os.path.join("Chess_Pieces","Queen_W.png"))
Pawn_B = pygame.image.load(os.path.join("Chess_Pieces","Pawn_B.png"))
Pawn_W = pygame.image.load(os.path.join("Chess_Pieces","Pawn_W.png"))
Horse_B = pygame.image.load(os.path.join("Chess_Pieces","Horse_B.png"))
Horse_W = pygame.image.load(os.path.join("Chess_Pieces","Horse_W.png"))
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
FPS = 20
x = 0
y = 0


move_made = 0

clicked_square_x, clicked_square_y = 0, 0


lst_Bischop_B_1 = []
lst_Bischop_B_2 = []
lst_Bischop_W_1 = []
lst_Bischop_W_2 = []

lst_Horse_B_1 = []
lst_Horse_B_2 = []
lst_Horse_W_1 = []
lst_Horse_W_2 = []

lst_Rook_B_1 = []
lst_Rook_B_2 = []
lst_Rook_W_1 = []
lst_Rook_W_2 = []

lst_King_B = []
lst_King_W = []

lst_Queen_B = []
lst_Queen_W = []

lst_Horse_B = []
lst_Horse_W = []

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
First_Horse_B_1, First_Horse_B_2 = 0, 0
Captured_Horse_B_1, Captured_Horse_B_2 = 0, 0
Horse_B_1_x, Horse_B_1_y = 0, 0
Horse_B_2_x, Horse_B_2_y = 0, 0

First_Horse_W_1, First_Horse_W_2 = 0, 0
Captured_Horse_W_1, Captured_Horse_W_2 = 0, 0
Horse_W_1_x, Horse_W_1_y = 0, 0
Horse_W_2_x, Horse_W_2_y = 0, 0
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
Captured_King_W = 0
King_W_x, King_W_y = 0, 0
#-----------------------------------------------
First_Queen_B= 0
Captured_Queen_B = 0
Queen_B_x, Queen_B_y = 0, 0

First_Queen_W = 0
Captured_Queen_W = 0
Queen_W_x, Queen_W_y = 0, 0
#-----------------------------------------------
First_Pawn_B_1, First_Pawn_B_2 = 0, 0
Captured_Pawn_B_1, Captured_Pawn_B_2 = 0, 0
Pawn_B_1_x, Pawn_B_1_y = 0, 0
Pawn_B_2_x, Pawn_B_2_y = 0, 0

First_Pawn_W_1, First_Pawn_W_2 = 0, 0
Captured_Pawn_W_1, Captured_Pawn_W_2 = 0, 0
Pawn_W_1_x, Pawn_W_1_y = 0, 0
Pawn_W_2_x, Pawn_W_2_y = 0, 0

First_Pawn_B_3, First_Pawn_B_4 = 0, 0
Captured_Pawn_B_3, Captured_Pawn_B_4 = 0, 0
Pawn_B_3_x, Pawn_B_3_y = 0, 0
Pawn_B_4_x, Pawn_B_4_y = 0, 0

First_Pawn_W_3, First_Pawn_W_4 = 0, 0
Captured_Pawn_W_3, Captured_Pawn_W_4 = 0, 0
Pawn_W_3_x, Pawn_W_3_y = 0, 0
Pawn_W_4_x, Pawn_W_4_y = 0, 0

First_Pawn_B_5, First_Pawn_B_6 = 0, 0
Captured_Pawn_B_5, Captured_Pawn_B_6 = 0, 0
Pawn_B_5_x, Pawn_B_5_y = 0, 0
Pawn_B_6_x, Pawn_B_6_y = 0, 0

First_Pawn_W_5, First_Pawn_W_6 = 0, 0
Captured_Pawn_W_5, Captured_Pawn_W_6 = 0, 0
Pawn_W_5_x, Pawn_W_5_y = 0, 0
Pawn_W_6_x, Pawn_W_6_y = 0, 0

First_Pawn_B_7, First_Pawn_B_8 = 0, 0
Captured_Pawn_B_7, Captured_Pawn_B_8 = 0, 0
Pawn_B_7_x, Pawn_B_7_y = 0, 0
Pawn_B_8_x, Pawn_B_8_y = 0, 0

First_Pawn_W_7, First_Pawn_W_8 = 0, 0
Captured_Pawn_W_7, Captured_Pawn_W_8 = 0, 0
Pawn_W_7_x, Pawn_W_7_y = 0, 0
Pawn_W_8_x, Pawn_W_8_y = 0, 0
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
    global Captured_Bischop_B_1, Captured_Bischop_B_2, Captured_Bischop_W_1, Captured_Bischop_W_2
    global Captured_Horse_B_1, Captured_Horse_B_2, Captured_Horse_W_1, Captured_Horse_W_2
    global Captured_Rook_B_1, Captured_Rook_B_2, Captured_Rook_W_1, Captured_Rook_W_2
    global Captured_King_B, Captured_Queen_B, Captured_King_W, Captured_Queen_W
    global Captured_Pawn_B_1, Captured_Pawn_B_2, Captured_Pawn_B_3, Captured_Pawn_B_4, Captured_Pawn_B_5, Captured_Pawn_B_6, Captured_Pawn_B_7, Captured_Pawn_B_8
    global Captured_Pawn_W_1, Captured_Pawn_W_2, Captured_Pawn_W_3, Captured_Pawn_W_4, Captured_Pawn_W_5, Captured_Pawn_W_6, Captured_Pawn_W_7, Captured_Pawn_W_8

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

#--------------------------------------------------------------
    if Bischop_B_1_x == clicked_square_x and Bischop_B_1_y == clicked_square_y:
        Captured_Bischop_B_1 = 1
    if Bischop_B_2_x == clicked_square_x and Bischop_B_2_y == clicked_square_y:
        Captured_Bischop_B_2 = 1

    if Horse_B_1_x == clicked_square_x and Horse_B_1_y == clicked_square_y:
        Captured_Horse_B_1 = 1
    if Horse_B_2_x == clicked_square_x and Horse_B_2_y == clicked_square_y:
        Captured_Horse_B_2 = 1

    if Rook_B_1_x == clicked_square_x and Rook_B_1_y == clicked_square_y:
        Captured_Rook_B_1 = 1
    if Rook_B_2_x == clicked_square_x and Rook_B_2_y == clicked_square_y:
        Captured_Rook_B_2 = 1

    if King_B_x == clicked_square_x and King_B_y == clicked_square_y:
        Captured_King_B = 1

    if Queen_B_x == clicked_square_x and Queen_B_y == clicked_square_y:
        Captured_Queen_B = 1

    if Pawn_B_1_x == clicked_square_x and Pawn_B_1_y == clicked_square_y:
        Captured_Pawn_B_1 = 1
    if Pawn_B_2_x == clicked_square_x and Pawn_B_2_y == clicked_square_y:
        Captured_Pawn_B_2 = 1
    if Pawn_B_3_x == clicked_square_x and Pawn_B_3_y == clicked_square_y:
        Captured_Pawn_B_3 = 1
    if Pawn_B_4_x == clicked_square_x and Pawn_B_4_y == clicked_square_y:
        Captured_Pawn_B_4 = 1
    if Pawn_B_5_x == clicked_square_x and Pawn_B_5_y == clicked_square_y:
        Captured_Pawn_B_5 = 1
    if Pawn_B_6_x == clicked_square_x and Pawn_B_6_y == clicked_square_y:
        Captured_Pawn_B_6 = 1
    if Pawn_B_7_x == clicked_square_x and Pawn_B_7_y == clicked_square_y:
        Captured_Pawn_B_7 = 1
    if Pawn_B_8_x == clicked_square_x and Pawn_B_8_y == clicked_square_y:
        Captured_Pawn_B_8 = 1

#------------------
    if Bischop_W_1_x == clicked_square_x and Bischop_W_1_y == clicked_square_y:
        Captured_Bischop_W_1 = 1
    if Bischop_W_2_x == clicked_square_x and Bischop_W_2_y == clicked_square_y:
        Captured_Bischop_W_2 = 1

    if Horse_W_1_x == clicked_square_x and Horse_W_1_y == clicked_square_y:
        Captured_Horse_W_1 = 1
    if Horse_W_2_x == clicked_square_x and Horse_W_2_y == clicked_square_y:
        Captured_Horse_W_2 = 1

    if Rook_W_1_x == clicked_square_x and Rook_W_1_y == clicked_square_y:
        Captured_Rook_W_1 = 1
    if Rook_W_2_x == clicked_square_x and Rook_W_2_y == clicked_square_y:
        Captured_Rook_W_2 = 1

    if King_W_x == clicked_square_x and King_W_y == clicked_square_y:
        Captured_King_W = 1

    if Queen_W_x == clicked_square_x and Queen_W_y == clicked_square_y:
        Captured_Queen_W = 1

    if Pawn_W_1_x == clicked_square_x and Pawn_W_1_y == clicked_square_y:
        Captured_Pawn_W_1 = 1
    if Pawn_W_2_x == clicked_square_x and Pawn_W_2_y == clicked_square_y:
        Captured_Pawn_W_2 = 1

    if Pawn_W_3_x == clicked_square_x and Pawn_W_3_y == clicked_square_y:
        Captured_Pawn_W_3 = 1
    if Pawn_W_4_x == clicked_square_x and Pawn_W_4_y == clicked_square_y:
        Captured_Pawn_W_4 = 1
    
    if Pawn_W_5_x == clicked_square_x and Pawn_W_5_y == clicked_square_y:
        Captured_Pawn_W_5 = 1
    if Pawn_W_6_x == clicked_square_x and Pawn_W_6_y == clicked_square_y:
        Captured_Pawn_W_6 = 1
    
    if Pawn_W_7_x == clicked_square_x and Pawn_W_7_y == clicked_square_y:
        Captured_Pawn_W_7 = 1
    if Pawn_W_8_x == clicked_square_x and Pawn_W_8_y == clicked_square_y:
        Captured_Pawn_W_8 = 1

#function for displaying everything
def draw_window():
    global clicked_square_x, clicked_square_y, move_made
    
    global Bischop_B_1_x, Bischop_B_1_y, Bischop_B_2_x, Bischop_B_2_y, First_Bischop_B_1, First_Bischop_B_2
    global Horse_B_1_x, Horse_B_1_y, Horse_B_2_x, Horse_B_2_y, First_Horse_B_1, First_Horse_B_2
    global Rook_B_1_x, Rook_B_1_y, Rook_B_2_x, Rook_B_2_y, First_Rook_B_1, First_Rook_B_2
    global King_B_x, King_B_y, First_King_B
    global Queen_B_x, Queen_B_y, First_Queen_B
    global Pawn_B_1_x, Pawn_B_1_y, Pawn_B_2_x, Pawn_B_2_y, Pawn_B_3_x, Pawn_B_3_y, Pawn_B_4_x, Pawn_B_4_y, Pawn_B_5_x, Pawn_B_5_y, Pawn_B_6_x, Pawn_B_6_y, Pawn_B_7_x, Pawn_B_7_y, Pawn_B_8_x, Pawn_B_8_y
    global First_Pawn_B_1, First_Pawn_B_2, First_Pawn_B_3, First_Pawn_B_4, First_Pawn_B_5, First_Pawn_B_6, First_Pawn_B_7, First_Pawn_B_8

    global Bischop_W_1_x, Bischop_W_1_y, Bischop_W_2_x, Bischop_W_2_y, First_Bischop_W_1, First_Bischop_W_2
    global Horse_W_1_x, Horse_W_1_y, Horse_W_2_x, Horse_W_2_y, First_Horse_W_1, First_Horse_W_2
    global Rook_W_1_x, Rook_W_1_y, Rook_W_2_x, Rook_W_2_y, First_Rook_W_1, First_Rook_W_2
    global King_W_x, King_W_y, First_King_W
    global Queen_W_x, Queen_W_y, First_Queen_W
    global Pawn_W_1_x, Pawn_W_1_y, Pawn_W_2_x, Pawn_W_2_y, Pawn_W_3_x, Pawn_W_3_y, Pawn_W_4_x, Pawn_W_4_y, Pawn_W_5_x, Pawn_W_5_y, Pawn_W_6_x, Pawn_W_6_y, Pawn_W_7_x, Pawn_W_7_y, Pawn_W_8_x, Pawn_W_8_y
    global First_Pawn_W_1, First_Pawn_W_2, First_Pawn_W_3, First_Pawn_W_4, First_Pawn_W_5, First_Pawn_W_6, First_Pawn_W_7, First_Pawn_W_8



    if move_made == 1:

        if First_Bischop_B_1 == 3 and Captured_Bischop_B_1 == 0:
            win.blit(Bischop_B, (Bischop_B_1_x, Bischop_B_1_y))
        else:
            win.blit(Bischop_B, (1000, 0))
        
        if First_Bischop_B_2 == 3 and Captured_Bischop_B_2 == 0:
            win.blit(Bischop_B, (Bischop_B_2_x, Bischop_B_2_y))
        else:
            win.blit(Bischop_B, (1000, 0))
#--------------
        if First_Horse_B_1 == 3 and Captured_Horse_B_1 == 0:
            win.blit(Horse_B, (Horse_B_1_x, Horse_B_1_y))
        else:
            win.blit(Horse_B, (1000, 0))
        
        if First_Horse_B_2 == 3 and Captured_Horse_B_2 == 0:
            win.blit(Horse_B, (Horse_B_2_x, Horse_B_2_y))
        else:
            win.blit(Horse_B, (1000, 0))
#--------------
        if First_Rook_B_1 == 3 and Captured_Rook_B_1 == 0:
            win.blit(Rook_B, (Rook_B_1_x, Rook_B_1_y))
        else:
            win.blit(Rook_B, (1000, 0))
        
        if First_Rook_B_2 == 3 and Captured_Rook_B_2 == 0:
            win.blit(Rook_B, (Rook_B_2_x, Rook_B_2_y))
        else:
            win.blit(Rook_B, (1000, 0))
#--------------
        if First_King_B == 3 and Captured_King_B == 0:
            win.blit(King_B, (King_B_x, King_B_y))
        else:
            win.blit(King_B, (1000, 0))
#--------------
        if First_Queen_B == 3 and Captured_Queen_B == 0:
            win.blit(Queen_B, (Queen_B_x, Queen_B_y))
        else:
            win.blit(Queen_B, (1000, 0))
#--------------
        if First_Pawn_B_1 == 3 and Captured_Pawn_B_1 == 0:
            win.blit(Pawn_B, (Pawn_B_1_x, Pawn_B_1_y))
        else:
            win.blit(Pawn_B, (1000, 0))
        
        if First_Pawn_B_2 == 3 and Captured_Pawn_B_2 == 0:
            win.blit(Pawn_B, (Pawn_B_2_x, Pawn_B_2_y))
        else:
            win.blit(Pawn_B, (1000, 0))
        
        if First_Pawn_B_3 == 3 and Captured_Pawn_B_3 == 0:
            win.blit(Pawn_B, (Pawn_B_3_x, Pawn_B_3_y))
        else:
            win.blit(Pawn_B, (1000, 0))
        
        if First_Pawn_B_4 == 3 and Captured_Pawn_B_4 == 0:
            win.blit(Pawn_B, (Pawn_B_4_x, Pawn_B_4_y))
        else:
            win.blit(Pawn_B, (1000, 0))
        
        if First_Pawn_B_5 == 3 and Captured_Pawn_B_5 == 0:
            win.blit(Pawn_B, (Pawn_B_5_x, Pawn_B_5_y))
        else:
            win.blit(Pawn_B, (1000, 0))
        
        if First_Pawn_B_6 == 3 and Captured_Pawn_B_6 == 0:
            win.blit(Pawn_B, (Pawn_B_6_x, Pawn_B_6_y))
        else:
            win.blit(Pawn_B, (1000, 0))
        
        if First_Pawn_B_7 == 3 and Captured_Pawn_B_7 == 0:
            win.blit(Pawn_B, (Pawn_B_7_x, Pawn_B_7_y))
        else:
            win.blit(Pawn_B, (1000, 0))
        
        if First_Pawn_B_8 == 3 and Captured_Pawn_B_8 == 0:
            win.blit(Pawn_B, (Pawn_B_8_x, Pawn_B_8_y))
        else:
            win.blit(Pawn_B, (1000, 0))

#------------------------------------------------------------------------

        if First_Bischop_W_1 == 3 and Captured_Bischop_W_1 == 0:
            win.blit(Bischop_W, (Bischop_W_1_x, Bischop_W_1_y))
        else:
            win.blit(Bischop_W, (1000, 0))
        
        if First_Bischop_W_2 == 3 and Captured_Bischop_W_2 == 0:
            win.blit(Bischop_W, (Bischop_W_2_x, Bischop_W_2_y))
        else:
            win.blit(Bischop_W, (1000, 0))
#--------------
        if First_Horse_W_1 == 3 and Captured_Horse_W_1 == 0:
            win.blit(Horse_W, (Horse_W_1_x, Horse_W_1_y))
        else:
            win.blit(Horse_W, (1000, 0))
        
        if First_Horse_W_2 == 3 and Captured_Horse_W_2 == 0:
            win.blit(Horse_W, (Horse_W_2_x, Horse_W_2_y))
        else:
            win.blit(Horse_W, (1000, 0))
#--------------
        if First_Rook_W_1 == 3 and Captured_Rook_W_1 == 0:
            win.blit(Rook_W, (Rook_W_1_x, Rook_W_1_y))
        else:
            win.blit(Rook_W, (1000, 0))
        
        if First_Rook_W_2 == 3 and Captured_Rook_W_2 == 0:
            win.blit(Rook_W, (Rook_W_2_x, Rook_W_2_y))
        else:
            win.blit(Rook_W, (1000, 0))
#--------------
        if First_King_W == 3 and Captured_King_W == 0:
            win.blit(King_W, (King_W_x, King_W_y))
        else:
            win.blit(King_W, (1000, 0))
#--------------
        if First_Queen_W == 3 and Captured_Queen_W == 0:
            win.blit(Queen_W, (Queen_W_x, Queen_W_y))
        else:
            win.blit(Queen_W, (1000, 0))
#--------------
        if First_Pawn_W_1 == 3 and Captured_Pawn_W_1 == 0:
            win.blit(Pawn_W, (Pawn_W_1_x, Pawn_W_1_y))
        else:
            win.blit(Pawn_W, (1000, 0))
        
        if First_Pawn_W_2 == 3 and Captured_Pawn_W_2 == 0:
            win.blit(Pawn_W, (Pawn_W_2_x, Pawn_W_2_y))
        else:
            win.blit(Pawn_W, (1000, 0))
        
        if First_Pawn_W_3 == 3 and Captured_Pawn_W_3 == 0:
            win.blit(Pawn_W, (Pawn_W_3_x, Pawn_W_3_y))
        else:
            win.blit(Pawn_W, (1000, 0))
        
        if First_Pawn_W_4 == 3 and Captured_Pawn_W_4 == 0:
            win.blit(Pawn_W, (Pawn_W_4_x, Pawn_W_4_y))
        else:
            win.blit(Pawn_W, (1000, 0))
        
        if First_Pawn_W_5 == 3 and Captured_Pawn_W_5 == 0:
            win.blit(Pawn_W, (Pawn_W_5_x, Pawn_W_5_y))
        else:
            win.blit(Pawn_W, (1000, 0))
        
        if First_Pawn_W_6 == 3 and Captured_Pawn_W_6 == 0:
            win.blit(Pawn_W, (Pawn_W_6_x, Pawn_W_6_y))
        else:
            win.blit(Pawn_W, (1000, 0))
        
        if First_Pawn_W_7 == 3 and Captured_Pawn_W_7 == 0:
            win.blit(Pawn_W, (Pawn_W_7_x, Pawn_W_7_y))
        else:
            win.blit(Pawn_W, (1000, 0))
        
        if First_Pawn_W_8 == 3 and Captured_Pawn_W_8 == 0:
            win.blit(Pawn_W, (Pawn_W_8_x, Pawn_W_8_y))
        else:
            win.blit(Pawn_W, (1000, 0))




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

    if First_Horse_B_1 == 0:
        lst_Horse_B_1.append(win.blit(Horse_B, (coords[1])))
        Horse_B_1_x, Horse_B_1_y = coords[1][0], coords[1][1]
    
    if First_Horse_B_1 == 2:
        lst_Horse_B_1[0] = win.blit(Horse_B, (clicked_square_x, clicked_square_y))
        Horse_B_1_x, Horse_B_1_y = clicked_square_x, clicked_square_y

    if First_Horse_B_2 == 0:
        lst_Horse_B_2.append(win.blit(Horse_B, (coords[6])))
        Horse_B_2_x, Horse_B_2_y = coords[6][0], coords[6][1]

    if First_Horse_B_2 == 2:
        lst_Horse_B_2[0] = win.blit(Horse_B, (clicked_square_x, clicked_square_y))
        Horse_B_2_x, Horse_B_2_y = clicked_square_x, clicked_square_y
    
    if First_Rook_B_1 == 0:
        lst_Rook_B_1.append(win.blit(Rook_B, (coords[0])))
        Rook_B_1_x, Rook_B_1_y = coords[0][0], coords[0][1]
    
    if First_Rook_B_1 == 2:
        lst_Rook_B_1[0] = win.blit(Rook_B, (clicked_square_x, clicked_square_y))
        Rook_B_1_x, Rook_B_1_y = clicked_square_x, clicked_square_y

    if First_Rook_B_2 == 0:
        lst_Rook_B_2.append(win.blit(Rook_B, (coords[7])))
        Rook_B_2_x, Rook_B_2_y = coords[7][0], coords[7][1]

    if First_Rook_B_2 == 2:
        lst_Rook_B_2[0] = win.blit(Rook_B, (clicked_square_x, clicked_square_y))
        Rook_B_2_x, Rook_B_2_y = clicked_square_x, clicked_square_y


    if First_King_B == 0:
        lst_King_B.append(win.blit(King_B, (coords[4])))
        King_B_x, King_B_y = coords[4][0], coords[4][1]
    
    if First_King_B == 2:
        lst_King_B[0] = win.blit(King_B, (clicked_square_x, clicked_square_y))
        King_B_x, King_B_y = clicked_square_x, clicked_square_y

    if First_Queen_B == 0:
        lst_Queen_B.append(win.blit(Queen_B, (coords[3])))
        Queen_B_x, Queen_B_y = coords[3][0], coords[3][1]

    if First_Queen_B == 2:
        lst_Queen_B[0] = win.blit(Queen_B, (clicked_square_x, clicked_square_y))
        Queen_B_x, Queen_B_y = clicked_square_x, clicked_square_y

    


    if First_Pawn_B_1 == 0:
        lst_Pawn_B_1.append(win.blit(Pawn_B, (coords[8])))
        Pawn_B_1_x, Pawn_B_1_y = coords[8][0], coords[8][1]
    
    if First_Pawn_B_1 == 2:
        lst_Pawn_B_1[0] = win.blit(Pawn_B, (clicked_square_x, clicked_square_y))
        Pawn_B_1_x, Pawn_B_1_y = clicked_square_x, clicked_square_y

    if First_Pawn_B_2 == 0:
        lst_Pawn_B_2.append(win.blit(Pawn_B, (coords[9])))
        Pawn_B_2_x, Pawn_B_2_y = coords[9][0], coords[9][1]

    if First_Pawn_B_2 == 2:
        lst_Pawn_B_2[0] = win.blit(Pawn_B, (clicked_square_x, clicked_square_y))
        Pawn_B_2_x, Pawn_B_2_y = clicked_square_x, clicked_square_y

    if First_Pawn_B_3 == 0:
        lst_Pawn_B_3.append(win.blit(Pawn_B, (coords[10])))
        Pawn_B_3_x, Pawn_B_3_y = coords[10][0], coords[10][1]
    
    if First_Pawn_B_3 == 2:
        lst_Pawn_B_3[0] = win.blit(Pawn_B, (clicked_square_x, clicked_square_y))
        Pawn_B_3_x, Pawn_B_3_y = clicked_square_x, clicked_square_y

    if First_Pawn_B_4 == 0:
        lst_Pawn_B_4.append(win.blit(Pawn_B, (coords[11])))
        Pawn_B_4_x, Pawn_B_4_y = coords[11][0], coords[11][1]

    if First_Pawn_B_4 == 2:
        lst_Pawn_B_4[0] = win.blit(Pawn_B, (clicked_square_x, clicked_square_y))
        Pawn_B_4_x, Pawn_B_4_y = clicked_square_x, clicked_square_y

    if First_Pawn_B_5 == 0:
        lst_Pawn_B_5.append(win.blit(Pawn_B, (coords[12])))
        Pawn_B_5_x, Pawn_B_5_y = coords[12][0], coords[12][1]
    
    if First_Pawn_B_5 == 2:
        lst_Pawn_B_5[0] = win.blit(Pawn_B, (clicked_square_x, clicked_square_y))
        Pawn_B_5_x, Pawn_B_5_y = clicked_square_x, clicked_square_y

    if First_Pawn_B_6 == 0:
        lst_Pawn_B_6.append(win.blit(Pawn_B, (coords[13])))
        Pawn_B_6_x, Pawn_B_6_y = coords[13][0], coords[13][1]

    if First_Pawn_B_6 == 2:
        lst_Pawn_B_6[0] = win.blit(Pawn_B, (clicked_square_x, clicked_square_y))
        Pawn_B_6_x, Pawn_B_6_y = clicked_square_x, clicked_square_y

    if First_Pawn_B_7 == 0:
        lst_Pawn_B_7.append(win.blit(Pawn_B, (coords[14])))
        Pawn_B_7_x, Pawn_B_7_y = coords[14][0], coords[14][1]
    
    if First_Pawn_B_7 == 2:
        lst_Pawn_B_7[0] = win.blit(Pawn_B, (clicked_square_x, clicked_square_y))
        Pawn_B_7_x, Pawn_B_7_y = clicked_square_x, clicked_square_y

    if First_Pawn_B_8 == 0:
        lst_Pawn_B_8.append(win.blit(Pawn_B, (coords[15])))
        Pawn_B_8_x, Pawn_B_8_y = coords[15][0], coords[15][1]

    if First_Pawn_B_8 == 2:
        lst_Pawn_B_8[0] = win.blit(Pawn_B, (clicked_square_x, clicked_square_y))
        Pawn_B_8_x, Pawn_B_8_y = clicked_square_x, clicked_square_y

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

    if First_Horse_W_1 == 0:
        lst_Horse_W_1.append(win.blit(Horse_W, (coords[57])))
        Horse_W_1_x, Horse_W_1_y = coords[57][0], coords[57][1]
    
    if First_Horse_W_1 == 2:
        lst_Horse_W_1[0] = win.blit(Horse_W, (clicked_square_x, clicked_square_y))
        Horse_W_1_x, Horse_W_1_y = clicked_square_x, clicked_square_y

    if First_Horse_W_2 == 0:
        lst_Horse_W_2.append(win.blit(Horse_W, (coords[62])))
        Horse_W_2_x, Horse_W_2_y = coords[62][0], coords[62][1]

    if First_Horse_W_2 == 2:
        lst_Horse_W_2[0] = win.blit(Horse_W, (clicked_square_x, clicked_square_y))
        Horse_W_2_x, Horse_W_2_y = clicked_square_x, clicked_square_y
    
    if First_Rook_W_1 == 0:
        lst_Rook_W_1.append(win.blit(Rook_W, (coords[56])))
        Rook_W_1_x, Rook_W_1_y = coords[56][0], coords[56][1]
    
    if First_Rook_W_1 == 2:
        lst_Rook_W_1[0] = win.blit(Rook_W, (clicked_square_x, clicked_square_y))
        Rook_W_1_x, Rook_W_1_y = clicked_square_x, clicked_square_y

    if First_Rook_W_2 == 0:
        lst_Rook_W_2.append(win.blit(Rook_W, (coords[63])))
        Rook_W_2_x, Rook_W_2_y = coords[63][0], coords[63][1]

    if First_Rook_W_2 == 2:
        lst_Rook_W_2[0] = win.blit(Rook_W, (clicked_square_x, clicked_square_y))
        Rook_W_2_x, Rook_W_2_y = clicked_square_x, clicked_square_y


    if First_King_W == 0:
        lst_King_W.append(win.blit(King_W, (coords[60])))
        King_W_x, King_W_y = coords[60][0], coords[60][1]
    
    if First_King_W == 2:
        lst_King_W[0] = win.blit(King_W, (clicked_square_x, clicked_square_y))
        King_W_x, King_W_y = clicked_square_x, clicked_square_y

    if First_Queen_W == 0:
        lst_Queen_W.append(win.blit(Queen_W, (coords[59])))
        Queen_W_x, Queen_W_y = coords[59][0], coords[59][1]

    if First_Queen_W == 2:
        lst_Queen_W[0] = win.blit(Queen_W, (clicked_square_x, clicked_square_y))
        Queen_W_x, Queen_W_y = clicked_square_x, clicked_square_y

    


    if First_Pawn_W_1 == 0:
        lst_Pawn_W_1.append(win.blit(Pawn_W, (coords[48])))
        Pawn_W_1_x, Pawn_W_1_y = coords[48][0], coords[48][1]
    
    if First_Pawn_W_1 == 2:
        lst_Pawn_W_1[0] = win.blit(Pawn_W, (clicked_square_x, clicked_square_y))
        Pawn_W_1_x, Pawn_W_1_y = clicked_square_x, clicked_square_y

    if First_Pawn_W_2 == 0:
        lst_Pawn_W_2.append(win.blit(Pawn_W, (coords[49])))
        Pawn_W_2_x, Pawn_W_2_y = coords[49][0], coords[49][1]

    if First_Pawn_W_2 == 2:
        lst_Pawn_W_2[0] = win.blit(Pawn_W, (clicked_square_x, clicked_square_y))
        Pawn_W_2_x, Pawn_W_2_y = clicked_square_x, clicked_square_y

    if First_Pawn_W_3 == 0:
        lst_Pawn_W_3.append(win.blit(Pawn_W, (coords[50])))
        Pawn_W_3_x, Pawn_W_3_y = coords[50][0], coords[50][1]
    
    if First_Pawn_W_3 == 2:
        lst_Pawn_W_3[0] = win.blit(Pawn_W, (clicked_square_x, clicked_square_y))
        Pawn_W_3_x, Pawn_W_3_y = clicked_square_x, clicked_square_y

    if First_Pawn_W_4 == 0:
        lst_Pawn_W_4.append(win.blit(Pawn_W, (coords[51])))
        Pawn_W_4_x, Pawn_W_4_y = coords[51][0], coords[51][1]

    if First_Pawn_W_4 == 2:
        lst_Pawn_W_4[0] = win.blit(Pawn_W, (clicked_square_x, clicked_square_y))
        Pawn_W_4_x, Pawn_W_4_y = clicked_square_x, clicked_square_y

    if First_Pawn_W_5 == 0:
        lst_Pawn_W_5.append(win.blit(Pawn_W, (coords[52])))
        Pawn_W_5_x, Pawn_W_5_y = coords[52][0], coords[52][1]
    
    if First_Pawn_W_5 == 2:
        lst_Pawn_W_5[0] = win.blit(Pawn_W, (clicked_square_x, clicked_square_y))
        Pawn_W_5_x, Pawn_W_5_y = clicked_square_x, clicked_square_y

    if First_Pawn_W_6 == 0:
        lst_Pawn_W_6.append(win.blit(Pawn_W, (coords[53])))
        Pawn_W_6_x, Pawn_W_6_y = coords[53][0], coords[53][1]

    if First_Pawn_W_6 == 2:
        lst_Pawn_W_6[0] = win.blit(Pawn_W, (clicked_square_x, clicked_square_y))
        Pawn_W_6_x, Pawn_W_6_y = clicked_square_x, clicked_square_y

    if First_Pawn_W_7 == 0:
        lst_Pawn_W_7.append(win.blit(Pawn_W, (coords[54])))
        Pawn_W_7_x, Pawn_W_7_y = coords[54][0], coords[54][1]
    
    if First_Pawn_W_7 == 2:
        lst_Pawn_W_7[0] = win.blit(Pawn_W, (clicked_square_x, clicked_square_y))
        Pawn_W_7_x, Pawn_W_7_y = clicked_square_x, clicked_square_y

    if First_Pawn_W_8 == 0:
        lst_Pawn_W_8.append(win.blit(Pawn_W, (coords[55])))
        Pawn_W_8_x, Pawn_W_8_y = coords[55][0], coords[55][1]

    if First_Pawn_W_8 == 2:
        lst_Pawn_W_8[0] = win.blit(Pawn_W, (clicked_square_x, clicked_square_y))
        Pawn_W_8_x, Pawn_W_8_y = clicked_square_x, clicked_square_y

    First_Bischop_B_1 = 3
    First_Bischop_B_2 = 3
    First_Horse_B_1 = 3
    First_Horse_B_2 = 3
    First_Rook_B_1 = 3
    First_Rook_B_2 = 3
    First_King_B = 3
    First_King_W = 3
    First_Queen_B = 3
    First_Queen_W = 3
    First_Pawn_B_1 = 3
    First_Pawn_B_2 = 3
    First_Pawn_B_3 = 3
    First_Pawn_B_4 = 3
    First_Pawn_B_5 = 3
    First_Pawn_B_6 = 3
    First_Pawn_B_7 = 3
    First_Pawn_B_8 = 3

    First_Bischop_W_1 = 3
    First_Bischop_W_2 = 3
    First_Horse_W_1 = 3
    First_Horse_W_2 = 3
    First_Rook_W_1 = 3
    First_Rook_W_2 = 3
    First_King_W = 3
    First_King_W = 3
    First_Queen_W = 3
    First_Queen_W = 3
    First_Pawn_W_1 = 3
    First_Pawn_W_2 = 3
    First_Pawn_W_3 = 3
    First_Pawn_W_4 = 3
    First_Pawn_W_5 = 3
    First_Pawn_W_6 = 3
    First_Pawn_W_7 = 3
    First_Pawn_W_8 = 3
    
    
    move_made = 0

    pygame.display.update()

def main():
    global p, x, y, move_made
    
    global First_Bischop_B_1, First_Bischop_B_2
    global First_Horse_B_1, First_Horse_B_2
    global First_Rook_B_1, First_Rook_B_2
    global First_King_B, First_Queen_B
    global First_Pawn_B_1, First_Pawn_B_2, First_Pawn_B_3, First_Pawn_B_4, First_Pawn_B_5, First_Pawn_B_6, First_Pawn_B_7, First_Pawn_B_8

    global First_Bischop_W_1, First_Bischop_W_2
    global First_Horse_W_1, First_Horse_W_2
    global First_Rook_W_1, First_Rook_W_2
    global First_King_W, First_Queen_W
    global First_Pawn_W_1, First_Pawn_W_2, First_Pawn_W_3, First_Pawn_W_4, First_Pawn_W_5, First_Pawn_W_6, First_Pawn_W_7, First_Pawn_W_8

    aantalKliksBischop_B_1 = 0
    aantalKliksBischop_B_2 = 0
    aantalKliksHorse_B_1 = 0
    aantalKliksHorse_B_2 = 0
    aantalKliksRook_B_1 = 0
    aantalKliksRook_B_2 = 0

    aantalKliksKing_B = 0
    aantalKliksQueen_B = 0

    aantalKliksPawn_B_1 = 0
    aantalKliksPawn_B_2 = 0
    aantalKliksPawn_B_3 = 0
    aantalKliksPawn_B_4 = 0
    aantalKliksPawn_B_5 = 0
    aantalKliksPawn_B_6 = 0
    aantalKliksPawn_B_7 = 0
    aantalKliksPawn_B_8 = 0


    aantalKliksBischop_W_1 = 0
    aantalKliksBischop_W_2 = 0
    aantalKliksHorse_W_1 = 0
    aantalKliksHorse_W_2 = 0
    aantalKliksRook_W_1 = 0
    aantalKliksRook_W_2 = 0

    aantalKliksKing_W = 0
    aantalKliksQueen_W = 0

    aantalKliksPawn_W_1 = 0
    aantalKliksPawn_W_2 = 0
    aantalKliksPawn_W_3 = 0
    aantalKliksPawn_W_4 = 0
    aantalKliksPawn_W_5 = 0
    aantalKliksPawn_W_6 = 0
    aantalKliksPawn_W_7 = 0
    aantalKliksPawn_W_8 = 0

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
                    aantalKliksBischop_B_1 += 1
                elif aantalKliksBischop_B_1 == 1:
                    aantalKliksBischop_B_1 = 0
                    Clicked()
                    First_Bischop_B_1 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Bischop_B_2):
                    aantalKliksBischop_B_2 += 1
                elif aantalKliksBischop_B_2 == 1:
                    aantalKliksBischop_B_2 = 0
                    Clicked()
                    First_Bischop_B_2 = 2
                    move_made = 1
                    draw_board()


                if any(rect.collidepoint(x, y) for rect in lst_Horse_B_1):
                    aantalKliksHorse_B_1 += 1
                elif aantalKliksHorse_B_1 == 1:
                    aantalKliksHorse_B_1 = 0
                    Clicked()
                    First_Horse_B_1 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Horse_B_2):
                    aantalKliksHorse_B_2 += 1
                elif aantalKliksHorse_B_2 == 1:
                    aantalKliksHorse_B_2 = 0
                    Clicked()
                    First_Horse_B_2 = 2
                    move_made = 1
                    draw_board()


                if any(rect.collidepoint(x, y) for rect in lst_Rook_B_1):
                    aantalKliksRook_B_1 += 1
                elif aantalKliksRook_B_1 == 1:
                    aantalKliksRook_B_1 = 0
                    Clicked()
                    First_Rook_B_1 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Rook_B_2):
                    aantalKliksRook_B_2 += 1
                elif aantalKliksRook_B_2 == 1:
                    aantalKliksRook_B_2 = 0
                    Clicked()
                    First_Rook_B_2 = 2
                    move_made = 1
                    draw_board()

                if any(rect.collidepoint(x, y) for rect in lst_King_B):
                    aantalKliksKing_B += 1
                elif aantalKliksKing_B == 1:
                    aantalKliksKing_B = 0
                    Clicked()
                    First_King_B = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Queen_B):
                    aantalKliksQueen_B += 1
                elif aantalKliksQueen_B == 1:
                    aantalKliksQueen_B = 0
                    Clicked()
                    First_Queen_B = 2
                    move_made = 1
                    draw_board()


                if any(rect.collidepoint(x, y) for rect in lst_Pawn_B_1):
                    aantalKliksPawn_B_1 += 1
                elif aantalKliksPawn_B_1 == 1:
                    aantalKliksPawn_B_1 = 0
                    Clicked()
                    First_Pawn_B_1 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Pawn_B_2):
                    aantalKliksPawn_B_2 += 1
                elif aantalKliksPawn_B_2 == 1:
                    aantalKliksPawn_B_2 = 0
                    Clicked()
                    First_Pawn_B_2 = 2
                    move_made = 1
                    draw_board()

                if any(rect.collidepoint(x, y) for rect in lst_Pawn_B_3):
                    aantalKliksPawn_B_3 += 1
                elif aantalKliksPawn_B_3 == 1:
                    aantalKliksPawn_B_3 = 0
                    Clicked()
                    First_Pawn_B_3 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Pawn_B_4):
                    aantalKliksPawn_B_4 += 1
                elif aantalKliksPawn_B_4 == 1:
                    aantalKliksPawn_B_4 = 0
                    Clicked()
                    First_Pawn_B_4 = 2
                    move_made = 1
                    draw_board()

                if any(rect.collidepoint(x, y) for rect in lst_Pawn_B_5):
                    aantalKliksPawn_B_5 += 1
                elif aantalKliksPawn_B_5 == 1:
                    aantalKliksPawn_B_5 = 0
                    Clicked()
                    First_Pawn_B_5 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Pawn_B_6):
                    aantalKliksPawn_B_6 += 1
                elif aantalKliksPawn_B_6 == 1:
                    aantalKliksPawn_B_6 = 0
                    Clicked()
                    First_Pawn_B_6 = 2
                    move_made = 1
                    draw_board()

                if any(rect.collidepoint(x, y) for rect in lst_Pawn_B_7):
                    aantalKliksPawn_B_7 += 1
                elif aantalKliksPawn_B_7 == 1:
                    aantalKliksPawn_B_7 = 0
                    Clicked()
                    First_Pawn_B_7 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Pawn_B_8):
                    aantalKliksPawn_B_8 += 1
                elif aantalKliksPawn_B_8 == 1:
                    aantalKliksPawn_B_8 = 0
                    Clicked()
                    First_Pawn_B_8 = 2
                    move_made = 1
                    draw_board()

#--------------------------------------------------------------------------------------------------------------
                if any(rect.collidepoint(x, y) for rect in lst_Bischop_W_1):
                    aantalKliksBischop_W_1 += 1
                elif aantalKliksBischop_W_1 == 1:
                    aantalKliksBischop_W_1 = 0
                    Clicked()
                    First_Bischop_W_1 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Bischop_W_2):
                    aantalKliksBischop_W_2 += 1
                elif aantalKliksBischop_W_2 == 1:
                    aantalKliksBischop_W_2 = 0
                    Clicked()
                    First_Bischop_W_2 = 2
                    move_made = 1
                    draw_board()


                if any(rect.collidepoint(x, y) for rect in lst_Horse_W_1):
                    aantalKliksHorse_W_1 += 1
                elif aantalKliksHorse_W_1 == 1:
                    aantalKliksHorse_W_1 = 0
                    Clicked()
                    First_Horse_W_1 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Horse_W_2):
                    aantalKliksHorse_W_2 += 1
                elif aantalKliksHorse_W_2 == 1:
                    aantalKliksHorse_W_2 = 0
                    Clicked()
                    First_Horse_W_2 = 2
                    move_made = 1
                    draw_board()


                if any(rect.collidepoint(x, y) for rect in lst_Rook_W_1):
                    aantalKliksRook_W_1 += 1
                elif aantalKliksRook_W_1 == 1:
                    aantalKliksRook_W_1 = 0
                    Clicked()
                    First_Rook_W_1 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Rook_W_2):
                    aantalKliksRook_W_2 += 1
                elif aantalKliksRook_W_2 == 1:
                    aantalKliksRook_W_2 = 0
                    Clicked()
                    First_Rook_W_2 = 2
                    move_made = 1
                    draw_board()

                if any(rect.collidepoint(x, y) for rect in lst_King_W):
                    aantalKliksKing_W += 1
                elif aantalKliksKing_W == 1:
                    aantalKliksKing_W = 0
                    Clicked()
                    First_King_W = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Queen_W):
                    aantalKliksQueen_W += 1
                elif aantalKliksQueen_W == 1:
                    aantalKliksQueen_W = 0
                    Clicked()
                    First_Queen_W = 2
                    move_made = 1
                    draw_board()


                if any(rect.collidepoint(x, y) for rect in lst_Pawn_W_1):
                    aantalKliksPawn_W_1 += 1
                elif aantalKliksPawn_W_1 == 1:
                    aantalKliksPawn_W_1 = 0
                    Clicked()
                    First_Pawn_W_1 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Pawn_W_2):
                    aantalKliksPawn_W_2 += 1
                elif aantalKliksPawn_W_2 == 1:
                    aantalKliksPawn_W_2 = 0
                    Clicked()
                    First_Pawn_W_2 = 2
                    move_made = 1
                    draw_board()

                if any(rect.collidepoint(x, y) for rect in lst_Pawn_W_3):
                    aantalKliksPawn_W_3 += 1
                elif aantalKliksPawn_W_3 == 1:
                    aantalKliksPawn_W_3 = 0
                    Clicked()
                    First_Pawn_W_3 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Pawn_W_4):
                    aantalKliksPawn_W_4 += 1
                elif aantalKliksPawn_W_4 == 1:
                    aantalKliksPawn_W_4 = 0
                    Clicked()
                    First_Pawn_W_4 = 2
                    move_made = 1
                    draw_board()

                if any(rect.collidepoint(x, y) for rect in lst_Pawn_W_5):
                    aantalKliksPawn_W_5 += 1
                elif aantalKliksPawn_W_5 == 1:
                    aantalKliksPawn_W_5 = 0
                    Clicked()
                    First_Pawn_W_5 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Pawn_W_6):
                    aantalKliksPawn_W_6 += 1
                elif aantalKliksPawn_W_6 == 1:
                    aantalKliksPawn_W_6 = 0
                    Clicked()
                    First_Pawn_W_6 = 2
                    move_made = 1
                    draw_board()

                if any(rect.collidepoint(x, y) for rect in lst_Pawn_W_7):
                    aantalKliksPawn_W_7 += 1
                elif aantalKliksPawn_W_7 == 1:
                    aantalKliksPawn_W_7 = 0
                    Clicked()
                    First_Pawn_W_7 = 2
                    move_made = 1
                    draw_board()
                    
                if any(rect.collidepoint(x, y) for rect in lst_Pawn_W_8):
                    aantalKliksPawn_W_8 += 1
                elif aantalKliksPawn_W_8 == 1:
                    aantalKliksPawn_W_8 = 0
                    Clicked()
                    First_Pawn_W_8 = 2
                    move_made = 1
                    draw_board()

        draw_window()

    pygame.quit()

draw_board()
main()