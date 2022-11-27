import pygame
from Screens.maps import world
from pygame.locals import Rect
from Objects.ghost import ghost
BLACK = (0, 0, 0)

# pygame.init()
# win = pygame.display.set_mode((800, 550))
score = 0


class Player(pygame.sprite.Sprite):
    explosion = False
    game_over = False

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        self.prevdir = 5

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

        # coin collision
        for coin in world.coin_list:
            if coin[1].colliderect(self.x, self.y, self.width, self.height):
                global score
                score += 10
                world.coin_list.remove(coin)
                print(score)

        # ghost collision
        if ghost.rect.colliderect(self.x, self.y, self.width, self.height):
            self.explosion = True
            self.game_over = True
            print("GameOver")

        # update player coordinates
        self.x += dx
        self.y += dy

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
