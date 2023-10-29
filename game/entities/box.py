from game.entities.base_entity import BaseEntity


class Box(BaseEntity):
    def __init__(self, _id, name, width, height, image, input_handler):
        BaseEntity.__init__(self, _id, name, width,
                            height, image, input_handler)
        self.selected = False
        self.opened = False
