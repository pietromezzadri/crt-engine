import pygame
from pygame import constants
from utils.logger import Logger


class InputHandler:
    def __init__(self) -> None:
        self.logger = Logger('input-handler')
        self.keys_pressed: list = []
        self.logger.debug('InputHandler loaded!')

    def event_handler(self) -> int:
        for event in pygame.event.get():
            if event.type == constants.KEYDOWN:
                self.keys_pressed.append(event.key)
            if event.type == constants.KEYUP:
                if event.key in self.keys_pressed:
                    self.keys_pressed.remove(event.key)
            if event.type == constants.QUIT:
                return 0
        return 1
