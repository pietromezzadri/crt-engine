import pygame


class Font:
    def __init__(self, size):
        pygame.font.init()
        self.normal_font = pygame.font.Font(size=size)
        self.fonts = {'system': self.normal_font}

    def create_font(self, key, path, size):
        self.fonts[key] = pygame.font.Font(path, size)

    def get_default_font(self):
        return pygame.font.get_default_font()

    def get_font_list(self):
        return pygame.font.get_fonts()
