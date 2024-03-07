from utils.format_string import format_field


class BaseEntity:

    def __init__(self, _id, name, width, height, image, input_handler):
        self._id = _id
        self.name = name
        self.x = 0
        self.x_speed = 0.3
        self.y = 0
        self.y_speed = 0.3
        self.width = width
        self.height = height
        self.image = image
        self.input_handler = input_handler
        self.can_move = True
        self.paths = []
        self.print_info_screen = False
        self.info_fields = ['_id', 'x', 'y']
        self.selected = True

    def blit(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move(self, directions, delta_time):
        if not self.can_move:
            self.x += self.x_speed * directions[0] * delta_time
            self.y += self.y_speed * directions[1] * delta_time
        else:
            self.paths = []
            self.can_move = False

    def move_to_point(self, delta_time):
        if len(self.paths):
            dist_x = self.x - self.paths[0][0]
            dist_y = self.y - self.paths[0][1]
            if abs(dist_x) > 10:
                vel_x = self.x_speed * \
                    abs(dist_x / dist_y) * -(dist_x/abs(dist_x))
                if abs(vel_x) > self.x_speed:
                    self.x += self.x_speed * vel_x / abs(vel_x) * delta_time
                else:
                    self.x += vel_x * delta_time
            if abs(dist_y) > 10:
                vel_y = self.y_speed * \
                    abs(dist_y / dist_x) * -(dist_y/abs(dist_y))
                if abs(vel_y) > self.y_speed:
                    self.y += self.y_speed * vel_y / abs(vel_y) * delta_time
                else:
                    self.y += vel_y * delta_time
            if abs(dist_x) < 10 and abs(dist_y) < 10:
                self.paths.pop(0)
                if not len(self.paths):
                    self.can_move = False

    def get_info_screen(self):
        text_to_print = []
        for field in self.info_fields:
            text_to_print.append(
                f"{field}: {format_field(getattr(self, field))}")
        return text_to_print
