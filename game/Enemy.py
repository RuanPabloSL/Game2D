
from game.Entity import Entity
from game.Const import ENTITY_SPEED, WIN_WIDTH


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self) -> None:
        self.rect.centerx -= ENTITY_SPEED.get(self.name)

        if self.rect.right <= 0:
            self.rect.x = WIN_WIDTH
