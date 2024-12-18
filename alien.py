import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent the aliens in the game"""

    def __init__(self, ai_game):
        """Initialize alien and set starting pos"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image and set rect attribute
        self.image = pygame.image.load("img/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    def check_edges(self):
        """return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)