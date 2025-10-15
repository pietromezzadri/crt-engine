"""
    Pygame Renderer Backend
"""
import pygame
import cv2
from pygame import constants
from utils.logger import Logger
from backend.font import Font
from game.components.core.menu import MainMenu, SettingsMenu
from game.structures.map import Map


class Renderer:
    """
    Pygame Renderer Backend
    """

    def __init__(self, title, font, width=800, height=600):
        self.logger = Logger("renderer", False, True)
        pygame.display.init()
        self.font: Font = font
        self.title = title
        self.width = width
        self.height = height
        self.x_start = 0
        self.x_end = self.width
        self.y_start = 0
        self.y_end = self.height
        try:
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption(self.title)
            self.icon = self.load_image("./assets/icon.jpg")
            pygame.display.set_icon(self.icon)

        except RuntimeError as exception:
            self.logger.error(str(exception))
        self.logger.debug("Renderer loaded!")

    def update(self):
        """
        Renderer Update function
        """
        pygame.display.flip()

    def local_to_global_x(self, local_x):
        return local_x + self.x_start

    def local_to_global_y(self, local_y):
        return local_y + self.y_start

    def global_to_local_x(self, world_x):
        return world_x - self.x_start

    def global_to_local_y(self, world_y):
        return world_y - self.y_start

    def local_to_global_coords(self, local_x, local_y):
        """
        Returns global coords from local
        """
        world_x = local_x + self.x_start
        world_y = local_y + self.y_start
        return (world_x, world_y)

    def global_to_local_coords(self, world_x, world_y):
        """
        Returns local coords from global
        """
        local_x = world_x - self.x_start
        local_y = world_y - self.y_start
        return (local_x, local_y)

    def render_world_to_screen(self, surface, world_x, world_y):
        """
        Transform world coords to local coords
        """
        local_x = world_x - self.x_start
        local_y = world_y - self.y_start
        self.screen.blit(surface, (local_x, local_y))

    def render_info_to_screen(self, entity, spacing=15):
        """
        Render entity info to screen
        """
        info_text_list = entity.get_info_screen()
        total_items = len(entity.info_fields)

        for index, info in enumerate(info_text_list):
            text = self.font.render_text(info, "main_small", (150, 50, 50))
            self.render_world_to_screen(
                text,
                entity.x,
                entity.y - (spacing * (total_items - index)) - (50 - spacing),
            )

    def render_selected(self, x, y, width, height, border):
        local_coords = self.global_to_local_coords(x, y)
        pygame.draw.rect(
            self.screen,
            (235, 50, 50),
            (
                local_coords[0] - border,
                local_coords[1] - border,
                width + border,
                height + border,
            ),
            border,
        )

    def render_to_screen(self, surface, x, y):
        """
        Render using local coords
        """
        self.screen.blit(surface, (x, y))

    def set_icon(self, icon):
        pygame.display.set_icon(icon)

    def draw_line(self, color, start, end):
        pygame.draw.line(self.screen, color, start, end, width=3)

    def draw_circle(self, color, x, y, radius):
        pygame.draw.circle(self.screen, color, (x, y), radius)

    def get_surface(self, width, height):
        """
        Returns a surface
        """
        return pygame.Surface((width, height))

    def update_pos(self, x, y):
        """
        Update Rendered Area
        """
        self.x_start = x
        self.x_end = x + self.width
        self.y_start = y
        self.y_end = y + self.height

    def update_screen_size(self, width, height):
        """
        Renderer Screen Size function
        """
        self.x_end += width - self.width
        self.y_end += height - self.height

        self.width = width
        self.height = height
        try:
            self.screen = pygame.display.set_mode((self.width, self.height))
        except RuntimeError as exception:
            self.logger.error(str(exception))

    def render_terrain_map(self, map: list, tile_size, x_offset=0, y_offset=0):
        for y_index, y in enumerate(map):
            for x_index, x in enumerate(map[y_index]):
                tile = self.get_surface(tile_size, tile_size)
                if not x:
                    tile.fill((0, 0, 150))
                else:
                    tile.fill((255, 255, 255))
                self.render_world_to_screen(
                    tile, x_index * tile_size + x_offset, y_index * tile_size + y_offset
                )

    def render_entity_map(self, map: list, tile_size, x_offset=0, y_offset=0):
        for y_index, y in enumerate(map):
            for x_index, x in enumerate(map[y_index]):
                if x:
                    self.draw_circle(
                        (120, 0, 120),
                        x_index * tile_size + x_offset + int(tile_size / 2),
                        y_index * tile_size + y_offset + int(tile_size / 2),
                        int(tile_size / 2),
                    )

    def render_main_menu(self, main_menu: MainMenu):
        self.clear_screen((0, 0, 0))
        for index, option in enumerate(main_menu.options):
            if index == main_menu.selected:
                option_text = self.font.render_text(option.value, "main", (0, 255, 0))
            else:
                option_text = self.font.render_text(option.value, "main", (255, 0, 0))
            self.render_to_screen(option_text, 100, 100 + index * 50)

    def render_res_list(
        self, item_list: list, selected, spacing, x_offset=0, y_offset=0
    ):
        surface = self.get_surface(200, 200)
        current_res = (self.width, self.height)
        y_offset = selected * spacing
        for index, item in enumerate(item_list):
            if item == current_res or index == selected:
                item_text = self.font.render_text(
                    f"{item[0]}x{item[1]}", "main", (0, 255, 0)
                )
            else:
                item_text = self.font.render_text(
                    f"{item[0]}x{item[1]}", "main", (255, 0, 0)
                )
            surface.blit(item_text, (30 + x_offset, 80 + index * spacing - y_offset))

        return surface

    def render_settings(self, settings_menu: SettingsMenu, x_offset=0, y_offset=0):
        self.clear_screen((0, 0, 0))
        for index, option in enumerate(settings_menu.options):
            if not index and settings_menu.display_res_list:
                res_list = self.render_res_list(
                    settings_menu.res_options,
                    settings_menu.res_selected,
                    30,
                    x_offset,
                    y_offset,
                )
                pygame.draw.rect(
                    self.screen,
                    (255, 0, 0),
                    pygame.Rect(195, 195, 210, 210),
                    border_radius=3,
                )
                self.render_to_screen(res_list, 200, 200)
            if index == settings_menu.selected:
                option_text = self.font.render_text(option.value, "main", (0, 255, 0))
            else:
                option_text = self.font.render_text(option.value, "main", (255, 0, 0))
            self.render_to_screen(option_text, 100, 100 + index * 50)

    def get_res_list(self):
        return pygame.display.list_modes()

    def fullscreen(self, set_fullscreen=False):
        """
        Renderer fullscreen function
        """
        try:
            if set_fullscreen:
                self.screen = pygame.display.set_mode(
                    (self.width, self.width), constants.FULLSCREEN
                )
            else:
                self.screen = pygame.display.set_mode((self.width, self.width))
        except RuntimeError as exception:
            self.logger.error(str(exception))

    def load_image(self, image_file):
        """
        Load images
        """
        return pygame.image.load(image_file).convert()

    def load_video(self, video_file):
        """
        Load videos
        """
        return cv2.VideoCapture(video_file)

    def get_video_data(self, video_image):
        """
        Get video byte data
        """
        return pygame.image.frombuffer(
            video_image.tobytes(), video_image.shape[1::-1], "BGR"
        )

    def get_video_fps(self, video):
        return video.get(cv2.CAP_PROP_FPS)

    def clear_screen(self, color):
        """
        Renderer Clear screen
        """
        self.screen.fill(color)

    def end(self):
        """
        Renderer End function
        """
        pygame.display.quit()
