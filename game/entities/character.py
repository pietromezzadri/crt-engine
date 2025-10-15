import game.key_actions as actions
from game.entities.base_entity import BaseEntity
from backend.physics import Physics


class Character(BaseEntity):
    def __init__(self, _id, name, width, height, image, input_handler):
        BaseEntity.__init__(self, _id, name, width, height, image, input_handler)
        self.base_health = 100
        self.defense = 0
        self.control = False
        self.movement_images = []
        self.physics = Physics()

    def update(self, delta_time):
        pass
