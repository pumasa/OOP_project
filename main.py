import pygame
from game import Game


def main():
    """ Main function of the program.
    """

    # Initialize all imported pygame modules
    pygame.init()
    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode((800, 576))
    # Set the current window caption
    pygame.display.set_caption("Battle Royale - PacMan")
    # Loop until the user clicks the close button.
    run = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create a game object
    game = Game()
    # -------- Main Program Loop -----------
    while not run:
        # --- Process events
        run = game.process_events()

        # --- Game
        game.run_logic()

        # --- Draw the current frame
        game.display_frame(screen)

        # --- Limit to 30 frames per second
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()
