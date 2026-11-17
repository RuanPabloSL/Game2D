import random
import pygame
import sys

from pygame import Font, Rect, Surface
from game.Const import COLOR_WHITE, EVENT_ENEMY, MENU_OPTION, SPAWN_TIME
from game.Enemy import Enemy
from game.Entity import Entity
from game.EntityFactory import EntityFactory
from game.EntityMediator import EntityMediator
from game.Player import Player


class Level:

    def __init__(self, window, name, game_mode):
        self.window: Surface = window
        self.name: str = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LvL1'))
        self.entity_list.extend(EntityFactory.get_entity('Player1'))
        self.timeout = 20000  # Timeout in milliseconds , 1000 = 1 second
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.extend(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # 2second

    def run(self, ):
        pygame.mixer.music.load('./assets/Level1.mp3')
        pygame.mixer.music.play(-1)  # Play the music in a loop
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)  # Limit the frame rate to 60 FPS
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(14, f'Level: {self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            height = self.window.get_height()
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (10, height - 35))
            self.level_text(14, f'Entities: {len(self.entity_list)}', COLOR_WHITE, (10, height - 20))
            pygame.display.flip()
            
            # COLLISIONS
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucidasanstypewriter", size=text_size)
        text_surf: Surface = text_font.render(text, antialias=True, color=text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)
