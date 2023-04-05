"""
    CRT Egnine Class 
"""

from utils.logger import Logger
from renderer import Renderer
from input_handler import InputHandler
from game.game import Game


class CrtEngine:

    """
        Engine Main Class
    """

    def __init__(self) -> None:
        self.name = 'CRT Game Engine'
        self.version = '0.0.1'
        self.logger = Logger('main-engine')
        self.logger.debug('Starting program')
        self.logger.debug('Loading resources...')
        self.state = 'loading'
        self.renderer = Renderer(f'{self.name} - v.{self.version}')
        self.input_handler = InputHandler()
        self.game = Game(self.renderer, self.input_handler)
        self.logger.debug('Finished Loading!')
        self.state = 'running'
        self.fullscreen = False

    def run(self) -> None:
        """
            Engine  main loop
        """

        while self.state == 'running':
            if not self.input_handler.event_handler():
                self.renderer.end()
                break
            if self.game.state == 'running':
                self.game.run()
            if self.game.state == 'paused':
                self.game.pause()
            if self.game.state == 'end':
                self.game.end()
                self.renderer.end()
                break
            self.renderer.update()
        self.renderer.end()
        self.logger.debug('Ending program')

    def load(self) -> int:
        """
            Engine  load function
        """
        if self.game:
            self.logger.debug('Start Loading Game...')
            if self.game.load():
                self.logger.debug('Finished Loading Game...')
                self.game.state = 'running'
                self.run()
            else:
                self.logger.debug('Unable to load Engine')
