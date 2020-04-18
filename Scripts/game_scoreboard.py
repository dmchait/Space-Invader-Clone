import pygame.ftfont
from pygame.sprite import Group
from spaceship import Ship


class Scoreboard:
    """Class to represent information for game scoring"""

    def __init__(self, ai_settings, screen, stats):
        """Initialize score keeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Establish font settings for game score
        self.txt_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 30)

        # Prepare image for starting score
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        """Show the number of ships player has left"""
        self.ships = Group()

        for ship_number in range(self.stats.ships_left):
            space_craft = Ship(self.ai_settings, self.screen)
            space_craft.rect.x = 595 + ship_number * space_craft.rect.width
            space_craft.rect.y = self.screen_rect.bottom - 60
            self.ships.add(space_craft)

    def prep_level(self):
        """Turn the level into a rendered image"""
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.txt_color, self.ai_settings.bg_color)

        # position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.score_rect.left
        self.level_rect.top = self.screen_rect.top

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.txt_color,
                                            self.ai_settings.bg_image)

        # Display score on the top right of the game screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.txt_color,
                                                 self.ai_settings.bg_image)

        # Display score on the top right of the game screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw the score and ships to the game screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Draw ships
        self.ships.draw(self.screen)
