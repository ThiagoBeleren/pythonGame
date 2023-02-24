import pygame 
import sys

class Game(object):
    screen_width = 600
    screen_height = 600 
    
    
    def __init__(self):
        pygame.init()
        print("pygame has started ")

        self.clock = pygame.time.Clock()
        self.home_screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        
    def run(self):
        while True:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

    def quit(self):
        sys.exit()


game = Game()
game.run()