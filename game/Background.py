import pygame

from game.Const import ENTITY_SPEED
from game.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        surface = pygame.display.get_surface()
        self.surf = pygame.transform.scale(self.surf, surface.get_size())
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = ENTITY_SPEED[name]




    def move(self) -> None:
        self.rect.centerx -= ENTITY_SPEED.get(self.name)
        if self.rect.right <=  0:
            self.rect.x = self.surf.get_width() * 2
        
