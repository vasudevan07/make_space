from .MeetingRoom import MeetingRoom


class Tower(MeetingRoom):
    name = 'D-Tower'

    def __init__(self):
        super().__init__()
        self.capacity = 7
