import sys

import pygame

from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_setting = Settings()
    # screen = pygame.display.set_mode((1200, 800))
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption("打飞机")
    # bg_color = (230, 230, 230)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.fill(ai_setting.bg_color)
            ship.bliteme()
            pygame.display.flip()


run_game()
