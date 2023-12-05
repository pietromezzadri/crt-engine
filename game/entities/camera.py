from game.entities.base_entity import BaseEntity

class Camera(BaseEntity):

    def __init__(self, _id, name, width, height, image, input_handler, renderer):
        BaseEntity.__init__(_id, name, width, height, image, input_handler, renderer)
