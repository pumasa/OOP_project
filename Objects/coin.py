import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Images/point.png')
        self.image = pygame.transform.scale(img, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
