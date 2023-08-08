"""
    Game
"""
import datetime
import time
from game.entities.box import Box
from game.entities.character import Character
from game.components.core.menu import Menu
import utils.json_handler as json_handler
import game.key_actions as actions
from utils.logger import Logger
from backend.input_handler import InputHandler
from backend.renderer import Renderer
from backend.font import Font
from backend.clock import Clock


class Game:
    """
        Game Class
    """

    def __init__(self, renderer, input_handler, clock):
        self.logger = Logger('game')
        self.name = 'Game Test'
        self.version = '0.0.1-alpha'
        self.state = 'title screen'
        self.input_handler: InputHandler = input_handler
        self.renderer: Renderer = renderer
        self.clock: Clock = clock
        self.font = Font(30)
        self.selected = 0
        self.components = {}

    def load(self) -> int:
        """
            Game Load function
        """
        self.logger.debug('loading fonts')
        self.load_fonts()
        self.logger.debug('finished loading fonts')
        self.logger.debug('loading components')
        self.load_components()
        self.logger.debug('finished loading components')

        return 1

    def run(self):
        """
            Game Run function
        """
        start_time = time.time()
        if actions.MAIN_GAME['PAUSE'] in self.input_handler.keys_pressed:
            self.state = 'paused'
            self.components['menu'].state = 'run'
            self.logger.info('Game is Paused')
            self.input_handler.keys_pressed.remove(
                actions.MAIN_GAME['PAUSE'])

        self.components['character'].update(self.clock.delta_time())

        # GAME LOOP
        self.renderer.clear_screen((0, 0, 0))
        self.components['character'].blit(self.renderer.screen)
        self.components['box'].blit(self.renderer.screen)
        if len(self.components['character'].paths):
            self.renderer.draw_line(
                (0, 255, 0), (self.components['character'].x,
                              self.components['character'].y),
                (self.components['character'].paths[0]))

        if len(self.components['character'].paths):
            for path in self.components['character'].paths:
                marker = self.renderer.get_surface(20, 20)
                marker.fill((0, 200, 20))
                self.renderer.screen.blit(marker, (path[0], path[1]))

        self.clock.update()
        end_time = time.time() - start_time
        true_fps = 1. / (end_time or 1)
        fps_text = self.font.fonts['main'].render(
            f'Fonts: {int(true_fps)}', 4, (255, 0, 0))
        self.renderer.screen.blit(fps_text, (50, 300))

    def pause(self):
        """
            Game Pause function
        """

        self.renderer.clear_screen((0, 0, 0))
        if self.components['menu'].state == 'run':
            self.components['menu'].run()
        elif self.components['menu'].state == 'options':
            self.components['menu'].options()
        elif self.components['menu'].state == 'end':
            self.state = self.components['menu'].game_state

        if actions.MAIN_GAME['PAUSE'] in self.input_handler.keys_pressed:
            if self.state == 'paused':
                self.state = 'running'
                self.logger.info('Game is Running')
                self.input_handler.keys_pressed.remove(
                    actions.MAIN_GAME['PAUSE'])

        game_text = self.font.fonts['main'].render(
            f'Game is paused {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
            4, (0, 255, 0))
        self.renderer.screen.blit(game_text, (50, 50))

    def title_screen(self):
        """
            Game Title Screen
        """
        if actions.MAIN_GAME['PAUSE'] in self.input_handler.keys_pressed:
            if self.components['menu'].state == 'run':
                self.state = 'end'
                self.input_handler.keys_pressed.remove(
                    actions.MAIN_GAME['PAUSE'])

        if self.components['menu'].state == 'run':
            self.components['menu'].run()
            self.state = self.components['menu'].game_state
        elif self.components['menu'].state == 'options':
            self.components['menu'].options()

    def load_components(self):
        """
            Game Pause Screen
        """
        self.components['menu']: Menu = Menu(300, 200, ['START', 'OPTIONS', 'QUIT'],
                                             self.renderer, self.input_handler,
                                             self.font, self.state)
        self.components['character']: Character = Character(
            '1', 'test', 50, 50, self.renderer.get_surface(50, 50),
            self.input_handler)
        self.components['character'].image.fill((0, 0, 255))
        self.components['box']: Box = Box(
            '2', 'box', 20, 20, self.renderer.get_surface(20, 20),
            self.input_handler)
        self.components['box'].image.fill((0, 20, 180))
        self.components['box'].x = 300
        self.components['box'].y = 300

    def load_fonts(self):
        """
            Load Font funtions
        """
        font_map = json_handler.json_to_dict(
            './game/assets/fonts/font_map.json')

        total_fonts = len(font_map)

        for index, font in enumerate(font_map):
            self.renderer.clear_screen((0, 0, 0))
            self.font.create_font(
                font['key'], f"./game/assets/fonts/{font['file_name']}", 30)
            game_text = self.font.fonts['system'].render(
                f'{index+1} / {total_fonts} loaded!', 4, (0, 255, 0))
            self.renderer.screen.blit(game_text, (50, 250))
            self.renderer.update()

    def end(self):
        """ 
            Game End function
        """
