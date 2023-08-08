import game.key_actions as actions
from backend.input_handler import InputHandler
from backend.renderer import Renderer
from backend.font import Font


class Menu:
    def __init__(self, width, height, menu_items,
                 renderer, input_handler, font, game_state):
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

        if actions.MAIN_GAME['ENTER'] in self.input_handler.keys_pressed \
                or self.input_handler.mouse.m_left:
            if self.selected == 0:
                self.input_handler.mouse.m_left = False
                self.game_state = 'running'
                self.state = 'end'

            if self.selected == 1:
                self.state = 'options'

            elif self.selected == 2:
                self.game_state = 'end'
                self.state = 'end'

            if actions.MAIN_GAME['ENTER'] in self.input_handler.keys_pressed:
                self.input_handler.keys_pressed.remove(
                    actions.MAIN_GAME['ENTER'])

        self.renderer.clear_screen((0, 0, 0))

        mouse_x = self.font.fonts['main'].render(
            f"X: {self.input_handler.mouse.get_x()}", 2, (255, 255, 255))
        mouse_y = self.font.fonts['main'].render(
            f"Y: {self.input_handler.mouse.get_y()}", 2, (255, 255, 255))
        self.renderer.screen.blit(mouse_x, (50, 300))
        self.renderer.screen.blit(mouse_y, (50, 400))

        for index, text in enumerate(self.menu_items):
            color = (0, 255, 0)
            if index == self.selected:
                color = (255, 255, 0)

            text_obj = self.font.fonts['main'].render(text, 4, color)
            screen_middle = int(self.renderer.width / 2)
            menu_width = screen_middle - int(text_obj.get_width() / 2)
            self.renderer.screen.blit(text_obj, (menu_width, 100 + 50*index))
            text_obj_x = menu_width
            text_obj_y = 100 + 50*index
            text_obj_w = text_obj.get_width()
            text_obj_h = text_obj.get_height()
            if self.input_handler.mouse.get_x() >= text_obj_x \
                    and self.input_handler.mouse.get_x() <= text_obj_x + text_obj_w \
                    and self.input_handler.mouse.get_y() >= text_obj_y \
                    and self.input_handler.mouse.get_y() <= text_obj_y + text_obj_h:
                self.selected = index

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

        menu_text = f'Current Resolution - [{self.renderer.width}]' + \
            f'x[{self.renderer.height}]'
        text_obj = self.font.fonts['main'].render(menu_text, 4, (255, 255, 0))
        self.renderer.clear_screen((0, 0, 0))
        screen_middle = int(self.renderer.width / 2)
        menu_width = screen_middle - int(text_obj.get_width() / 2)
        self.renderer.screen.blit(text_obj, (menu_width, 150))
