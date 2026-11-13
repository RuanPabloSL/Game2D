import pygame
from pygame import Surface
from game.Entity import Entity
from game.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.window: Surface = window
        self.name: str = name
        self.game_mode= game_mode
        self.entity_list: list [Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LvL1'))




    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
