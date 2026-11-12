import pygame

from game.Const import WIN_HEIGHT, WIN_WIDTH
from game.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()

        pygame.mixer.init() # Initialize the mixer module for audio

        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Shooter Game") # Set the window title

        self.menu = Menu(self.window)
        self.clock = pygame.time.Clock()
        self.running = True


    def run(self):
        while self.running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

            self.menu.run()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()