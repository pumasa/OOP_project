import pygame


class Coin(pygame.sprite.Sprite):
    """ This class is used to create a coin object that can be used in Pygame.
    """

    def __init__(self, x, y):
        """ Initializes the coin object.

        Args:
            x (int): The x coordinate of the coin.
            y (int): The y coordinate of the coin.
        """
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Images/point.png')
        self.image = pygame.transform.scale(img, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
