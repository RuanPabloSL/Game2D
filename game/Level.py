import random
import pygame
import sys

from pygame import Rect, Surface
from game.Const import (COLOR_BLACK, COLOR_GREEN, COLOR_GREY, COLOR_RED, COLOR_WHITE, EVENT_ENEMY, EVENT_TIMEOUT, MENU_OPTION, SPAWN_TIME, TIMEOUT_LEVEL, TIMEOUT_STEP)
from game.Enemy import Enemy
from game.Entity import Entity
from game.EntityFactory import EntityFactory
from game.EntityMediator import EntityMediator
from game.Player import Player


class Level:

    def __init__(self, window, name, game_mode, player_score=None):
        self.window: Surface = window
        self.name: str = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name))
        player = EntityFactory.get_entity('Player1')[0]
        player.score = player_score[0] if player_score else 0
        self.entity_list.append(player)
        is_two_player = game_mode in [MENU_OPTION[1], MENU_OPTION[2]]
        self.timeout = TIMEOUT_LEVEL * (3 if is_two_player else 1)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')[0]
            player.score = player_score[1] if player_score and len(player_score) > 1 else 0
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)


    def run(self, menu):
        music_file = './assets/Level1.mp3' if self.name == 'LvL1' else './assets/Level2.mp3'
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        start_countdown = 5
        start_time = pygame.time.get_ticks()
        result = None
        paused = False
        pause_selection = 0
        pause_options = ('Return to game', 'Settings', 'Main menu')

        while True:
            clock.tick(60)  # Limit the frame rate to 60 FPS
            elapsed_start = (pygame.time.get_ticks() - start_time) / 1000
            if elapsed_start < start_countdown:
                self.window.fill((0, 0, 0))
                self.level_text(24, f'Player 1: arrows + Right Ctrl', COLOR_GREEN, (20, 20))
                if self.game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
                    self.level_text(24, 'Player 2: W A S D + Left Ctrl', COLOR_GREY, (self.window.get_width() - 460, 20))
                self.level_text(64, str(5 - int(elapsed_start)), COLOR_WHITE,
                                (self.window.get_width() // 2 - 20, self.window.get_height() // 2 - 40))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                continue
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', COLOR_GREY, (10, 45))
            players = [ent for ent in self.entity_list if isinstance(ent, Player)]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    paused = not paused
                    if paused:
                        pause_started = pygame.time.get_ticks()
                        pygame.time.set_timer(EVENT_ENEMY, 0)
                        pygame.time.set_timer(EVENT_TIMEOUT, 0)
                    else:
                        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
                        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
                if paused and event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_DOWN):
                        pause_selection = (pause_selection + (1 if event.key == pygame.K_DOWN else -1)) % len(pause_options)
                    elif event.key == pygame.K_RETURN:
                        if pause_selection == 0:
                            paused = False
                            pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
                            pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
                        elif pause_selection == 1:
                            self.timeout += pygame.time.get_ticks() - pause_started
                            new_size = menu.settings((self.window.get_width(), self.window.get_height()))
                            if new_size != (self.window.get_width(), self.window.get_height()):
                                self.window = pygame.display.set_mode(new_size)
                                menu = type(menu)(self.window)
                            paused = False
                            pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
                            pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
                        else:
                            pygame.time.set_timer(EVENT_ENEMY, 0)
                            pygame.time.set_timer(EVENT_TIMEOUT, 0)
                            return None
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                elif event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
            if paused:
                self.window.fill(COLOR_BLACK)
                self.level_text(38, 'PAUSED', COLOR_WHITE, (self.window.get_width() // 2 - 80, 120))
                for i, option in enumerate(pause_options):
                    self.level_text(26, f'{"> " if i == pause_selection else "  "}{option}', COLOR_GREEN if i == pause_selection else COLOR_WHITE,
                                    (self.window.get_width() // 2 - 150, 220 + i * 50))
                pygame.display.flip()
                continue
            players = [ent for ent in self.entity_list if isinstance(ent, Player)]
            two_player = self.game_mode in [MENU_OPTION[1], MENU_OPTION[2]]
            if not players or (two_player and len(players) < 2):
                result = False
                break
            if self.timeout <= 0:
                result = all(player.score >= 2500 for player in players)
                break

            # printed text
            self.level_text(14, f'Level: {self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            height = self.window.get_height()
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (10, height - 35))
            self.level_text(14, f'Entities: {len(self.entity_list)}', COLOR_WHITE, (10, height - 20))
            pygame.display.flip()
            
            # COLLISIONS
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

        pygame.time.set_timer(EVENT_ENEMY, 0)
        pygame.time.set_timer(EVENT_TIMEOUT, 0)
        self.show_result(result, players)
        return result, [player.score for player in players]

    def show_result(self, won, players):
        self.window.fill((0, 0, 0))
        color = COLOR_GREEN if won else COLOR_RED
        message = ('Congratulations, you beat the game!' if self.name == 'LvL2' else 'You won and have moved on to the next stage.') if won else 'GAME - OVER'
        rect = pygame.font.SysFont('lucidasanstypewriter', 28).render(message, True, color).get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 - 40))
        self.window.blit(pygame.font.SysFont('lucidasanstypewriter', 28).render(message, True, color), rect)
        for index, player in enumerate(players):
            player_color = COLOR_GREEN if player.name == 'Player1' else COLOR_GREY
            self.level_text(22, f'{player.name} score: {player.score}', player_color,
                            (self.window.get_width() // 2 - 120, self.window.get_height() // 2 + 10 + index * 35))
        if len(players) == 2:
            if players[0].score > players[1].score:
                winner = players[0]
            elif players[1].score > players[0].score:
                winner = players[1]
            else:
                winner = None
            if winner:
                self.level_text(22, f'{winner.name} scored more: {winner.score}', COLOR_GREEN if winner.name == 'Player1' else COLOR_GREY, (self.window.get_width() // 2 - 220, self.window.get_height() // 2 + 10))
            else:
                self.level_text(22, f'Tie: {players[0].score} points each', COLOR_WHITE, (self.window.get_width() // 2 - 170, self.window.get_height() // 2 + 10))
        pygame.display.flip()
        pygame.time.wait(2500)
        

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: pygame.font.Font = pygame.font.SysFont(name="lucidasanstypewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)
