from game.entities.base_entity import BaseEntity


class Character(BaseEntity):
    def __init__(self, _id, name, width, height, image):
        BaseEntity.__init__(self, _id, name, width, height, image)
        self.health = 100
        self.defense = 0
        self.control = False
        self.movement_images = []