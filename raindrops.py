import pygame
from settings import Settings
from raindrop import Raindrop
import sys

class Raindrops:
    """Overall class to manage the asset(s) and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()    # Initalized clock to run at a set fps.
        self.settings = Settings()

        # Set the screen window.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops")

        # Raindrop setup
        #self.raindrop = Raindrop(self)
        self.raindrops = pygame.sprite.Group()

        self._create_raindrops()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)     # Have the game run at 60 fps.

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            # If the player closes the window, then exit.
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_raindrops(self):
        """Create the rows of raindrops"""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size        # Get the raindrop width and height.
        
        # Set the current x and y to the raindrop's width and height
        current_x, current_y = raindrop_width, raindrop_height

        # Loop to create the rows of raindrops.
        # Setting the width and height between raindrops to be the width and height of a raindrop.
        # The current x and y values will be the positions of where the next raindrop will go.
        while current_y < (self.settings.screen_height - 3 * raindrop_height):
            while current_x < (self.settings.screen_width - 2 * raindrop_width):
                # Create a raindrop at the current x and y position
                self._create_raindrop(current_x, current_y)
                current_x += 2 * raindrop_width     # Leaves space between the previous and current x value exactly one raindrop size.

            # Once a row is finished, reset the x value to the beginning of the row,
            # and increment the y value to start the new row.
            current_x = raindrop_width
            current_y += 2 * raindrop_height

    def _create_raindrop(self, x_position, y_position):
        """Creates a star."""
        # x_position is the location in the row that the raindrop is placed.
        # y_position is the current row for the raindrops.
        new_raindrop = Raindrop(self)
        new_raindrop.x = x_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()            


if __name__ == '__main__':
    # Make the game instance and run the game.
    rd = Raindrops()
    rd.run_game()