import pygame


class Block(pygame.sprite.Sprite):
    """ This class is used to create a Block object to be used in a game.
    """

#############################################################################################################
    def __init__(self, x, y, color, width, height):
        """ Creates a Block object with the given parameters.

        Args:
            x (int): x coordinate of the top left corner of the block
            y (int): y coordinate of the top left corner of the block
            color (tuple): color of the block
            width (int): width of the block
            height (int): height of the block
        """

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
