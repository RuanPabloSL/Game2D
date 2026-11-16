import pygame
from pathlib import Path

pygame.init()
for i in range(5):
    path = Path(f'assets/LvL1BG{i}.png')
    img = pygame.image.load(str(path))
    print(path.name, img.get_size(), 'alpha' if img.get_flags() & pygame.SRCALPHA else 'sem alpha')
    pygame.image.save(img, f'debug_LvL1BG{i}.png')


import pygame

pygame.init()
for i in range(5):
    img = pygame.image.load(f'assets/LvL1BG{i}.png')
    w, h = img.get_size()
    esq = sum(img.get_at((0, y)).a == 0 for y in range(h))
    dir_ = sum(img.get_at((w - 1, y)).a == 0 for y in range(h))
    print(f'LvL1BG{i}: borda esquerda transparente em {esq}/{h} linhas, direita em {dir_}/{h} linhas')