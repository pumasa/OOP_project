import pygame
from Objects import Coin
# from Screens import enviroment


win = pygame.display.set_mode((800, 576))


class World():
    """This class is used to create a world object that can be used in Pygame.
    """

#############################################################################################################
    def __init__(self, data):
        """Initializes the world object.

        Args:
            data (list): A list of lists that contain information about the world.
        """

        self.tile_list = []
        self.coin_list = []
        self.intersections = []
        wall_img = pygame.image.load('Images/blue.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(
                        wall_img, (32, 32))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * 32
                    img_rect.y = row_count * 32
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2:
                    coin = Coin(col_count * 32 + (32 // 2), row_count*32 + (32 // 2))
                    # coin_group.add(coin)
                    coin_data = (coin.image, coin.rect)
                    self.coin_list.append(coin_data)

                if tile == 3:
                    intersec_rect = img.get_rect()
                    intersec_rect.x = col_count * 32
                    intersec_rect.y = row_count * 32
                    intersect = intersec_rect
                    self.intersections.append((intersect[0], intersect[1]))
                col_count += 1
            row_count += 1

#############################################################################################################
    def draw(self):
        """Draws the world object.
        """

        for tile in self.tile_list:
            win.blit(tile[0], tile[1])

        for coin in self.coin_list:
            win.blit(coin[0], coin[1])


# world = World(enviroment())
