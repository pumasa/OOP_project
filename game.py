import pygame
from Screens.menu import Menu
from Screens.maps import world
from Objects.ghost import ghost
from Objects.player import Player
from client import main

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode((800, 576))
image = pygame.image.load("Images/player.png")
p1 = Player(32, 32, 29, 29)


class Game(object):
    def __init__(self):
        self.font = pygame.font.Font(None, 40)
        self.about = False
        self.game_over = True
        self.multiplayer = False
        self.game_over_screen = p1.game_over
        # Create the font for displaying the score on the screen
        self.font = pygame.font.Font(None, 35)
        # Create the menu of the game
        self.menu = Menu(("Single Player", "Multi Player", "About", "Exit"), font_color=WHITE, font_size=60)

    def process_events(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                return True

            self.menu.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over and not self.about:
                        if self.menu.state == 0:
                            # ---- Single Player ------
                            self.__init__()
                            self.game_over = False
                            self.menu = Menu(("Restart", "Multi Player", "About", "Exit"), font_color=WHITE, font_size=60)

                        elif self.menu.state == 1:
                            # ---- Multi Player ------
                            self.__init__()
                            self.game_over = False
                            self.multiplayer = True
                            main()

                        elif self.menu.state == 2:
                            # --- ABOUT ------
                            self.about = True
                        elif self.menu.state == 3:
                            # --- EXIT -------
                            # User clicked exit
                            return True

                if event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    self.about = False
        return False

    def run_logic(self):
        if not self.game_over:
            self.game_over_screen = p1.game_over
            if self.game_over_screen:
                self.game_over = True

    def display_frame(self, screen):
        # First, clear the screen to white. Don't put other drawing commands
        screen.fill(BLACK)
        # --- Drawing code should go here

        if self.game_over:
            if self.game_over_screen:
                self.display_message_score(screen, "Your Score: " + str(p1.score))
            if self.about:
                self.display_message(screen, "It is an arcade Game")
            else:
                self.menu.display_frame(screen)

        # elif self.multiplayer:
        #     screen.fill((0, 0, 0))
        #     world.draw()
        #     screen.blit(ghost.image, ghost.rect)
        #     ghost.update()
        #     text = self.font.render("Score: " + str(p1.score), True, GREEN)
        #     screen.blit(text, [10, 5])
        #     self.multi(screen)

        else:
            screen.blit(image, p1)
            world.draw()
            screen.blit(ghost.image, ghost.rect)
            ghost.update()
            p1.move()
            text = self.font.render("Score: " + str(p1.score), True, GREEN)
            screen.blit(text, [10, 5])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def display_message(self, screen, message, color=(255, 0, 0)):
        label = self.font.render(message, True, color)
        # Get the width and height of the label
        width = label.get_width()
        height = label.get_height()
        # Determine the position of the label
        posX = (800 / 2) - (width / 2)
        posY = (576 / 2) - (height / 2)
        # Draw the label onto the screen
        screen.blit(label, (posX, posY))

    def display_message_score(self, screen, message, color=(255, 0, 0)):
        label = self.font.render(message, True, color)
        # Get the width and height of the label
        width = label.get_width()
        # Determine the position of the label
        posX = (800 / 2) - (width / 2)
        posY = (50)
        # Draw the label onto the screen
        screen.blit(label, (posX, posY))
