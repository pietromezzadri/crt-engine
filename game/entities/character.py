import game.key_actions as actions
from game.entities.base_entity import BaseEntity
from backend.physics import Physics


class Character(BaseEntity):
    def __init__(self, _id, name, width, height, image, input_handler):
        BaseEntity.__init__(self, _id, name, width,
                            height, image, input_handler)
        self.health = 100
        self.defense = 0
        self.control = False
        self.movement_images = []
        self.physics = Physics()

    def update(self, delta_time):
        if self.control:
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
            if actions.MAIN_GAME['shift'] in self.input_handler.keys_pressed:
                self.x_speed = 0.6
                self.y_speed = 0.6
            else:
                self.x_speed = 0.3
                self.y_speed = 0.3    
            
        if actions.MAIN_GAME['c'] in self.input_handler.keys_pressed:
            self.paths = []

        if self.input_handler.mouse.m_right:
            self.can_move = True
            self.paths.append((self.input_handler.mouse.get_global_x(),
                               self.input_handler.mouse.get_global_y()))
            
        if self.input_handler.mouse.m_left:
            if self.physics.collide_local_to_global(self.input_handler.mouse, self, \
                                                    self.input_handler.renderer.x_start, \
                                                    self.input_handler.renderer.y_start):
                self.selected = True
            elif actions.MAIN_GAME['shift'] not in self.input_handler.keys_pressed:
                self.selected = False

        if self.can_move:
            self.move_to_point(delta_time)
