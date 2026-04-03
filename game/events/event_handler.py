class EventHandler:
    def __init__(self):
        self.events = []

    def add_event(self, event_id):
        self.events.append(event_id)

    def run_event(self):
        return self.events[0]

    def remove_event(self):
        self.events.pop(0)
