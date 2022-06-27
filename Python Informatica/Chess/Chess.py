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

black = (0, 0, 0)
white = (255, 255, 255)
tile_black = (35, 28, 19)
tile_white = (226, 191, 128)
bg_grey = (40, 36, 44)


board = pygame.Surface((cellSize * 8, cellSize * 8))
pygame.Surface.fill(board, tile_black)

win.fill(bg_grey)
pygame.draw.rect(win, black, pygame.Rect(75, 5, cellSize * 8 + 10, cellSize * 8 + 10))

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


def draw_window():
    win.blit(board, (80, 10))

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        draw_window()
    pygame.quit()

draw_board()
main()