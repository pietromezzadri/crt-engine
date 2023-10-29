import game.key_actions as actions
from game.entities.base_entity import BaseEntity


class Character(BaseEntity):
    def __init__(self, _id, name, width, height, image, input_handler):
        BaseEntity.__init__(self, _id, name, width,
                            height, image, input_handler)
        self.health = 100
        self.defense = 0
        self.control = False
        self.movement_images = []

    def update(self, delta_time):
        if actions.MAIN_GAME['d'] in self.input_handler.keys_pressed:
            self.move(
                [1, 0], delta_time)
        if actions.MAIN_GAME['a'] in self.input_handler.keys_pressed:
            self.move(
                [-1, 0], delta_time)
        if actions.MAIN_GAME['w'] in self.input_handler.keys_pressed:
            self.move(
                [0, -1], delta_time)
        if actions.MAIN_GAME['s'] in self.input_handler.keys_pressed:
            self.move(
                [0, 1], delta_time)
        if actions.MAIN_GAME['c'] in self.input_handler.keys_pressed:
            self.paths = []

        if self.input_handler.mouse.m_left:
            self.can_move = True
            self.paths.append((self.input_handler.mouse.get_x(),
                               self.input_handler.mouse.get_y()))

        if self.can_move:
            self.move_to_point(delta_time)
