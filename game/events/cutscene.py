from backend.renderer import Renderer
from backend.input_handler import InputHandler
from backend.audio import Audio

from utils.logger import Logger

import game.key_actions as actions

class Cutscene:
    def __init__(self, renderer, input_handler, audio,
                 video_file, music_file, subtitles = None) -> None:
        self.logger = Logger('cutscene')
        self.renderer: Renderer = renderer
        self.input_handler: InputHandler = input_handler
        self.audio: Audio = audio
        self.logger.info('loading files')
        self.video = self.renderer.load_video(video_file)
        self.music = self.audio.load_music_file(music_file)
        self.logger.info('finished loading!')
        self.subtitles = subtitles
        self.status = False

    def get_video_frame(self):
        self.status, video_image = self.video.read()
        if self.status:
            return self.renderer.get_video_data(video_image)
        self.status = False
        return self.renderer.get_surface(10, 10)
    
    def run(self):
        if actions.MAIN_GAME['skip'] in self.input_handler.keys_pressed:
            self.logger.info('Stopping cutscene')
            self.video.release()
            self.input_handler.keys_pressed.remove(actions.MAIN_GAME['skip'])
        video_frame = self.get_video_frame()
        if self.status:
            self.renderer.screen.blit(video_frame, (0, 0))
            self.audio.play_music()
        else:
            self.audio.stop_music()