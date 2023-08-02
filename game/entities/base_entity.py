class BaseEntity:

    def __init__(self, _id, name, width, height, image):
        self._id = _id
        self.name = name
        self.x = 0
        self.x_speed = 1
        self.y = 0
        self.y_speed = 1
        self.width = width
        self.height = height
        self.image = image
        self.move = True

    def blit(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self, directions, delta_time):
        if self.move:
            self.x += self.x_speed * directions[0] * delta_time
            self.y += self.y_speed * directions[1] * delta_time
