"""
Game
"""

import datetime
import time

from game.entities.camera import Camera
import game.key_actions as actions
from game.components.core.menu import MainMenu, SettingsMenu
from game.structures.map import Map

import utils.json_handler as json_handler
from utils.logger import Logger
from utils.info_screen import InfoScreen
from utils.shared import GameState, GameMode
from utils.i18n.menu import MainMenuOptions, ConfigMenuOptions

from backend.audio import Audio
from backend.input_handler import InputHandler
from backend.renderer import Renderer
from backend.font import Font
from backend.clock import Clock
from backend.physics import Physics


class Game:
    """
    Game Class
    """

    def __init__(self, font, renderer, input_handler, clock, audio):
        self.logger = Logger("game", False, True)
        self.name = "Game Test"
        self.version = "0.0.1-alpha"
        self.state = GameState.TITLE_SCREEN
        self.font: Font = font
        self.renderer: Renderer = renderer
        self.input_handler: InputHandler = input_handler
        self.audio: Audio = audio
        self.clock: Clock = clock
        self.selected = 0
        self.physics = Physics()
        self.camera = Camera(0, "main_camera")
        self.ui_components = {}
        self.entities = {}
        self.sounds = {}
        self.map = None
        self.tile_size = 100
        self.x = 3
        self.y = 1
        # self.info_screen = InfoScreen()
        self.mode = GameMode.DEBUG

    def load(self) -> int:
        """
        Game Load function
        """
        self.logger.debug("loading fonts")
        self.load_fonts()
        self.logger.debug("finished loading fonts")
        self.logger.debug("loading components")
        self.load_components()
        self.logger.debug("finished loading components")
        self.logger.debug("loading sounds")
        self.load_sounds()
        self.logger.debug("finished loading sounds")

        return 1

    def run(self):
        """
        Game Run function
        """
        start_time = time.time()
        self.renderer.clear_screen((0, 0, 0))
        mouse_x, mouse_y = self.input_handler.mouse.get_pos()
        w_mouse_x, w_mouse_y = self.renderer.local_to_global_coords(mouse_x, mouse_y)
        w_x = int(w_mouse_x / self.tile_size) * self.tile_size
        w_y = int(w_mouse_y / self.tile_size) * self.tile_size
        cx = int(w_mouse_x / self.tile_size)
        cy = int(w_mouse_y / self.tile_size)
        tc = self.map.get_chunk(cx, cy)
        tp = self.map.get_pos(cx, cy)

        if self.input_handler.mouse.m_left:
            self.map.terrain_chunks[f"{tc[0]}x{tc[1]}"][tp[1]][tp[0]] = 1
        if self.input_handler.mouse.m_right:
            self.map.terrain_chunks[f"{tc[0]}x{tc[1]}"][tp[1]][tp[0]] = 0

        if actions.MainGameAction.ZOOM_IN.value in self.input_handler.keys_pressed:
            self.tile_size += 5
            self.input_handler.keys_pressed.remove(actions.MainGameAction.ZOOM_IN.value)
        elif actions.MainGameAction.ZOOM_OUT.value in self.input_handler.keys_pressed:
            self.tile_size -= 5
            self.input_handler.keys_pressed.remove(
                actions.MainGameAction.ZOOM_OUT.value
            )

        elif (
            actions.MainGameAction.LEFT.value in self.input_handler.keys_pressed
            and int((self.x - 1) / self.map.chunk_size) >= 0
            and self.x > 0
        ):
            current_chunk = self.map.get_chunk(self.x, self.y)
            current_pos = self.map.get_pos(self.x, self.y)
            next_chunk = self.map.get_chunk(self.x - 1, self.y)
            next_pos = self.map.get_pos(self.x - 1, self.y)
            next_tile = self.map.terrain_chunks[f"{next_chunk[0]}x{next_chunk[1]}"][
                next_pos[1]
            ][next_pos[0]]
            if not next_tile:
                self.map.entity_chunks[f"{current_chunk[0]}x{current_chunk[1]}"][
                    current_pos[1]
                ][current_pos[0]] = 0
                self.map.entity_chunks[f"{next_chunk[0]}x{next_chunk[1]}"][next_pos[1]][
                    next_pos[0]
                ] = 1
                self.x -= 1
                self.sounds["wood"].play(maxtime=500)
                self.renderer.x_start = int(self.x * self.tile_size / 2)
            self.input_handler.keys_pressed.remove(actions.MainGameAction.LEFT.value)
        elif (
            actions.MainGameAction.RIGHT.value in self.input_handler.keys_pressed
            and int((self.x + 1) / self.map.chunk_size) < self.map.chunk_quantity
        ):
            current_chunk = self.map.get_chunk(self.x, self.y)
            current_pos = self.map.get_pos(self.x, self.y)
            next_chunk = self.map.get_chunk(self.x + 1, self.y)
            next_pos = self.map.get_pos(self.x + 1, self.y)
            next_tile = self.map.terrain_chunks[f"{next_chunk[0]}x{next_chunk[1]}"][
                next_pos[1]
            ][next_pos[0]]
            if not next_tile:
                self.map.entity_chunks[f"{current_chunk[0]}x{current_chunk[1]}"][
                    current_pos[1]
                ][current_pos[0]] = 0
                self.map.entity_chunks[f"{next_chunk[0]}x{next_chunk[1]}"][next_pos[1]][
                    next_pos[0]
                ] = 1
                self.x += 1
                self.sounds["wood"].play(maxtime=500)
                self.renderer.x_start = int(self.x * self.tile_size / 2)
            self.input_handler.keys_pressed.remove(actions.MainGameAction.RIGHT.value)
        elif (
            actions.MainGameAction.UP.value in self.input_handler.keys_pressed
            and int((self.y - 1) / self.map.chunk_size) >= 0
            and self.y > 0
        ):
            current_chunk = self.map.get_chunk(self.x, self.y)
            current_pos = self.map.get_pos(self.x, self.y)
            next_chunk = self.map.get_chunk(self.x, self.y - 1)
            next_pos = self.map.get_pos(self.x, self.y - 1)
            next_tile = self.map.terrain_chunks[f"{next_chunk[0]}x{next_chunk[1]}"][
                next_pos[1]
            ][next_pos[0]]
            if not next_tile:
                self.map.entity_chunks[f"{current_chunk[0]}x{current_chunk[1]}"][
                    current_pos[1]
                ][current_pos[0]] = 0
                self.map.entity_chunks[f"{next_chunk[0]}x{next_chunk[1]}"][next_pos[1]][
                    next_pos[0]
                ] = 1
                self.y -= 1
                self.sounds["wood"].play(maxtime=500)
                self.renderer.y_start = int(self.y * self.tile_size / 2)
            self.input_handler.keys_pressed.remove(actions.MainGameAction.UP.value)
        if (
            actions.MainGameAction.DOWN.value in self.input_handler.keys_pressed
            and int((self.y + 1) / self.map.chunk_size) < self.map.chunk_quantity
        ):
            current_chunk = self.map.get_chunk(self.x, self.y)
            current_pos = self.map.get_pos(self.x, self.y)
            next_chunk = self.map.get_chunk(self.x, self.y + 1)
            next_pos = self.map.get_pos(self.x, self.y + 1)
            next_tile = self.map.terrain_chunks[f"{next_chunk[0]}x{next_chunk[1]}"][
                next_pos[1]
            ][next_pos[0]]
            if not next_tile:
                self.map.entity_chunks[f"{current_chunk[0]}x{current_chunk[1]}"][
                    current_pos[1]
                ][current_pos[0]] = 0
                self.map.entity_chunks[f"{next_chunk[0]}x{next_chunk[1]}"][next_pos[1]][
                    next_pos[0]
                ] = 1
                self.y += 1
                self.sounds["wood"].play(maxtime=500)
                self.renderer.y_start = int(self.y * self.tile_size / 2)
            self.input_handler.keys_pressed.remove(actions.MainGameAction.DOWN.value)
        if actions.CameraAction.DOWN.value in self.input_handler.keys_pressed:
            self.renderer.y_start += 0.5
        if actions.CameraAction.UP.value in self.input_handler.keys_pressed:
            self.renderer.y_start -= 0.5
        if actions.CameraAction.RIGHT.value in self.input_handler.keys_pressed:
            self.renderer.x_start += 0.5
        if actions.CameraAction.LEFT.value in self.input_handler.keys_pressed:
            self.renderer.x_start -= 0.5
        if actions.CameraAction.FIND.value in self.input_handler.keys_pressed:
            self.renderer.x_start = int(self.x * self.tile_size / 2)
            self.renderer.y_start = int(self.y * self.tile_size / 2)

        current_chunk_x = int(self.x / self.map.chunk_size)
        current_chunk_y = int(self.y / self.map.chunk_size)
        current_pos_x = int(self.x % self.map.chunk_size)
        current_pos_y = int(self.y % self.map.chunk_size)
        current_x = current_chunk_x
        current_y = current_chunk_y
        if current_x + 1 >= self.map.chunk_quantity:
            next_x = current_x - 1
        else:
            next_x = current_x + 1

        if current_y + 1 >= self.map.chunk_quantity:
            next_y = current_y - 1
        else:
            next_y = current_y + 1
        chunk_list_x = [current_x, next_x]
        chunk_list_y = [current_y, next_y]
        for y in chunk_list_y:
            for x in chunk_list_x:
                self.renderer.render_terrain_map(
                    self.map.terrain_chunks[f"{x}x{y}"],
                    self.tile_size,
                    x * self.tile_size * self.map.chunk_size,
                    y * self.tile_size * self.map.chunk_size,
                )
                self.renderer.render_entity_map(
                    self.map.entity_chunks[f"{x}x{y}"],
                    self.tile_size,
                    x * self.tile_size * self.map.chunk_size - self.renderer.x_start,
                    y * self.tile_size * self.map.chunk_size - self.renderer.y_start,
                )

        self.renderer.render_selected(w_x, w_y, self.tile_size, self.tile_size, 3)

        current_chunk_x = int(self.x / self.map.chunk_size)
        current_chunk_y = int(self.y / self.map.chunk_size)
        current_pos_x = int(self.x % self.map.chunk_size)
        current_pos_y = int(self.y % self.map.chunk_size)
        info_text_1 = f"cx: {current_chunk_x} - cy: {current_chunk_y}"
        info_text_2 = f" x: {current_pos_x} -  y: {current_pos_y}"
        mouse_info = f"lx: {cx} ly: {cy} wx: {tc[0]} wy: {tc[1]}"
        text_1 = self.font.render_text(info_text_1, "main", (255, 0, 0))
        text_2 = self.font.render_text(info_text_2, "main", (255, 0, 0))
        mouse_surf = self.font.render_text(mouse_info, "main", (255, 0, 0))
        self.renderer.render_to_screen(text_1, 10, 10)
        self.renderer.render_to_screen(text_2, 10, 35)
        self.renderer.render_to_screen(mouse_surf, 10, 60)

        self.clock.fps = 60

    def pause(self):
        """
        Game Pause function
        """
        pass

    def title_screen(self):
        """
        Game Title Screen
        """
        current_index = self.ui_components["main_menu"].selected
        if actions.MenuAction.DOWN.value in self.input_handler.keys_pressed:
            if current_index + 1 >= len(self.ui_components["main_menu"].options):
                current_index = 0
            else:
                current_index += 1
            self.ui_components["main_menu"].selected = current_index
            self.input_handler.keys_pressed.remove(actions.MenuAction.DOWN.value)
        elif actions.MenuAction.UP.value in self.input_handler.keys_pressed:
            if current_index - 1 < 0:
                current_index = len(self.ui_components["main_menu"].options) - 1
            else:
                current_index -= 1
            self.ui_components["main_menu"].selected = current_index
            self.input_handler.keys_pressed.remove(actions.MenuAction.UP.value)
        elif actions.MenuAction.SELECT.value in self.input_handler.keys_pressed:
            if (
                self.ui_components["main_menu"].options[current_index]
                == MainMenuOptions.START_GAME
            ):
                self.state = GameState.RUNNING
            if (
                self.ui_components["main_menu"].options[current_index]
                == MainMenuOptions.SETTINGS
            ):
                self.state = GameState.SETTINGS
            if (
                self.ui_components["main_menu"].options[current_index]
                == MainMenuOptions.QUIT
            ):
                self.state = GameState.END
            self.input_handler.keys_pressed.remove(actions.MenuAction.SELECT.value)

        if self.ui_components["main_menu"].active:
            self.renderer.render_main_menu(self.ui_components["main_menu"])

    def settings(self):
        current_index = self.ui_components["settings_menu"].selected
        res_selected = self.ui_components["settings_menu"].res_selected
        if actions.MenuAction.PAUSE.value in self.input_handler.keys_pressed:
            if self.ui_components["settings_menu"].display_res_list:
                self.ui_components["settings_menu"].display_res_list = False
            else:
                self.state = GameState.TITLE_SCREEN
            self.input_handler.keys_pressed.remove(actions.MenuAction.PAUSE.value)
        if actions.MenuAction.DOWN.value in self.input_handler.keys_pressed:
            if self.ui_components["settings_menu"].display_res_list:
                if res_selected + 1 >= len(
                    self.ui_components["settings_menu"].res_options
                ):
                    res_selected = 0
                else:
                    res_selected += 1
                self.ui_components["settings_menu"].res_selected = res_selected
            else:
                if current_index + 1 >= len(
                    self.ui_components["settings_menu"].res_options
                ):
                    current_index = 0
                else:
                    current_index += 1
                self.ui_components["settings_menu"].selected = current_index
            self.input_handler.keys_pressed.remove(actions.MenuAction.DOWN.value)
        elif actions.MenuAction.UP.value in self.input_handler.keys_pressed:
            if self.ui_components["settings_menu"].display_res_list:
                if res_selected - 1 < 0:
                    res_selected = (
                        len(self.ui_components["settings_menu"].res_options) - 1
                    )
                else:
                    res_selected -= 1
                self.ui_components["settings_menu"].res_selected = res_selected
            else:
                if current_index - 1 < 0:
                    current_index = len(self.ui_components["settings_menu"].options) - 1
                else:
                    current_index -= 1
                self.ui_components["settings_menu"].selected = current_index
            self.input_handler.keys_pressed.remove(actions.MenuAction.UP.value)
        elif actions.MenuAction.SELECT.value in self.input_handler.keys_pressed:
            if self.ui_components["settings_menu"].display_res_list:
                new_res = self.ui_components["settings_menu"].res_options[
                    self.ui_components["settings_menu"].res_selected
                ]
                self.renderer.update_screen_size(new_res[0], new_res[1])
            if (
                self.ui_components["settings_menu"].options[current_index]
                == ConfigMenuOptions.CHANGE_RES
            ):
                self.ui_components["settings_menu"].display_res_list = True
            if (
                self.ui_components["settings_menu"].options[current_index]
                == ConfigMenuOptions.BACK
            ):
                self.state = GameState.TITLE_SCREEN
            self.input_handler.keys_pressed.remove(actions.MenuAction.SELECT.value)
        if self.ui_components["settings_menu"].active:
            self.renderer.render_settings(self.ui_components["settings_menu"])

    def load_components(self):
        """
        Load components
        """
        main_menu = MainMenu()
        settings_menu = SettingsMenu()
        settings_menu.res_options = self.renderer.get_res_list()
        self.ui_components["main_menu"] = main_menu
        self.ui_components["settings_menu"] = settings_menu
        self.map = Map(1, "main")
        self.map.load_map_data()
        self.map.create_chunks()

    def load_fonts(self):
        """
        Load Font funtions
        """
        font_map = json_handler.json_to_dict("./game/assets/fonts/font_map.json")

        total_fonts = len(font_map)

        for index, font in enumerate(font_map):
            self.renderer.clear_screen((0, 0, 0))
            self.font.create_font(
                font["key"], f"./game/assets/fonts/{font['file_name']}", 30
            )
            self.font.create_font(
                f"{font['key']}_small", f"./game/assets/fonts/{font['file_name']}", 20
            )
            font_number = self.font.render_text(
                f"{index + 1} / {total_fonts} loaded!", "system", (0, 255, 0)
            )
            font_name = self.font.render_text(font["file_name"], "system", (0, 255, 0))
            self.renderer.render_to_screen(font_number, 50, 50)
            self.renderer.render_to_screen(font_name, 50, 100)
            self.renderer.update()
            # self.clock.delay(1000)

    def load_sounds(self):
        grass_sound = self.audio.load_sound_effect("./game/assets/grass.mp3")
        self.sounds["grass"] = grass_sound
        wood_sound = self.audio.load_sound_effect("./game/assets/wood.mp3")
        self.sounds["wood"] = wood_sound

    def end(self):
        """
        Game End function
        """
