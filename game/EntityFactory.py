import random
import pygame

from game.Enemy import Enemy
from game.Player import Player
from game.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'LvL1':
                list_bg = []
                width = pygame.display.get_surface().get_width()
                for i in range(7):
                    list_bg.append(Background(f'LvL1BG{i}', (0, 0)))
                    list_bg.append(Background(f'LvL1BG{i}', (width, 0)))
                return list_bg
            case 'LvL2':
                            list_bg = []
                            width = pygame.display.get_surface().get_width()
                            for i in range(5):
                                list_bg.append(Background(f'LvL2BG{i}', (0, 0)))
                                list_bg.append(Background(f'LvL2BG{i}', (width, 0)))
                            return list_bg
            case 'Player1':
                return [Player('Player1', (10, pygame.display.get_surface().get_height() // 2))]
            case 'Player2':
                return [Player('Player2', (10, pygame.display.get_surface().get_height() // 2.5))]
            case 'Enemy1':
                surface = pygame.display.get_surface()
                return Enemy('Enemy1', (surface.get_width() + 10, random.randint(50, surface.get_height() - 90)))
            case 'Enemy2':
                surface = pygame.display.get_surface()
                return Enemy('Enemy2', (surface.get_width() + 10, random.randint(50, surface.get_height() - 90)))
            case _:
                raise ValueError(f"Entidade desconhecida: {entity_name}")
