import sys

import pygame


def check_event(ship):
    move_distance = 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += move_distance
            elif event.key == pygame.K_LEFT:
                ship.rect.centerx -= move_distance


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.bliteme()
    pygame.display.flip()
