import pygame

class Audio:
    def __init__(self) -> None:
        pygame.mixer.init()
        self.num_channels = 8
        self.playing = False
        self.paused = False

    def load_music_file(self, file_name):
        pygame.mixer.music.load(file_name)

    def play_music(self):
        if not self.playing:
            pygame.mixer.music.play()
            self.playing = True
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def stop_music(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False

    def pause_music(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True