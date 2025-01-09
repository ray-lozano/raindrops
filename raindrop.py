import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """Class to represent a single raindrop in the sky."""

    def __init__(self, rain_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = rain_game.screen

        # Load the raindrop image and set itss rect attribute.
        self.image = pygame.image.load('raindrop.png')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact horizontal position.
        self.x = float(self.rect.x)