class Objective:

    def __init__(self) -> None:
        self.state = 'todo'
        objetive_type = {
            'id': '',
            'state': '',
            'name': '',
            'description': '',
            'reward': ''
        }
        self.objectives: [objetive_type] = []
