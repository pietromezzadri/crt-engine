from game.entities.base_entity import BaseEntity


class BoxEntity(BaseEntity):
    def __init__(self, _id, name, width, height, image):
        BaseEntity.__init__(self, _id, name, width, height, image)
        self.selected = False
        self.opened = False