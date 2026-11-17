import pygame

from game.EnemyShot import EnemyShot
from game.Enemy import Enemy
from game.Entity import Entity
from game.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= pygame.display.get_surface().get_width():
                ent.health = 0
        if isinstance(ent, EnemyShot):
                    if ent.rect.left <= 0:
                        ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_area = entity_list[i]
            EntityMediator.__verify_collision_window(entity_area)


    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
import pygame

