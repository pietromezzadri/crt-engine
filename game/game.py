"""
    Game
"""
import datetime
import time

from game.entities.box import Box
from game.entities.character import Character
from game.components.core.menu import Menu
from game.events.cutscene import Cutscene
import game.key_actions as actions

import utils.json_handler as json_handler
from utils.logger import Logger

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

    def __init__(self, renderer, input_handler, clock, audio):
        self.logger = Logger('game')
        self.name = 'Game Test'
        self.version = '0.0.1-alpha'
        self.state = 'title screen'
        self.state = 'title screen'
        self.input_handler: InputHandler = input_handler
        self.renderer: Renderer = renderer
        self.audio: Audio = audio
        self.clock: Clock = clock
        self.font = Font(30)
        self.selected = 0
        self.components = {}
        self.physics = Physics()
        self.cutscene = None

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

        
        self.cutscene = Cutscene(self.renderer, self.input_handler, self.audio, './game/assets/GTAtitles.mpg',
                                 './game/assets/file.mp3')

        self.clock.fps = self.renderer.get_video_fps(self.cutscene.video)

        return 1

    def run(self):
        """
            Game Run function
        """
        start_time = time.time()
        start_time = time.time()
        camera_right = False
        camera_left = False
        camera_up = False
        camera_down = False
        if actions.MAIN_GAME['PAUSE'] in self.input_handler.keys_pressed:
            self.state = 'paused'
            self.components['menu'].state = 'run'
            self.components['menu'].state = 'run'
            self.logger.info('Game is Paused')
            self.input_handler.keys_pressed.remove(
                actions.MAIN_GAME['PAUSE'])
        
        if actions.MAIN_GAME['w'] in self.input_handler.keys_pressed:
            camera_up = True
            
        if actions.MAIN_GAME['s'] in self.input_handler.keys_pressed:
            camera_down = True
            
        if actions.MAIN_GAME['a'] in self.input_handler.keys_pressed:
            camera_left = True
            
        if actions.MAIN_GAME['d'] in self.input_handler.keys_pressed:
            camera_right = True
            

        last_x = self.components['character'].x
        last_y = self.components['character'].y
        self.components['character'].update(self.clock.delta_time())

        cam_x = self.components['character'].x - last_x
        cam_y = self.components['character'].y - last_y

        
        if camera_right:
            self.renderer.x_start += 5
            self.renderer.x_end += 5
        
        elif camera_left:
            self.renderer.x_start -= 5
            self.renderer.x_end -= 5

        if camera_up:
            self.renderer.y_start -= 5
            self.renderer.y_end -= 5

        if camera_down:
            self.renderer.y_start += 5
            self.renderer.y_end += 5 

        # GAME LOOP
        self.renderer.clear_screen((0, 0, 0))
        chr_id = self.font.render_text(f"id: {self.components['character']._id}", 'main', (0,255,0))
        chr_pos_x = self.font.render_text(f"x: {self.components['character'].x:.2f}", 'main', (0,255,0))
        chr_pos_y = self.font.render_text(f"y: {self.components['character'].y:.2f}", 'main', (0,255,0))
        
        self.renderer.render_world_to_screen(chr_id, self.components['character'].x, self.components['character'].y - 100)
        self.renderer.render_world_to_screen(chr_pos_x, self.components['character'].x, self.components['character'].y - 70)
        self.renderer.render_world_to_screen(chr_pos_y, self.components['character'].x, self.components['character'].y - 40)

        self.renderer.render_world_to_screen(self.components['character'].image, self.components['character'].x, self.components['character'].y)
        self.renderer.render_world_to_screen(self.components['box'].image, self.components['box'].x, self.components['box'].y)

        if len(self.components['character'].paths):
            self.renderer.draw_line(
                (0, 255, 0), (self.components['character'].x,
                              self.components['character'].y),
                (self.components['character'].paths[0]))
            for path in self.components['character'].paths:
                marker = self.renderer.get_surface(20, 20)
                marker.fill((0, 200, 20))
                self.renderer.screen.blit(marker, (path[0], path[1]))

        self.clock.update()
        end_time = time.time() - start_time
        true_fps = int(1. / (end_time or 1))
        fps_text = self.font.render_text(f'FPS: {true_fps}', 'main', (255, 0, 0))
        self.renderer.screen.blit(fps_text, (50, 100))

        self.cutscene.run()

        if not self.cutscene.status:
            self.clock.fps = 60


    def pause(self):
        """
            Game Pause function
        """

        self.renderer.clear_screen((0, 0, 0))
        self.audio.pause_music()
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
                
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        game_text = self.font.render_text(f'Game is paused -> {current_time}',
                                        'main', (0, 255, 0))
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
            Load components
        """
        self.components['menu']: Menu = Menu(300, 200, ['START', 'OPTIONS', 'QUIT'],
                                             self.renderer, self.input_handler,
                                             self.font, self.state)
        self.components['character']: Character = Character(
            '1', 'test', 350, 350, self.renderer.get_surface(50, 50),
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
