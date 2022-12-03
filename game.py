import pygame
import json
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
    """This class is used to create a game object that can be used in Pygame.
    """

#############################################################################################################
    def __init__(self):
        """ Initialize the game
        """

        self.font = pygame.font.Font('freesansbold.ttf', 40)
        self.names = False
        self.game_over = True
        self.singleplayer = False
        self.multiplayer = False
        self.p1_dead = False
        self.username = None
        self.username2 = None
        self.saved = False

        self.world = World(enviroment())
        self.player = Player(32, 32, 29, 29)
        self.player.world = self.world
        self.ghosts = pygame.sprite.Group()
        self.ghosts.add = Ghost(544, 288, -2, 0)
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
        self.menu = Menu(("Single Player", "Multi Player", "Exit"), font_color=WHITE, font_size=60)

#############################################################################################################
    def process_events(self):
        """ Process the events of the game
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            self.menu.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over and not self.names:
                        if self.menu.state == 0:

                            # ---- Single Player ------
                            self.__init__()
                            self.game_over = False
                            self.menu = Menu(("Restart", "Multi Player", "Exit"), font_color=WHITE, font_size=60)
                            self.singleplayer = True
                            self.multiplayer = False

                        elif self.menu.state == 1:
                            # ---- Multi Player ------
                            self.__init__()
                            self.game_over = False
                            self.singleplayer = False
                            self.multiplayer = True
                            self.p2_dead = False
                            self.menu = Menu(("Single Player", "Restart", "Exit"), font_color=WHITE, font_size=60)
                            self.player2 = Player(736, 448, 29, 29)
                            self.player2.world = self.world
                            # self.player2 = Player(64, 32, 29, 29)

                        elif self.menu.state == 3:
                            # --- Name Enter ------
                            self.names = True

                        elif self.menu.state == 2:
                            # --- EXIT -------
                            # User clicked exit
                            return True

                if event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    self.names = False
        return False

    def draw_name(self):
        screen.fill((0, 0, 0))
        self.display_message_score(screen, "Enter your username:", WHITE, 250)
        pygame.display.flip()

#############################################################################################################
    def run_logic(self):
        """ Run the logic of the game
        """

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
                    self.pacman_sound.play()
                    self.player.score += 10
                    self.world.coin_list.remove(coin)
                if coin[1].colliderect(Rect(self.player2.rect)):
                    self.pacman_sound.play()
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

#############################################################################################################
    def display_frame(self, screen):
        """ Display everything to the screen for the game.
        """

        screen.fill(BLACK)
        # --- Drawing code should go here
        if self.game_over:
            if self.singleplayer:
                if self.saved is False:
                    self.game_over_sound
                    self.save()
                    self.saved = True
                self.display_message_score(screen, "Your Score: " + str(self.player.score), GREEN, 80)
            if self.multiplayer:
                if self.saved is False:
                    if self.p1_dead:
                        self.game_over_sound
                        self.player2.score += 1000
                    elif self.p2_dead:
                        self.game_over_sound
                        self.player.score += 1000
                    self.save()
                    self.saved = True
                self.display_message_score(screen, self.username + "'s Score: " + str(self.player.score), GREEN, 80)
                self.display_message_score(screen, self.username2 + "'s Score: " + str(self.player2.score), GREEN, 110)
                if self.p1_dead:
                    self.display_message_score(screen, self.username + " Lost", RED, 50)
                elif self.p2_dead:
                    self.display_message_score(screen, self.username2 + " Lost", RED, 50)
            if self.names:
                screen.fill((0, 0, 0))
                self.display_message_score(screen, "Enter your username:", WHITE, 250)
            else:
                self.menu.display_frame(screen)

        elif not self.game_over:
            # Username p1
            if self.username is None:
                self.username = self.define_username(1)
            # Username p2
            elif self.multiplayer and self.username2 is None:
                self.username2 = self.define_username(2)

            else:
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

#############################################################################################################
    def display_message_score(self, screen, message, color, y):
        """ Display a message on the screen

        Args:
            screen: the screen to display the message on
            message: the message to display
            color: the color of the message
            y: the y position of the message
        """

        label = self.font.render(message, True, color)
        # Get the width and height of the label
        width = label.get_width()
        # Determine the position of the label
        posX = (800 / 2) - (width / 2)
        posY = y
        # Draw the label onto the screen
        screen.blit(label, (posX, posY))

#############################################################################################################
    def define_username(self, num):
        """Defines the username

        Args:
            num (int): Player number
        """
        username = ""
        typing = True
        while typing:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():
                        username += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    elif event.key == pygame.K_RETURN:
                        typing = False
                        return username
                screen.fill((0, 0, 0))
                if num == 1:
                    self.display_message_score(screen, "Enter Player name:", WHITE, 250)
                elif num == 2:
                    self.display_message_score(screen, "Enter Player 2 name:", WHITE, 250)
                text = self.font.render(username, True, WHITE)
                screen.blit(text, (350, 300))
                pygame.display.update()

#############################################################################################################
    def save(self):
        """Save the highscore to a file
        """

        if self.singleplayer:
            with open("scores.json", "r") as f:
                scores = json.load(f)
                scores["single_player"].append({"player_name": self.username, "score": self.player.score})
            with open("scores.json", "w") as f:
                json.dump(scores, f)
        elif self.multiplayer:
            with open("scores.json", "r") as f:
                scores = json.load(f)
                scores["multi_player"].append({"player_name": self.username, "score": self.player.score})
                scores["multi_player"].append({"player_name": self.username2, "score": self.player2.score})
            with open("scores.json", "w") as f:
                json.dump(scores, f)
