class Camera():

    def __init__(self, _id, name, input_handler, renderer):
        self._id = _id
        self.name = name
        self.input_handler = input_handler
        self.renderer = renderer

    def goto(self, x, y):
        self.renderer.update_pos(x, y)
