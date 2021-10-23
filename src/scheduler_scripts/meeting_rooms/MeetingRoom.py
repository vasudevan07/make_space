from config import Status, Constants


class MeetingRoom:

    # Util methods
    @staticmethod
    def is_buffer_slot(slot):
        """
        checks if a time slot falls in buffer time meant for cleaning rooms
        :param slot: str - time range eg: "10:00", "12:45" etc.
        :return: bool
        True if slot in buffer False otherwise
        """
        return slot in Constants.BUFFER_SLOTS.value

    @staticmethod
    def get_slot_value(hour, minute):
        """
        creates a slot value from hour and minute value provided
        :param hour: int - hour value eg:1,10, 23
        :param minute: int - minute value eg:10, 59
        :return: str
        a string of time slot value. eg: "10:00", "19:45" etc.
        """
        return f"{hour if hour > 9 else f'0{hour}'}:{minute or '00'}"

    @staticmethod
    def create_calendar():
        """
        Creates a dictionary of time_slot: status for a meeting room.
        Defaults  status to "BOOKED" for buffer time slot
        :return: dict
            :key (str) - time slot. eg: "10:00" etc.
            :value (str) - status eg: "VACANT", "BOOKED"
        """
        scheduler = {}
        for hour in range(0, 24):
            for minute in range(0, 60, 15):
                slot = MeetingRoom.get_slot_value(hour, minute)
                if MeetingRoom.is_buffer_slot(slot):
                    scheduler[slot] = Status.BOOKED.value
                else:
                    scheduler[slot] = Status.VACANT.value

        return scheduler

    @staticmethod
    def get_time_range(start_time, end_time):
        """
        to generate all time slots within a time range.
        :param start_time: str- eg: "10:00"
        :param end_time: str - eg: "12:00"
        :return: list
        a list of all time slots between the range of start_time and end_time
        """
        time_range = []
        start_time_split = start_time.split(":")
        end_time_split = end_time.split(":")
        start_hour, start_minute = int(start_time_split[0]), int(start_time_split[1])
        end_hour, end_minute = int(end_time_split[0]), int(end_time_split[1])

        for hour in range(start_hour, end_hour + 1):
            for minute in range(0, 60, Constants.MIN_TIME_INTERVAL.value):
                if (hour == start_hour and minute < start_minute) or \
                        (hour == end_hour and minute >= end_minute):
                    continue
                time_range.append(MeetingRoom.get_slot_value(hour, minute))

        return time_range

    # Instance methods
    def __init__(self):
        # creating the calendar once initiated
        self.scheduler = self.create_calendar()
        self.fully_booked = False  # to keep track if all slots of a room are booked
        self.capacity = 0

    def is_vacant(self, start_time, end_time):
        """
        checks if a room is vacant or not
        :param start_time: str -  eg: "10:00"
        :param end_time: str - eg: "12:00"
        :return: bool
        True if a room is vacant False otherwise
        """
        time_range = self.get_time_range(start_time, end_time)

        return all(self.scheduler[slot] == Status.VACANT.value for slot in time_range)

    def book_room(self, start_time, end_time):
        """
        books a room in the given time range
        :param start_time: str -  eg: "10:00"
        :param end_time: str - eg: "12:00"
        :return: None
        """
        if self.is_vacant(start_time, end_time):
            time_range = self.get_time_range(start_time, end_time)

            for slot in time_range:
                self.scheduler[slot] = Status.BOOKED.value

            # if all slots of a room are booked, then changes the fully_booked flag to True
            if len(set(self.scheduler.values())) == 1:
                self.fully_booked = True

    # Operator overloading methods
    def __ge__(self, other):
        if isinstance(other, MeetingRoom):
            return self.capacity >= other.capacity
        else:
            return self.capacity >= other

    def __le__(self, other):
        if isinstance(other, MeetingRoom):
            return self.capacity <= other.capacity
        else:
            return self.capacity <= other

    def __gt__(self, other):
        if isinstance(other, MeetingRoom):
            return self.capacity > other.capacity
        else:
            return self.capacity > other

    def __lt__(self, other):
        if isinstance(other, MeetingRoom):
            return self.capacity < other.capacity
        else:
            return self.capacity < other
