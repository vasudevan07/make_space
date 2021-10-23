from .MeetingRoom import MeetingRoom


class Cave(MeetingRoom):
    name = 'C-Cave'

    def __init__(self):
        super().__init__()
        self.capacity = 3
