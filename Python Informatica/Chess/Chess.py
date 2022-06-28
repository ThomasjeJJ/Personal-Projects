#Thomas Jansen
#thomas@ronmix.com

from cmath import rect
import pygame
import time
import os

pygame.init()

WIDTH, HEIGHT = 800, 660
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

cellSize = 80
FPS = 60
coords = []


# Colors
black = (0, 0, 0)
white = (255, 255, 255)
tile_black = (128, 0, 0)
tile_white = (255, 255, 255)
bg_grey = (48, 44, 52)

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


board = pygame.Surface((cellSize * 8, cellSize * 8))
pygame.Surface.fill(board, tile_black)

win.fill(bg_grey)
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


#Function for making the list of coordinates needed for the right placements
def list_maker():
    for x in range(0, 640, 80):
        for y in range(0, 640, 80):
            coords.append((80+x, 10+y))
    print(coords)

#function for displaying everything
def draw_window():
    win.blit(board, (80, 10))
    win.blit(Bischop_B, (90,20))

    pygame.display.update()

def main():
    #makes the game run at 60 fps so it doesnt use too many computer resources
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        draw_window()
    pygame.quit()

list_maker()
draw_board()
main()