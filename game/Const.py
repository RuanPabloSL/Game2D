import pygame

# C
COLOR_ORANGE =(255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREY = (128, 128, 128)
COLOR_CYAN = (0, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (237, 28, 36)

# E
EVENT_ENEMY= pygame.USEREVENT + 1
ENTITY_SPEED = {
    'LvL1BG0': 0,
    'LvL1BG1': 1,
    'LvL1BG2': 2,
    'LvL1BG3': 3,
    'LvL1BG4': 4,
    'LvL1BG5': 5,
    'LvL1BG6': 0,
    'Player1': 3,
    'Player1Shot': 4,
    'Player2': 3,
    'Player2Shot': 4,
    'Enemy1': 1,
    'Enemy1Shot': 6,
    'Enemy2': 1,
    'Enemy2Shot': 6,
    
}

ENTITY_HEALTH = {'LvL1BG0': 999,
                 'LvL1BG1': 999,
                 'LvL1BG2': 999,
                 'LvL1BG3': 999,
                 'LvL1BG4': 999,
                 'LvL1BG5': 999,
                 'LvL1BG6': 999,
                 'LvL2BG0': 999,
                 'LvL2BG1': 999,
                 'LvL2BG2': 999,
                 'LvL2BG3': 999,
                 'LvL2BG4': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 100,
                 'Enemy1Shot': 1,
                 'Enemy2': 100,
                 'Enemy2Shot': 1,
                 }

ENTITY_SHOT_DELAY = {
                    'Player1': 30,
                    'Player2': 30,
                    'Enemy1': 110,
                    'Enemy2': 110,
                    }

ENTITY_DAMAGE = {
                 'LvL1BG0': 0,
                 'LvL1BG1': 0,
                 'LvL1BG2': 0,
                 'LvL1BG3': 0,
                 'LvL1BG4': 0,
                 'LvL1BG5': 0,
                 'LvL1BG6': 999,
                 'LvL2BG0': 999,
                 'LvL2BG1': 999,
                 'LvL2BG2': 999,
                 'LvL2BG3': 999,
                 'LvL2BG4': 999,
                 'Player1': 1,
                 'Player1Shot': 35,
                 'Player2': 1,
                 'Player2Shot': 35,
                 'Enemy1': 1,
                 'Enemy1Shot': 35,
                 'Enemy2': 1,
                 'Enemy2Shot': 35,
                }

#M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - CO-OP',
                'NEW GAME 2P - COPETITIVE',
                'SCORE',
                'SETTINGS',
                'EXIT')

# P 
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000 #4 SEGUNDOS
ENTITY_SCORE = {
                 'LvL1BG0': 0,
                 'LvL1BG1': 0,
                 'LvL1BG2': 0,
                 'LvL1BG3': 0,
                 'LvL1BG4': 0,
                 'LvL1BG5': 0,
                 'LvL1BG6': 0,
                 'LvL2BG0': 0,
                 'LvL2BG1': 0,
                 'LvL2BG2': 0,
                 'LvL2BG3': 0,
                 'LvL2BG4': 0,
                 'Player1': 0,
                 'Player1Shot': 0,
                 'Player2': 0,
                 'Player2Shot': 0,
                 'Enemy1': 100,
                 'Enemy1Shot': 0,
                 'Enemy2': 114,
                 'Enemy2Shot': 0,
                }

# W 
WINDEFAULT_WIDTH = 800 
WINDEFAULT_HEIGHT = 600
WIN_WIDTH = 1000 # escala maior
WIN_HEIGHT = 600

