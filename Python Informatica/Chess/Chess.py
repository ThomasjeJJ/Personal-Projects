#Thomas Jansen
#thomas@ronmix.com

from cmath import rect
from pydoc import cli
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
Pawn_B = pygame.image.load(os.path.join("Chess_Pieces","Pawn_B.png"))
Pawn_W = pygame.image.load(os.path.join("Chess_Pieces","Pawn_W.png"))
Queen_B = pygame.image.load(os.path.join("Chess_Pieces","Queen_B.png"))
Queen_W = pygame.image.load(os.path.join("Chess_Pieces","Queen_W.png"))
Rook_B = pygame.image.load(os.path.join("Chess_Pieces","Rook_B.png"))
Rook_W = pygame.image.load(os.path.join("Chess_Pieces","Rook_W.png"))

coords = []
coordsX = [90, 170, 250, 330, 410, 490, 570, 650]
coordsY = [20, 100, 180, 260, 340, 420, 500, 580]
#Function for making the list of coordinates needed for the right placements
def list_maker():
    for y in range(0, 640, 80):
        for x in range(0, 640, 80):
            coords.append((90+x, 20+y))


list_maker()

#variables
cellSize = 80
FPS = 60
p = 0
lst = []
First_Bischop_B = 0
x = 0
y = 0
aantalKliks = 0

clicked_square_x = 0
clicked_square_y = 0



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

#A nice border around the board
pygame.draw.rect(win, black, pygame.Rect(73, 3, cellSize * 8 + 14, cellSize * 8 + 14))

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


def Bishop_B_Clicked ():
    k = 0
    ClickedX = 0
    ClickedY = 0

    while ClickedX == 0:
        if coordsX[k] < x:
            k += 1
        else:
            ClickedX = 1
            f = coordsX[k-1]
            l = coordsX[k]
            n = x - f
            m = l - x
            if n >= m:
                clicked_square_x = k -1
            else:
                clicked_square_x = k
            print (coordsX[clicked_square_x])
    
    while ClickedY == 0:
        if coordsY[k] < x:
            k += 1
        else:
            ClickedY = 1
            f = coordsY[k-1]
            l = coordsY[k]
            n = x - f
            m = l - x
            if n >= m:
                clicked_square_y = k -1
            else:
                clicked_square_y = k
            print (coordsX[clicked_square_y])
            win.blit(Bischop_B, (350,350))
    
    

                
            



#function for displaying everything
def draw_window():
    global First_Bischop_B
    win.blit(board, (80, 10))
    
    if First_Bischop_B == 0:
        lst.append(win.blit(Bischop_B, (coords[p])))
        First_Bischop_B = 1
    lst[0] = win.blit(Bischop_B, (coords[p]))

    pygame.display.update()

def main():
    global p, x, y, aantalKliks

    #Clickerd_Bishop_B = 0

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
                if any(rect.collidepoint(x, y) for rect in lst):
                    print("gecklickt")
                    aantalKliks += 1
                elif aantalKliks == 1:
                    aantalKliks = 0
                    print("2e")
                    Bishop_B_Clicked()
                            

        draw_window()

    pygame.quit()




draw_board()
main()