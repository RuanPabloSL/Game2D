import pygame
from pathlib import Path

from game.Const import COLOR_BLACK, COLOR_YELLOW, WINDEFAULT_HEIGHT, WINDEFAULT_WIDTH, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, COLOR_ORANGE, COLOR_WHITE

BASE_DIR = Path(__file__).resolve().parent.parent


class Menu:

    def __init__(self,window):
        self.window: pygame.Surface = window

        self.menu_option = 0
        self.running = True
        self.clock = pygame.time.Clock()
        
        image_path = BASE_DIR / "assets" / "BGMenu.png"
        self.surf = pygame.image.load(str(image_path)).convert_alpha()
        self.surf = pygame.transform.smoothscale(
            self.surf, (self.window.get_width(), self.window.get_height())
        )
        self.rect = self.surf.get_rect(topleft=(0, 0))

        music_path = BASE_DIR / "assets" / "menu.mp3"
        pygame.mixer.music.load(str(music_path))
        pygame.mixer.music.play(-1) # Loop the music indefinitely


    def run(self, menu_option):

        self.menu_option = menu_option
        self.running = True

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.menu_option = (self.menu_option +1) % len(MENU_OPTION)
                    elif event.key == pygame.K_UP:
                        self.menu_option = (self.menu_option - 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[self.menu_option]

            self.window.blit(self.surf, self.rect)
            self.menu_text(50, "Game Shooter", COLOR_ORANGE,
                           (self.window.get_width() // 2, 70))
            
            for i, option in enumerate(MENU_OPTION):
                color = COLOR_YELLOW if i == self.menu_option else COLOR_BLACK
                self.menu_text(30, option, color,
                               (self.window.get_width() // 2, 200 + i * 35))
            self.menu_text(18, "UP/DOWN: select   ENTER: apply   ESC: back", COLOR_WHITE,
                    (self.window.get_width() // 2, self.window.get_height() - 40))
            pygame.display.flip()
            self.clock.tick(60)
           

    def settings(self, current_size):
        #Let the player choose one of the resolutions defined in Const.py.
        sizes = ((WINDEFAULT_WIDTH, WINDEFAULT_HEIGHT), (WIN_WIDTH, WIN_HEIGHT))
        selected = sizes.index(current_size) if current_size in sizes else 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_DOWN):
                        selected = (selected + 1) % len(sizes)
                    elif event.key == pygame.K_RETURN:
                        return sizes[selected]
                    elif event.key == pygame.K_ESCAPE:
                        return current_size

            self.window.fill(COLOR_BLACK)
            self.menu_text(40, "SETTINGS - SCREEN SIZE", COLOR_ORANGE,
                           (self.window.get_width() // 2, 100))
            for i, size in enumerate(sizes):
                label = f"{size[0]} x {size[1]}"
                color = COLOR_YELLOW if i == selected else COLOR_WHITE
                self.menu_text(30, label, color,
                               (self.window.get_width() // 2, 220 + i * 50))
            # self.menu_text(18, "UP/DOWN: select   ENTER: apply   ESC: back", COLOR_WHITE,
                           # (self.window.get_width() // 2, self.window.get_height() - 40))
            pygame.display.flip()
            self.clock.tick(60)

        

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.font.Font = pygame.font.SysFont(name="lucidasanstypewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
