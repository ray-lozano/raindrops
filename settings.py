class Settings:
    """Class for storing settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Raindrop settings
        self.rain_speed = 1.0
        self.rain_direction = 1