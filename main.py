import pygame


class Main:
    def main():
        pygame.init()
        screen = pygame.display.set_mode((800, 576))
        pygame.display.set_caption("Battle Royal Pacman")

        clock = pygame.time.Clock()

        running = True
        while running:

            # RGB screen colors
            screen.fill((255, 255, 255))
            clock.tick(30)
            # Quit function for close button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    if __name__ == '__main__':
        main()
