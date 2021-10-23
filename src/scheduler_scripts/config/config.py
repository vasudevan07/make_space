from enum import Enum


class CustomEnum(Enum):
    @classmethod
    def list(cls):
        """
        Provides the list of values of a Enum class

        :return:
        list of Enum values
        """
        return list(map(lambda c: c.value, cls))


class Status(CustomEnum):
    BOOKED = "BOOKED"
    VACANT = "VACANT"


class InputTypes(CustomEnum):
    VACANCY_TYPE = "VACANCY"
    BOOK_TYPE = "BOOK"


class Messages(Enum):
    NO_VACANT_ROOM = "NO_VACANT_ROOM"
    INCORRECT_INPUT = "INCORRECT_INPUT"


class Constants(Enum):
    BUFFER_SLOTS = ["09:00", "13:15", "13:30", "18:45"]
    MIN_TIME_INTERVAL = 15
    MIN_PEOPLE_ALLOWED = 2
