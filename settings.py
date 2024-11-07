class Settings:
    """A class to store settings for Alien Invasion"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Game settings
        self.fps = 60

        # Ship settings
        self.ship_speed = 1.5