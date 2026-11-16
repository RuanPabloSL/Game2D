import pygame

from game.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from game.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT)) #remover tlvz
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = ENTITY_SPEED[name]




    def move(self) -> None:
        self.rect.centerx -= ENTITY_SPEED.get(self.name)
        if self.rect.right <=  0:
            self.rect.x = WIN_WIDTH * 2
        
