import sys
from meeting_rooms import Cave, Tower, Mansion
from config import InputTypes, Messages, Constants
from utils import Utility


def main(rooms_dict, input_val):
    """
    Process the input value and either books a room based on vacancy or 
    provides vacant status of rooms based on the input time range. 

    :params:
    --------
    input_value:str
        get vacancy status or book a room
        eg:
            VACANCY 13:45 15:00 - To get vacant rooms between 13:45 and 15:00
            BOOK 09:30 13:15 2 - Book a room for 2 members between 9:30 to 13:15
    
    :returns:
    ----------
    - a string of room names, in case of vacancy status
    - name of the room, in case of booking 
    - NO VACANT ROOM in case of rooms with no vacancy or 
      if number of people does not fall in range of room capacity available
    - INCORRECT INPUT in case the input is not correct
    """
    try:
        # parsing the input value
        input_data = input_val.split(" ")
        input_type = input_data[0]
        start_time = input_data[1]
        end_time = input_data[2]
        num_people = int(input_data[3]) if InputTypes.BOOK_TYPE.value in str(input_val).upper() else 0

        # validating the the time range and the input type (book or vacancy)
        if not Utility.is_time_slot_valid(start_time, end_time) or \
                input_type.strip() not in InputTypes.list():
            return Messages.INCORRECT_INPUT.value

        max_room_capacity = rooms_dict[max(rooms_dict, key=lambda x: rooms_dict[x])].capacity
        min_room_capacity = Constants.MIN_PEOPLE_ALLOWED.value
        vacant_rooms = sorted([room for _, room in rooms_dict.items() if
                               not room.fully_booked and room.is_vacant(start_time, end_time)])

        # validates if a room is vacant and if the number of people fall within the rooms capacity range
        if (
                input_type == InputTypes.BOOK_TYPE.value and
                (
                        (num_people < min_room_capacity) or
                        (num_people > max_room_capacity)
                )
        ) or not vacant_rooms:
            return Messages.NO_VACANT_ROOM.value

        # processes the input types and returns the appropriate output
        if input_type.upper() == InputTypes.VACANCY_TYPE.value:

            return " ".join([room.name for room in vacant_rooms])

        elif input_type.upper() == InputTypes.BOOK_TYPE.value:
            for room in vacant_rooms:
                if num_people <= room:
                    room.book_room(start_time, end_time)
                    return room.name

    except Exception as e:
        print(f"Error occurred {e}")
        return Messages.INCORRECT_INPUT.value

    return Messages.INCORRECT_INPUT.value


if __name__ == '__main__':
    file_path = sys.argv[1]

    with open(file_path, 'r') as f:
        inputs = f.readlines()

    rooms = dict(cave=Cave(), tower=Tower(), mansion=Mansion())

    for input_value in inputs:
        input_value = input_value.strip()
        if input_value:
            print(main(rooms, input_value))
