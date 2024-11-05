import sys
import pygame
from settings import Settings

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

    def run_game(self):
        """Start main game loop"""
        while True:
            # Watch for HID events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            # Redraw bg_color
            self.screen.fill(self.settings.bg_color)
        
            # Make the most recently drawn screen visible    
            pygame.display.flip()
            self.clock.tick(60)
    
if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()