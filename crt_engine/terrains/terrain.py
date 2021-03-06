import pygame

class Terrain(pygame.sprite.Sprite):

    # initial parameters
    def __init__(self, id: int, width: int = 10, height: int = 10, 
                 x: int = 0, y: int = 0) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.id: int = id
        self.width: int = width
        self.height: int = height
        self.x: int = x
        self.y: int = y
        self.type: str = ""
        self.image = pygame.Surface([self.width, self.height])
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)