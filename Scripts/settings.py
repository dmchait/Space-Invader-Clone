import pygame


class Settings:
    """Class that stores all game settings"""

    def __init__(self):
        """Initialize static game settings"""
        # screen parameters

        self.screen_width = 800
        self.screen_height = 500
        self.bg_image = pygame.image.load('images/space_bg.jpg')
        self.bg_color = (30, 30, 30)
        self.font_color = (230, 230, 230)
        pygame.mixer.music.load('sounds/ufo-landing.wav')
        pygame.mixer.music.load('sounds/laser.wav')

        # Show fps flag
        self.fps = 60
        self.show_fps = True

        # Ship settings
        self.ship_limit = 3

        # Bullet parameters
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 230, 230, 230
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 6

        # Game tempo factor
        self.speedup_scale = 1.0

        # Aliens cost increase factor
        self.score_scale = 1.5

        # Shot frequency value
        self.tick_factor = 100

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize dynamic settings"""
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 10
        self.invader_bullet_speed_factor = self.bullet_speed_factor / 4
        self.invader_speed_factor = 3

        # fleet_direction = 1 means right; -1 means left
        self.fleet_direction = 1

        # Points amount for an alien
        self.invader_points = 50

    def increase_speed(self):
        """Increase game speed settings & alien cost"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.invader_speed_factor *= self.speedup_scale

        self.invader_points = int(self.invader_points * self.score_scale)
