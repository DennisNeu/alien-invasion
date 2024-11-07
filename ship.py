import pygame
from settings import Settings

class Ship:
    """A calss to manage the space ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image and get its rect
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()

        # Place at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

        self.settings = Settings()

    def blitme(self):
        """Draw the ship at current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag"""

        if self.moving_right:
            self.rect.x += self.settings.ship_speed
        
        if self.moving_left:
            self.rect.x -= self.settings.ship_speed

