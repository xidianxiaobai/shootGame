import pygame

import game_function as gf
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
        gf.check_event(ship)
        gf.update_screen(ai_setting, screen, ship)



run_game()
