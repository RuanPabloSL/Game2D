import pygame
from pathlib import Path

from game.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, COLOR_ORANGE, COLOR_WHITE

BASE_DIR = Path(__file__).resolve().parent.parent


class Menu:

    def __init__(self,window):
        self.window: pygame.Surface = window
        image_path = BASE_DIR / "assets" / "BGMenu.png"
        self.surf = pygame.image.load(str(image_path))
        self.surf = pygame.transform.smoothscale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(topleft=(0, 0))

        music_path = BASE_DIR / "assets" / "menu.mp3"
        pygame.mixer.music.load(str(music_path))
        pygame.mixer.music.play(-1) # Loop the music indefinitely


    def run(self, ):
        self.window.blit(self.surf, self.rect)
        self.menu_text(50, "Game Shooter", (COLOR_ORANGE), (WIN_WIDTH // 2, 70))


        for i in range(len(MENU_OPTION)):
            self.menu_text(20, MENU_OPTION[i], (COLOR_WHITE), (WIN_WIDTH // 2, 300 + i * 25))


        

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.Font = pygame.font.SysFont(name="Lucida Sans Typeriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, antialias=True, color=text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)