#Thomas Jansen
#thomas@ronmix.com

import pygame
import os

pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

Light_Grey = (192,192,192)
Black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

VELOCITY = 3
MAX_VEL = 5

Vel_ball_x = 5
Vel_ball_y = 0

score_rood = 0
score_blauw = 0

BORDER = pygame.Rect(WIDTH/2 - 5, 60, 10, 440) 


FPS = 60

Blue_Block = pygame.image.load(os.path.join("Assets","Blue_Block.png"))
Blue_Block = pygame.transform.scale(Blue_Block, (25,90))
Red_Block = pygame.image.load(os.path.join("Assets","Red_Block.png"))
Red_Block = pygame.transform.scale(Red_Block, (25,90))
Ball = pygame.image.load(os.path.join("Assets","Ball.png"))
Ball = pygame.transform.scale(Ball, (30, 30))

font = pygame.font.Font('freesansbold.ttf', 20)


def draw_window(blue, red, ball):
    WIN.fill(Light_Grey)
    pygame.draw.rect(WIN, Black, BORDER)
    WIN.blit(Blue_Block, (blue.x, blue.y))
    WIN.blit(Red_Block, (red.x, red.y))
    WIN.blit(Ball, (ball.x, ball.y))
    text = font.render(f"Blauw heeft {score_blauw} punten en Rood heeft {score_rood} punten", True, (0, 0, 255))
    textRect = text.get_rect()
    textRect.center = (350, 20)
    WIN.blit(text, textRect)
    pygame.display.update()

def movement_blue(keys_pressed, blue):
    if keys_pressed[pygame.K_w] and blue.y - VELOCITY > 0: #omhoog
        blue.y -= VELOCITY
    if keys_pressed[pygame.K_s] and blue.y - VELOCITY < 420: #omlaag
        blue.y += VELOCITY

def movement_red(keys_pressed, red):
    if keys_pressed[pygame.K_i] and red.y - VELOCITY > 0: #omhoog
        red.y -= VELOCITY
    if keys_pressed[pygame.K_k] and red.y - VELOCITY < 420: #omlaag
        red.y += VELOCITY

def movement_ball(keys_pressed, ball, blue, red):
    global score_blauw, score_rood, Vel_ball_x, Vel_ball_y
    
    ball.x = ball.x + Vel_ball_x
    ball.y = ball.y + Vel_ball_y


    if ball.x < 0:
        score_rood += 1
        print(f"Blauw heeft {score_blauw} punten en Rood heeft {score_rood} punten")
        draw_window(blue, red, ball)
        Vel_ball_y = 0
        Vel_ball_x = Vel_ball_x * -1
        main()
    if ball.x > 670:
        score_blauw += 1
        print(f"Blauw heeft {score_blauw} punten en Rood heeft {score_rood} punten")
        draw_window(blue, red, ball)
        Vel_ball_y = 0
        Vel_ball_x = Vel_ball_x * -1
        main()
    
    if ball.y < 0:
        Vel_ball_y = Vel_ball_y * -1
    if ball.y > 470:
        Vel_ball_y = Vel_ball_y * -1


def collision (blue, red, ball):
    global Vel_ball_x, Vel_ball_y
    if blue.x + 25 > ball.x and blue.y < ball.y + 15 < blue.y + 30:
        Vel_ball_x = Vel_ball_x * -1
        Vel_ball_y = -5
    if blue.x + 25 > ball.x and blue.y + 30 < ball.y + 15 < blue.y + 60:
        Vel_ball_x = Vel_ball_x * -1
        Vel_ball_y = 0
    if blue.x + 25 > ball.x and blue.y + 60 < ball.y + 15 < blue.y + 90:
        Vel_ball_x = Vel_ball_x * -1
        Vel_ball_y = 5

    if red.x - 30 < ball.x and red.y < ball.y + 15 < red.y + 30:
        Vel_ball_x = Vel_ball_x * -1
        Vel_ball_y = -5
    if red.x - 30 < ball.x and red.y + 30 < ball.y + 15 < red.y + 60:
        Vel_ball_x = Vel_ball_x * -1
        Vel_ball_y = 0
    if red.x - 30 < ball.x and red.y + 60 < ball.y + 15 < red.y + 90:
        Vel_ball_x = Vel_ball_x * -1
        Vel_ball_y = 5



def main():
    blue = pygame.Rect(50, 210, 25, 90)
    red = pygame.Rect(650, 210, 25, 90)
    ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 10, 10)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        collision (blue, red, ball)
        movement_blue(keys_pressed, blue)
        movement_red(keys_pressed, red)
        movement_ball(keys_pressed, ball, blue, red)
        draw_window(blue, red, ball)

    pygame.quit()

main()