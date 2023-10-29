"""
    Pygame Renderer Backend
"""
import pygame
from pygame import constants
from utils.logger import Logger


class Renderer:
    """
        Pygame Renderer Backend
    """

    def __init__(self, title, width=800, height=600):
        self.logger = Logger('renderer')
        pygame.display.init()
        pygame.font.init()
        self.title = title
        self.width = width
        self.height = height
        try:
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption(self.title)
        except RuntimeError as exception:
            self.logger.error(str(exception))
        self.logger.debug('Renderer loaded!')

    def update(self):
        """
            Renderer Update function
        """
        pygame.display.flip()

    def set_icon(self, icon):
        pygame.display.set_icon(icon)

    def draw_line(self, color, start, end):
        pygame.draw.line(self.screen, color, start, end, width=3)

    def get_surface(self, width, height):
        """
            Returns a surface
        """
        return pygame.Surface((width, height))

    def update_screen_size(self, width, height):
        """
            Renderer Screen Size function
        """
        self.width = width
        self.height = height
        try:
            self.screen = pygame.display.set_mode((self.width, self.height))
        except RuntimeError as exception:
            self.logger.error(str(exception))

    def fullscreen(self, set_fullscreen=False):
        """
            Renderer fullscreen function
        """
        try:
            if set_fullscreen:
                self.screen = pygame.display.set_mode(
                    (self.width, self.width), constants.FULLSCREEN)
            else:
                self.screen = pygame.display.set_mode(
                    (self.width, self.width))
        except RuntimeError as exception:
            self.logger.error(str(exception))

    def load_image(self, image_file):
        """
            Load images
        """
        return pygame.image.load(image_file).convert()

    def clear_screen(self, color):
        """
            Renderer Clear screen
        """
        self.screen.fill(color)

    def end(self):
        """
            Renderer End function
        """
        pygame.display.quit()
