import pygame


class Font:
    def __init__(self, size):
        pygame.font.init()
        self.normal_font = pygame.font.Font(size=size)
        self.fonts = {'system': self.normal_font}

    def create_font(self, key, path, size):
        self.fonts[key] = pygame.font.Font(path, size)
