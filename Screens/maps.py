import pygame
from Objects.coin import Coin


tile_size = 32
win = pygame.display.set_mode((800, 576))


class World():
    def __init__(self, data):

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
                        wall_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2:
                    coin = Coin(col_count * tile_size + (tile_size // 2), row_count*tile_size + (tile_size // 2))
                    # coin_group.add(coin)
                    coin_data = (coin.image, coin.rect)
                    self.coin_list.append(coin_data)

                if tile == 3:
                    intersec_rect = img.get_rect()
                    intersec_rect.x = col_count * tile_size
                    intersec_rect.y = row_count * tile_size
                    intersect = intersec_rect
                    self.intersections.append((intersect[0], intersect[1]))
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            win.blit(tile[0], tile[1])

        for coin in self.coin_list:
            win.blit(coin[0], coin[1])


# coin_group = pygame.sprite.Group()


def enviroment():
    grid = (
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            (1, 3, 2, 2, 3, 2, 2, 3, 2, 2, 3, 1, 1, 1, 3, 2, 2, 3, 2, 2, 3, 2, 2, 3, 1),
            (1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1),
            (1, 0, 1, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 1, 0, 1),
            (1, 3, 0, 3, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 3, 0, 3, 1),
            (1, 0, 1, 0, 1, 3, 0, 3, 0, 0, 0, 3, 1, 3, 0, 0, 0, 3, 0, 3, 1, 0, 1, 0, 1),
            (1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1),
            (1, 3, 0, 3, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 3, 0, 3, 1),
            (1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1),
            (1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1),
            (1, 3, 0, 3, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 3, 0, 3, 1),
            (1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1),
            (1, 0, 1, 0, 1, 3, 0, 3, 0, 0, 0, 3, 1, 3, 0, 0, 0, 3, 0, 3, 1, 0, 1, 0, 1),
            (1, 3, 0, 3, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 3, 0, 3, 1),
            (1, 0, 1, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 1, 0, 1),
            (1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1),
            (1, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 1, 1, 1, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 1),
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            )
    return grid


world = World(enviroment())

# 3 cross road intersection
# 2 points
# 1 walls
# 0 empty
