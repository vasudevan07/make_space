from config import Constants


def is_time_slot_valid(start_time, end_time):
    """
    checks whether a time slot is valid or not
    :param start_time: str- eg: "10:00"
    :param end_time: str - eg: "12:00"
    :return: bool
    True if a time slot is valid False otherwise
    """
    try:
        # checks if the start time is always lesser than the end time
        if int(start_time.split(":")[0]) > int(end_time.split(":")[0]) or \
                start_time == end_time:
            return False

        for time_slot in [start_time, end_time]:
            hour, minute = time_slot.split(":")
            # checks whether the hour falls in the 24-hour format (0 -23) and
            # minute falls between 0 and 60 (both included)
            if not (0 <= int(hour) < 24 and minute in [f"0{val}" if val < 10 else str(val) for val in
                                                       range(0, 60, Constants.MIN_TIME_INTERVAL.value)]):
                return False

        return True

    except Exception as e:
        print(f"Error in input {e}")
        return False
