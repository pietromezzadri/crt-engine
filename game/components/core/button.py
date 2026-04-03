class Button:
    def __init__(self, button_id, state, event_id, label):
        self._id = button_id
        self.state = state
        self.selected = False
        self.event_id = event_id
        self.label = label
