import pygame
from Screens import Menu
from Screens import World
from Objects import Ghost
from Objects import Player
from Screens import enviroment
from pygame.locals import Rect

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((800, 576))
image = pygame.image.load("Images/player.png")

PLAYER1_CONTROLS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
PLAYER2_CONTROLS = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]


class Game():
    def __init__(self):
        self.font = pygame.font.Font(None, 40)
        self.about = False
        self.game_over = True
        self.singleplayer = False
        self.multiplayer = False
        self.p1_dead = False

        self.world = World(enviroment())
        self.player = Player(32, 32, 29, 29)
        self.player.world = self.world
        self.ghost1 = Ghost(544, 288, -2, 0)
        self.ghost1.world = self.world
        self.ghost2 = Ghost(576, 288, 2, 0)
        self.ghost2.world = self.world
        self.ghost3 = Ghost(256, 288, 0, 2)
        self.ghost3.world = self.world
        self.ghost4 = Ghost(288, 288, 0, -2)
        self.ghost4.world = self.world

        # Load the sound effects
        self.pacman_sound = pygame.mixer.Sound("Sounds/pacman_sound.ogg")
        self.game_over_sound = pygame.mixer.Sound("Sounds/game_over_sound.ogg")

        self.game_over_screen = self.player.game_over
        # Create the font for displaying the score on the screen
        self.font = pygame.font.Font(None, 35)
        # Create the menu of the game
        self.menu = Menu(("Single Player", "Multi Player", "About", "Exit"), font_color=WHITE, font_size=60)
########################################################################################################

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
                            self.singleplayer = True
                            self.multiplayer = False

                        elif self.menu.state == 1:
                            # ---- Multi Player ------
                            self.__init__()
                            self.game_over = False
                            self.singleplayer = False
                            self.multiplayer = True
                            self.p2_dead = False
                            self.menu = Menu(("Single Player", "Restart", "About", "Exit"), font_color=WHITE, font_size=60)
                            self.player2 = Player(736, 448, 29, 29)
                            self.player2.world = self.world
                            # self.player2 = Player(64, 32, 29, 29)

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
########################################################################################################

    def run_logic(self):
        # Single Player
        if self.singleplayer:
            if not self.game_over:
                self.game_over_screen = self.player.game_over
                if self.game_over_screen:
                    self.game_over = True

            # coin collision
            for coin in self.world.coin_list:
                if coin[1].colliderect(Rect(self.player.rect)):
                    self.pacman_sound.play()
                    self.player.score += 10
                    self.world.coin_list.remove(coin)

                # resets points and increses ghost speed
                if len(self.world.coin_list) == 0:
                    self.world = World(enviroment())
                    for i in range(1, 5):
                        eval("self.ghost" + str(i) + ".speed += 0.5")

            # ghost collision
            for i in range(1, 5):
                if eval("self.ghost" + str(i)).rect.colliderect(Rect(self.player.rect)):
                    self.player.game_over = True

        # Multiplayer
        elif self.multiplayer:
            if not self.game_over:
                self.game_over_screen = self.player.game_over
                if self.game_over_screen:
                    self.game_over = True

            # player collision
            if Rect(self.player.rect).colliderect(Rect(self.player2.rect)):
                self.player.collision = True
                self.player2.collision = True

            # coin collision
            for coin in self.world.coin_list:
                if coin[1].colliderect(Rect(self.player.rect)):
                    self.player.score += 10
                    self.world.coin_list.remove(coin)
                if coin[1].colliderect(Rect(self.player2.rect)):
                    self.player2.score += 10
                    self.world.coin_list.remove(coin)
                if len(self.world.coin_list) == 0:
                    self.world = World(enviroment())

            # ghost collision
            for i in range(1, 5):
                if eval("self.ghost" + str(i) + ".rect.colliderect(Rect(self.player.rect))"):
                    self.game_over = True
                    self.p1_dead = True

                if eval("self.ghost" + str(i) + ".rect.colliderect(Rect(self.player2.rect))"):
                    self.game_over = True
                    self.p2_dead = True

########################################################################################################

    def display_frame(self, screen):
        screen.fill(BLACK)

        # --- Drawing code should go here
        if self.game_over:
            if self.singleplayer:
                self.display_message_score(screen, "Your Score: " + str(self.player.score), GREEN, 80)

            if self.multiplayer:
                self.display_message_score(screen, "Player1 Score: " + str(self.player.score), GREEN, 80)
                self.display_message_score(screen, "Player2 Score: " + str(self.player2.score), GREEN, 110)
                if self.p1_dead:
                    self.display_message_score(screen, "Player1 Lost", RED, 50)
                elif self.p2_dead:
                    self.display_message_score(screen, "Player2 Lost", RED, 50)
            if self.about:
                self.display_message_score(screen, "It is an arcade Game")
            else:
                self.menu.display_frame(screen)

        elif not self.game_over:
            screen.fill((0, 0, 0))
            self.world.draw()
            # draw ghosts
            for i in range(1, 5):
                eval("self.ghost" + str(i) + ".update()")
                screen.blit(eval("self.ghost" + str(i) + ".image"), eval("self.ghost" + str(i) + ".rect"))

            self.player.move(PLAYER1_CONTROLS)
            screen.blit(self.player.img, self.player)

            if self.singleplayer:
                text = self.font.render("Score: " + str(self.player.score), True, GREEN)
                screen.blit(text, [104, 5])

            elif self.multiplayer:
                screen.blit(self.player2.img, self.player2)
                self.player2.move(PLAYER2_CONTROLS)
                text = self.font.render("P1 Score: " + str(self.player.score), True, GREEN)
                screen.blit(text, [104, 5])
                text = self.font.render("P2 Score: " + str(self.player2.score), True, GREEN)
                screen.blit(text, [512, 5])
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def display_message_score(self, screen, message, color, y):
        label = self.font.render(message, True, color)
        # Get the width and height of the label
        width = label.get_width()
        # Determine the position of the label
        posX = (800 / 2) - (width / 2)
        posY = y
        # Draw the label onto the screen
        screen.blit(label, (posX, posY))
