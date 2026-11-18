import pygame

from game.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from game.Menu import Menu
from game.Level import Level


class Game:

    def __init__(self):
        pygame.init()

        pygame.mixer.init() # Initialize the mixer module for audio

        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.screen_size = (WIN_WIDTH, WIN_HEIGHT)
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
                scores = []
                level = Level(self.window, 'LvL1', menu_return, scores)
                level_return, scores = level.run(self.menu)
                if level_return is None:
                    continue
                if level_return:
                    level = Level(self.window, 'LvL2', menu_return, scores)
                    level_return, scores = level.run(self.menu)
                    if level_return is None:
                        continue
                self.menu = Menu(self.window)
            elif menu_return == MENU_OPTION[4]:
                new_size = self.menu.settings(self.screen_size)
                if new_size != self.screen_size:
                    self.screen_size = new_size
                    self.window = pygame.display.set_mode(size=self.screen_size)
                    self.menu = Menu(self.window)
            elif menu_return == MENU_OPTION[5]:
                pygame.quit()
                quit()
            else:
                pass


        
