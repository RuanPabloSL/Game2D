import pygame




# C
COLOR_ORANGE =(255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREY = (128, 128, 128)
COLOR_CYAN = (0, 255, 255)
COLOR_BLACK = (0, 0, 0)

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
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 3,
}







#M
MENU_OPTION = ('NEW GAME 1P', 'NEW GAME 2P - CO-OP', 'NEW GAME 2P - COPETITIVE', 'SCORE', 'SETTINGS','EXIT')

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

# W 
WIN_WIDTH = 1000
WIN_HEIGHT = 560
576
800

