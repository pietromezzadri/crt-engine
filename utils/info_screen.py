from backend.renderer import Renderer

class InfoScreen:

    def __init__(self, renderer) -> None:
        self.fps = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.renderer: Renderer = renderer
        self.show = False
        self.components = []

    def display_info(self):
        if len(self.components):
            for component in self.components:
                self.renderer.blit(component.image, component.pos)