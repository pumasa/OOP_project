import pygame

state = 0


class Menu():
    """ This class is used to create a menu object to be used in a game.
    """

#############################################################################################################
    def __init__(self, items, font_color=(0, 0, 0), select_color=(255, 0, 0), ttf_font=None, font_size=25):
        """ Creates a menu object with the given parameters.

        Args:
            items (list): list of menu items
            font_color (tuple): color of the font
            select_color (tuple): color of the selected item
            ttf_font (str): path to the ttf font file
            font_size (int): size of the font
        """
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font, font_size)

#############################################################################################################
    def display_frame(self, screen):
        """ Displays the menu on the screen.

        Args:
            screen (pygame.Surface): the screen to display the menu on
        """

        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item, True, self.select_color)
            else:
                label = self.font.render(item, True, self.font_color)

            width = label.get_width()
            height = label.get_height()

            posX = (800 / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(self.items) * height
            posY = (576 / 2) - (t_h / 2) + (index * height)

            screen.blit(label, (posX, posY))

#############################################################################################################
    def event_handler(self, event):
        """ Handles the events for the menu.

        Args:
            event (pygame.event): the event to handle
        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) - 1:
                    self.state += 1
