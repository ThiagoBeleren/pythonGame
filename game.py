import pygame 
import sys
from display import Display

class Game(object):
    print("class game has initiated")

    display = Display()

    ball = pygame.load.image("./beach_ball.png")
    ball_rect = ball.get_rect()

    display.screen.blit(ball, ball_rect)

    pygame.display.flip()

