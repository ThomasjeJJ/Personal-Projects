#Thomas Jansen
#thomas@ronmix.com

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
bg_grey = (40, 36, 44)


board = pygame.Surface((cellSize * 8, cellSize * 8))
#Function for drawing the chess board
def draw_board():
    #loop for moving from row to row
    for x in range (0, 8, 2):
        #loop for the moving in the row
        for y in range (0, 8, 2):
            pygame.draw.rect(board, white, (x*cellSize, y*cellSize, 80, 80))
    
    for x in range (1, 8, 2):
        #loop for the moving in the row
        for y in range (1, 8, 2):
            pygame.draw.rect(board, white, (x*cellSize, y*cellSize, 80, 80))


def draw_window():
    win.fill(bg_grey)
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