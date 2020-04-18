# __author__ = Danielle M Chaitkin

import pygame

from background import Background
from settings import Settings
from spaceship import Ship
import ai_game_functions as gf
from pygame.sprite import Group
from game_statistics import GameStats
from fps_counter import FPSCounter
from menu import Menu
from game_scoreboard import Scoreboard


def run_game():
    # Init the game and create window object
    pygame.init()
    ai_settings = Settings()
    clock = pygame.time.Clock()
    background = Background("images/space_bg.jpg", (0, 0))

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")

    # Create an instance for game statistics storage & scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    fps_counter = FPSCounter(ai_settings, screen)

    # Create menu
    menu = Menu(screen, stats)

    # Create the ship, bullets group & aliens group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    invader_bullets = Group()
    alien_invaders = Group()

    # Create aliens fleet
    gf.create_fleet(ai_settings, screen, ship, alien_invaders)

    # Ticks
    ticks = 0

    game_process = True

    # Start main game loop
    while game_process:
        fps = int(clock.get_fps())

        gf.check_events(
            ai_settings, screen, stats, sb, menu, ship, alien_invaders, bullets)
        if stats.game_active:
            ticks += 1
            ship.update()
            pygame.mixer.music.play(0)
            gf.update_bullets(
                ai_settings, screen, stats, sb, ship,
                alien_invaders, bullets, invader_bullets)

            gf.update_aliens(
                ai_settings, stats, sb, screen, ship,
                alien_invaders, bullets, invader_bullets, ticks)

            if ticks % ai_settings.tick_factor == 0:
                ticks = 0

        gf.update_screen(
            ai_settings, screen, stats, sb, ship, alien_invaders,
            bullets, invader_bullets, menu, fps_counter, fps)

        clock.tick(ai_settings.fps)


run_game()
