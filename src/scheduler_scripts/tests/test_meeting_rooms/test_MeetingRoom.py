import unittest
from random import choice
from config import Constants, Status


class TestMeetingRoom(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from meeting_rooms import MeetingRoom
        cls.module = MeetingRoom()

    def setUp(self):
        self.test_slots = ['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45',
                           '02:00', '02:15', '02:30', '02:45', '03:00', '03:15', '03:30', '03:45',
                           '04:00', '04:15', '04:30', '04:45', '05:00', '05:15', '05:30', '05:45',
                           '06:00', '06:15', '06:30', '06:45', '07:00', '07:15', '07:30', '07:45',
                           '08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45',
                           '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45',
                           '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45',
                           '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45',
                           '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45',
                           '18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '19:45',
                           '20:00', '20:15', '20:30', '20:45', '21:00', '21:15', '21:30', '21:45',
                           '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30', '23:45']

        self.test_calender = {item: Status.VACANT.value
                              if item not in Constants.BUFFER_SLOTS.value
                              else Status.BOOKED.value
                              for item in self.test_slots
                              }

        self.non_buffer_slots = [slot for slot in self.test_slots if slot not in Constants.BUFFER_SLOTS.value]

    def test_buffer_slot(self):

        test_slot = choice(self.test_slots)
        self.assertEqual(self.module.is_buffer_slot(test_slot), test_slot in Constants.BUFFER_SLOTS.value)

    def test_get_slot_value(self):

        for test_slot in self.test_slots:
            test_slot_split = test_slot.split(":")
            hour, minute = int(test_slot_split[0]), int(test_slot_split[1])
            assert_value = f"{hour if hour > 9 else f'0{hour}'}:{minute or '00'}"
            self.assertEqual(self.module.get_slot_value(hour, minute), assert_value)

    def test_create_calendar(self):

        self.assertDictEqual(self.module.create_calendar(), self.test_calender, "Calendar not created error")

    def test_get_time_range(self):

        self.assertEqual(self.module.get_time_range("10:00", "11:00"), ["10:00", "10:15", "10:30", "10:45"])
        self.assertEqual(self.module.get_time_range("12:00", "14:30"), ["12:00", "12:15", "12:30", "12:45",
                                                                        "13:00", "13:15", "13:30", "13:45",
                                                                        "14:00", "14:15"])
        self.assertEqual(self.module.get_time_range("09:15", "10:30"), ["09:15", "09:30", "09:45", "10:00",
                                                                        "10:15"])

    def test_init(self):
        self.assertEqual(self.module.create_calendar(), self.test_calender)
        self.assertEqual(self.module.capacity, 0)
        self.assertFalse(self.module.fully_booked)

    def test_is_vacant(self):
        test_start_time = choice(Constants.BUFFER_SLOTS.value)
        test_end_time = test_start_time
        while test_end_time in Constants.BUFFER_SLOTS.value:
            test_end_time = self.test_slots[self.test_slots.index(test_start_time) + 4]
            self.assertFalse(self.module.is_vacant(test_start_time, test_end_time))

        test_start_time = choice(self.non_buffer_slots[:-12])
        increment = 2
        while True:
            test_end_time = self.non_buffer_slots[self.non_buffer_slots.index(test_start_time) + increment]
            time_range = self.module.get_time_range(test_start_time, test_end_time)
            if increment > 10:
                test_start_time = choice(self.non_buffer_slots[:-12])
                increment = 1
            if all(slot not in Constants.BUFFER_SLOTS.value for slot in time_range):
                break
            increment += 1
        self.assertTrue(self.module.is_vacant(test_start_time, test_end_time),
                        f"{test_start_time}, {test_end_time} error on test_is_vacant")
        self.module.__init__()

    def test_book_room(self):

        test_start_time = choice(self.non_buffer_slots[:5])
        increment = 2
        test_end_time = ""
        while test_end_time not in self.non_buffer_slots:
            test_end_time = self.test_slots[self.test_slots.index(test_start_time) + increment]
            increment += 1

        self.module.book_room(test_start_time, test_end_time)
        self.assertFalse(self.module.is_vacant(test_start_time, test_end_time),
                         f"{test_start_time}, {test_end_time} error on test_book_room")
        self.module.__init__()
