import pygame
from network import Network
from Screens.maps import world
# from pygame.locals import *
from Objects.ghost import ghost

width = 800
height = 576

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
win = pygame.display.set_mode((800, 576))
pygame.display.set_caption("Client")

image = pygame.image.load("player.png")


game_over = False


def redrawWindow(win, player, player2):
    win.fill((0, 0, 0))
    win.blit(image, player)
    win.blit(image, player2)
    world.draw()
    win.blit(ghost.image, ghost.rect)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    print(p)
    clock = pygame.time.Clock()

    while run:
        p2 = n.send(p)
        clock.tick(60)
        ghost.update()

        # Quit function for close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)

        pygame.display.flip()


if __name__ == '__main__':
    main()
