import random

from game.Enemy import Enemy
from game.Player import Player
from game.Background import Background
from game.Const import WIN_HEIGHT, WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'LvL1':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'LvL1BG{i}', (0, 0)))
                    list_bg.append(Background(f'LvL1BG{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return [Player('Player1', (10, WIN_HEIGHT // 2))]
            case 'Player2':
                return [Player('Player2', (10, WIN_HEIGHT // 2.5))]
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 90)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 90)))
            case _:
                raise ValueError(f"Entidade desconhecida: {entity_name}")
