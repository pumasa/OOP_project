import pygame
import random
from Screens.maps import world


width = 800
height = 550


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, change_x, change_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Images/ghost.png')
        self.image = pygame.transform.scale(img, (32, 32))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.change_x = change_x
        self.change_y = change_y
        self.rect.topleft = (x, y)

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.rect.left = width
        elif self.rect.left > width:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = height
        elif self.rect.top > height:
            self.rect.bottom = 0

        if self.rect.topleft in world.intersections:
            self.change_direction(random.choice(("x", "y")))

    # wall collision detection
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y - 2, 32, 32) and self.change_y == -2:
                self.change_x = 2
                self.change_y = 0

            elif tile[1].colliderect(self.rect.x+2, self.rect.y, 32, 32) and self.change_x == 2:
                self.change_x = 0
                self.change_y = 2

            elif tile[1].colliderect(self.rect.x, self.rect.y+2, 32, 32) and self.change_y == 2:
                self.change_x = -2
                self.change_y = 0

            elif tile[1].colliderect(self.rect.x-2, self.rect.y, 32, 32) and self.change_x == -2:
                self.change_x = 0
                self.change_y = -2

    def change_direction(self, direction):
        if direction == "x":
            x = random.choice(("left", "right"))
            if x == "left":
                self.change_x = -2
                self.change_y = 0
            elif x == "right":
                self.change_x = 2
                self.change_y = 0
        elif direction == "y":
            y = random.choice(("up", "down"))
            if y == "up":
                self.change_x = 0
                self.change_y = -2
            elif y == "down":
                self.change_x = 0
                self.change_y = 2


ghost = Ghost(96, 128, -2, 0)
