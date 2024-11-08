import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()

        # Initialize settings object
        self.settings = Settings()

        # Clock to control framerate
        self.clock = pygame.time.Clock()
        
        # Screen/Surface
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")
        
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Delete bullets that have left screen area
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        """Respond to HID events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()       

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Redraw bg_color
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.ship.blitme()

        # Make the most recently drawn screen visible    
        pygame.display.flip()

    def _fire_bullet(self):

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()