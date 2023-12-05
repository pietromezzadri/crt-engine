from game.entities.base_entity import BaseEntity


class Box(BaseEntity):
    def __init__(self, _id, name, width, height, image, input_handler, renderer):
        BaseEntity.__init__(self, _id, name, width,
                            height, image, input_handler, renderer)
        self.selected = False
        self.opened = False
