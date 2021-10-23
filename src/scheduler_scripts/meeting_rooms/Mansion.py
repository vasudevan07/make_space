from .MeetingRoom import MeetingRoom


class Mansion(MeetingRoom):
    name = 'G-Mansion'

    def __init__(self):
        super().__init__()
        self.capacity = 20
