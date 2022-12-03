import pygame
from pygame.locals import Rect
from Objects import Animation


class Player(pygame.sprite.Sprite):
    """ This class is used to create a player object to be used in a game.
    """

#############################################################################################################
    def __init__(self, x, y, width, height):
        """ Creates a Player object with the given parameters.

        Args:
            x (int): x coordinate of the top left corner of the player
            y (int): y coordinate of the top left corner of the player
            width (int): width of the player
            height (int): height of the player
        """

        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load("Images/player.png").convert()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        self.prevdir = 5
        self.score = 0
        self.game_over = False
        self.collision = False
        img = pygame.image.load("Images/walk.png").convert()
        self.right_anim = Animation(img, 32, 32)
        self.left_anim = Animation(pygame.transform.flip(img, True, False), 32, 32)
        self.up_anim = Animation(pygame.transform.rotate(img, 90), 32, 32)
        self.down_anim = Animation(pygame.transform.rotate(img, 270), 32, 32)

#############################################################################################################
    def move(self, controls):
        """ Moves the player in the direction specified by the controls.

        Args:
            controls (dict): dictionary containing the controls for the game
        """

        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        if keys[controls[0]]:
            dx -= 3
            self.prevdir = 0

        elif keys[controls[1]]:
            dx += 3
            self.prevdir = 1

        elif keys[controls[2]]:
            dy -= 3
            self.prevdir = 2

        elif keys[controls[3]]:
            dy += 3
            self.prevdir = 3
        else:
            if self.prevdir == 5:
                dx = 0
            elif self.prevdir == 0:
                self.left_anim.update(10)
                self.img = self.left_anim.get_current_image()
                dx -= 3
            elif self.prevdir == 1:
                self.right_anim.update(10)
                self.img = self.right_anim.get_current_image()
                dx += 3
            elif self.prevdir == 2:
                self.up_anim.update(10)
                self.img = self.up_anim.get_current_image()
                dy -= 3
            elif self.prevdir == 3:
                self.down_anim.update(10)
                self.img = self.down_anim.get_current_image()
                dy += 3

        # wall collision
        for tile in self.world.tile_list:
            if tile[1].colliderect(self.x + dx, self.y, self.width, self.height):
                dx = 0
            elif tile[1].colliderect(self.x, self.y + dy, self.width, self.height):
                dy = 0

        # player collision
        if self.collision:
            if dx == 3:
                dx = -4
                self.prevdir = 0
                self.collision = False
            if dx == -3:
                dx = 4
                self.prevdir = 1
                self.collision = False
            if dy == 3:
                dy = -4
                self.prevdir = 2
                self.collision = False
            if dy == -3:
                dy = 4
                self.prevdir = 3
                self.collision = False

        # off screen
        if self.x < 0:
            self.x = 800
        elif self.x > 800:
            self.x = 0
        if self.y < 0:
            self.y = 576
        elif self.y > 576:
            self.y = 0

        # update player coordinates
        self.x += dx
        self.y += dy

        self.update()

#############################################################################################################
    def update(self):
        """ Updates the player's position and image.
        """

        self.rect = (self.x, self.y, self.width, self.height)
