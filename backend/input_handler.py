import pygame
from pygame import constants
from utils.logger import Logger
from backend.renderer import Renderer


class Mouse:
    def __init__(self, renderer) -> None:
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50
        self.m_left = False
        self.m_right = False
        self.m_middle = False
        self.renderer: Renderer = renderer

    def get_pos(self):
        return self.x, self.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_global_x(self):
        return self.renderer.local_to_global_x(self.x)

    def get_global_y(self):
        return self.renderer.local_to_global_y(self.y)

    def update_pos(self):
        self.x, self.y = pygame.mouse.get_pos()

    def update_pressed(self):
        self.m_left, self.m_middle, self.m_right = pygame.mouse.get_pressed()


class InputHandler:
    def __init__(self, renderer) -> None:
        self.logger = Logger('input-handler', False, True)
        self.renderer: Renderer = renderer
        self.keys_pressed: list = []
        self.logger.debug('InputHandler loaded!')
        self.mouse: Mouse = Mouse(self.renderer)

    def event_handler(self) -> int:
        self.mouse.update_pos()
        for event in pygame.event.get():
            self.mouse.update_pressed()
            if event.type == constants.KEYDOWN:
                self.keys_pressed.append(event.key)
            if event.type == constants.KEYUP:
                if event.key in self.keys_pressed:
                    self.keys_pressed.remove(event.key)
            if event.type == constants.QUIT:
                return 0
        return 1
