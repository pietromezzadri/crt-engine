""" 
    Game 
"""
import game.key_actions as actions
from utils.logger import Logger
from backend.input_handler import InputHandler
from backend.renderer import Renderer
from backend.font import Font
import utils.json_handler as json_handler


class Game:
    """
        Game Class
    """

    def __init__(self, renderer, input_handler):
        self.logger = Logger('game')
        self.name = 'Game Test'
        self.version = '0.0.1'
        self.state = 'stopped'
        self.input_handler: InputHandler = input_handler
        self.renderer: Renderer = renderer
        self.font = Font(30)

    def load(self) -> int:
        """ 
            Game Load function
        """
        self.logger.debug('loading fonts')
        self.load_fonts()
        self.logger.debug('finished loading fonts')
        return 1

    def run(self):
        """ 
            Game Run function
        """
        if actions.MAIN_GAME['PAUSE'] in self.input_handler.keys_pressed:
            self.state = 'paused'
            self.input_handler.keys_pressed.remove(
                actions.MAIN_GAME['PAUSE'])
        self.renderer.clear_screen((0, 0, 0))
        game_text = self.font.fonts['main'].render(
            'Game is running', 4, (255, 0, 0))
        self.renderer.screen.blit(game_text, (50, 50))

    def pause(self):
        """ 
            Game Pause function
        """
        if actions.MAIN_GAME['PAUSE'] in self.input_handler.keys_pressed:
            if self.state == 'paused':
                self.state = 'running'
                self.input_handler.keys_pressed.remove(
                    actions.MAIN_GAME['PAUSE'])
        self.renderer.clear_screen((0, 0, 0))
        game_text = self.font.fonts['main'].render(
            'Game is paused', 4, (0, 255, 0))
        self.renderer.screen.blit(game_text, (50, 50))

    def load_fonts(self):
        """
            Load Font funtions
        """
        font_map = json_handler.json_to_dict(
            './game/assets/fonts/font_map.json')

        for font in font_map:
            self.font.create_font(
                font['key'], f"./game/assets/fonts/{font['file_name']}", 30)

    def end(self):
        """ 
            Game End function
        """
