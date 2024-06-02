import pygame


class Clock:

    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.v_sync = True
        self.fps = 60

    def set_fps(self, fps):
        self.fps = fps

    def delta_time(self):
        return self.clock.get_time()

    def update(self):
        self.clock.tick(self.fps)

    def delay(self, wait_time):
        pygame.time.delay(wait_time)
