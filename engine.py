"""
    CRT Egnine Class 
"""

from backend.clock import Clock
from backend.input_handler import InputHandler
from backend.font import Font
from backend.renderer import Renderer
from backend.audio import Audio
from game.game import Game
from utils.logger import Logger


class CrtEngine:

    """
        Engine Main Class
    """

    def __init__(self) -> None:
        self.name = 'CRT Game Engine'
        self.version = '0.0.2_pre-alpha'
        self.logger = Logger('main-engine', False, True)
        self.logger.debug('Starting program')
        self.logger.debug('Loading resources...')
        self.state = 'loading'
        self.font = Font(30)
        self.renderer = Renderer(f'{self.name} - v.{self.version}', self.font)
        self.icon = self.renderer.load_image('./assets/icon.jpg')
        self.renderer.set_icon(self.icon)
        self.input_handler = InputHandler(self.renderer)
        self.audio = Audio()
        self.clock = Clock()
        self.game = Game(self.font, self.renderer,
                         self.input_handler, self.clock, self.audio)
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
            if self.game.state == 'title screen':
                self.game.title_screen()
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
                self.game.state = 'title screen'
            else:
                self.logger.debug('Unable to load Engine')
