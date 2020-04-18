import pygame
from pygame.sprite import Sprite


class InvaderBullet(Sprite):
    """Control bullets produced by ship"""
    def __init__(self, ai_settings, screen, invader):
        """Create bullet object in current ship position"""
        super().__init__()
        self.screen = screen

        # Create a bullet in position (0, 0) and set right position
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        self.rect.centerx = invader.rect.centerx
        self.rect.bottom = invader.rect.bottom

        # Store float bullet position
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.invader_bullet_speed_factor

    def update(self):
        """Move bullet down"""
        # Update bullet position in float
        self.y += self.speed_factor

        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw a bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
