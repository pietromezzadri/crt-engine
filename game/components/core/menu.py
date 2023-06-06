import game.key_actions as actions
from utils.logger import Logger
from backend.input_handler import InputHandler
from backend.renderer import Renderer
from backend.font import Font


class Menu:
    def __init__(self, width, height, menu_items, renderer, input_handler, font, game_state):
        self._id = 0
        self.width = width
        self.height = height
        self.menu_items = menu_items
        self.selected = 0
        self.renderer: Renderer = renderer
        self.input_handler: InputHandler = input_handler
        self.font: Font = font
        self.game_state = game_state
        self.state = 'run'

    def run(self):
        if actions.MAIN_GAME['DOWN'] in self.input_handler.keys_pressed:
            self.selected += 1
            if self.selected >= 3:
                self.selected = 0
            self.input_handler.keys_pressed.remove(
                actions.MAIN_GAME['DOWN'])

        if actions.MAIN_GAME['UP'] in self.input_handler.keys_pressed:
            self.selected -= 1
            if self.selected < 0:
                self.selected = 2
            self.input_handler.keys_pressed.remove(
                actions.MAIN_GAME['UP'])

        if actions.MAIN_GAME['ENTER'] in self.input_handler.keys_pressed:
            if self.selected == 0:
                self.game_state = 'running'
                self.state = 'run'

            if self.selected == 1:
                self.state = 'options'

            elif self.selected == 2:
                self.game_state = 'end'

            self.input_handler.keys_pressed.remove(
                actions.MAIN_GAME['ENTER'])

        self.renderer.clear_screen((0, 0, 0))

        for index, text in enumerate(self.menu_items):
            color = (0, 255, 0)
            if index == self.selected:
                color = (255, 255, 0)

            text_obj = self.font.fonts['main'].render(text, 4, color)
            self.renderer.screen.blit(text_obj, (300, 100 + 50*index))

    def options(self):
        """
            Options screen
        """
        if actions.MAIN_GAME['PAUSE'] in self.input_handler.keys_pressed:
            self.state = 'run'
            self.input_handler.keys_pressed.remove(
                actions.MAIN_GAME['PAUSE'])

        if actions.MAIN_GAME['RIGHT'] in self.input_handler.keys_pressed:
            self.renderer.update_screen_size(1280, 720)
        if actions.MAIN_GAME['LEFT'] in self.input_handler.keys_pressed:
            self.renderer.update_screen_size(800, 600)

        menu_text = f'Current Resolution - [{self.renderer.width}]x[{self.renderer.height}]'
        text_obj = self.font.fonts['main'].render(menu_text, 4, (255, 255, 0))
        self.renderer.clear_screen((0, 0, 0))
        self.renderer.screen.blit(text_obj, (100, 150))
