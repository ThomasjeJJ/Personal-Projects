#Thomas Jansen
#thomas@ronmix.com

import pygame
import time
import os

pygame.init()

WIDTH, HEIGHT = 800, 660
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

FPS = 60

bg_grey = (40, 36, 44)

test_block = pygame.image.load(os.path.join("Chess_Pieces","King_B.png"))
test_block = pygame.transform.scale(test_block, (80,80))

def draw_window():
    win.fill(bg_grey)
    win.blit(test_block, (150, 150))
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

main()