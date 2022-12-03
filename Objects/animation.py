import pygame


class Animation():
    """ This class handles the animation by loading images from the sprite sheet and creating a list of images.
    It also updates the current image based on the fps.
    """
#############################################################################################################
    def __init__(self, img, width, height):
        """ Initialize the animation.

        Args:
            img (pygame.Surface): The sprite sheet.
            width (int): The width of each frame.
            height (int): The height of each frame.
        """

        self.sprite_sheet = img
        self.image_list = []
        self.load_images(width, height)
        self.index = 0
        self.clock = 1

#############################################################################################################
    def load_images(self, width, height):
        """ Loads all the images from the sprite sheet.

        Args:
            width (int): The width of each frame.
            height (int): The height of each frame.
        """

        for y in range(0, self.sprite_sheet.get_height(), height):
            for x in range(0, self.sprite_sheet.get_width(), width):
                img = self.get_image(x, y, width, height)
                self.image_list.append(img)

#############################################################################################################
    def get_image(self, x, y, width, height):
        """ Get an individual image from the sprite sheet.

        Args:
            x (int): The x coordinate of the image on the sprite sheet.
            y (int): The y coordinate of the image on the sprite sheet.
            width (int): The width of each frame.
            height (int): The height of each frame.

        Returns:
            A pygame.Surface with the image loaded onto it.
        """

        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))
        return image

#############################################################################################################
    def get_current_image(self):
        """ Get the current image of the animation.

        Returns:
            A pygame.Surface with the image loaded onto it.
        """

        return self.image_list[self.index]

#############################################################################################################
    def get_length(self):
        """ Get the length of the animation.

        Returns:
            The length of the animation (int).
        """

        return len(self.image_list)

#############################################################################################################
    def update(self, fps=30):
        """ Updates the animation.

        Args:
            fps (int): The frames per second of the animation.
        """

        step = 30 // fps
        l_range = range(1, 30, step)
        if self.clock == 30:
            self.clock = 1
        else:
            self.clock += 1

        if self.clock in l_range:
            # Increase index
            self.index += 1
            if self.index == len(self.image_list):
                self.index = 0
