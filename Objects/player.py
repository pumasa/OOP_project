import pygame
from Screens.maps import world
from pygame.locals import Rect

BLACK = (0, 0, 0)


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        self.prevdir = 5
        self.score = 0
        self.explosion = False
        self.game_over = False
        print(self.game_over)

    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            dx -= 3
            self.prevdir = 0

        elif keys[pygame.K_RIGHT]:
            dx += 3
            self.prevdir = 1

        elif keys[pygame.K_UP]:
            dy -= 3
            self.prevdir = 2

        elif keys[pygame.K_DOWN]:
            dy += 3
            self.prevdir = 3
        else:
            if self.prevdir == 5:
                dx = 0
            elif self.prevdir == 0:
                dx -= 3
            elif self.prevdir == 1:
                dx += 3
            elif self.prevdir == 2:
                dy -= 3
            elif self.prevdir == 3:
                dy += 3

        # wall collision
        for tile in world.tile_list:
            if tile[1].colliderect(self.x + dx, self.y, self.width, self.height):
                dx = 0
            elif tile[1].colliderect(self.x, self.y + dy, self.width, self.height):
                dy = 0

        # update player coordinates
        self.x += dx
        self.y += dy

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
