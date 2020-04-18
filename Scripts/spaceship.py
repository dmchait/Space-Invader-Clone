import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize Space Craft and set position on game screen"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load image for space craft
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set position of space craft craft on game screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        # store decimal value for center of ship
        self.up = float(self.rect.centery)
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update position of ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor

        # update rect object from self.center
        if self.moving_right or self.moving_left:
            self.rect.centerx = self.center
        if self.moving_up or self.moving_down:
            self.rect.centery = self.center

    def center_ship(self):
        """Center the new space craft"""
        self.center = self.screen_rect.centerx

    def blitme(self):
        """Draw image at set position"""
        self.screen.blit(self.image, self.rect)
