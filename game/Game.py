import pygame

from game.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from game.Menu import Menu
from game.Level import Level


class Game:

    def __init__(self):
        pygame.init()

        pygame.mixer.init() # Initialize the mixer module for audio

        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Game Shooter") # Set the window title

        self.menu = Menu(self.window)
        self.clock = pygame.time.Clock()
        self.running = True

        self.menu_option = 0
        

    def run(self):
        while self.running:
            menu_return = self.menu.run(self.menu_option)
        #action menu
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[5]:
                pygame.quit()
                quit()
            else:
                pass


        