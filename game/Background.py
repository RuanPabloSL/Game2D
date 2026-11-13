import pygame

from game.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from game.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.smoothscale(self.surf, (WIN_WIDTH, WIN_HEIGHT))




    def move(self) -> None:
        self.rect.centerx -= ENTITY_SPEED.get(self.name, 0)
        if self.rect.right <=  0:
            self.rect.left = WIN_WIDTH
        
