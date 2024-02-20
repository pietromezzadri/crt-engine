from game.entities.base_entity import BaseEntity
from backend.physics import Physics


class Box(BaseEntity):
    def __init__(self, _id, name, width, height, image, input_handler, renderer):
        BaseEntity.__init__(self, _id, name, width,
                            height, image, input_handler, renderer)
        self.selected = False
        self.opened = False
        self.physics = Physics()

    def update(self, delta_time):
        if self.input_handler.mouse.m_left:
            if self.physics.collide_local_to_global(self.input_handler.mouse, self, \
                                                    self.input_handler.renderer.x_start, \
                                                    self.input_handler.renderer.y_start):
                self.selected = True
            else:
                self.selected = False
