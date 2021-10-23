import unittest

from meeting_rooms import Cave, Tower, Mansion
from config import Messages

class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import scheduler
        cls.module = scheduler

    def setUp(self):
        pass

    def test_main(self):
        rooms = dict(cave=Cave(), tower=Tower(), mansion=Mansion())
        self.assertEqual(self.module.main(rooms, "BOOK 09:30 13:15 2"), "C-Cave")
        self.assertEqual(self.module.main(rooms, "BOOK 13:45 18:45 2"), "C-Cave")
        self.assertEqual(self.module.main(rooms, "BOOK 12:55 14:00 3"), Messages.INCORRECT_INPUT.value)
        self.assertEqual(self.module.main(rooms, "BOOK 13:45 17:15 6"), "D-Tower")
        self.assertEqual(self.module.main(rooms, "VACANCY 13:45 15:00"), "G-Mansion")
        self.assertEqual(self.module.main(rooms, "BOOK 14:00 15:00 2"), "G-Mansion")
        self.assertEqual(self.module.main(rooms, "BOOK 17:00 18:30 12"), "G-Mansion")
        self.assertEqual(self.module.main(rooms, "VACANCY 17:00 18:00"), Messages.NO_VACANT_ROOM.value)
        self.assertEqual(self.module.main(rooms, "VACANCY 17:30 18:00"), "D-Tower")
        self.assertEqual(self.module.main(rooms, "BOOK 17:00 18:30 12"), Messages.NO_VACANT_ROOM.value)
        self.assertEqual(self.module.main(rooms, "BOOK 15:35 16:35 12"), Messages.INCORRECT_INPUT.value)

        rooms = dict(cave=Cave(), tower=Tower(), mansion=Mansion())

        self.assertEqual(self.module.main(rooms, "VACANCY 10:00 12:00"), "C-Cave D-Tower G-Mansion")
        self.assertEqual(self.module.main(rooms, "BOOK 11:00 11:45 2"), "C-Cave")
        self.assertEqual(self.module.main(rooms, "BOOK 11:30 13:00 35"), Messages.NO_VACANT_ROOM.value)
        self.assertEqual(self.module.main(rooms, "BOOK 11:30 13:00 15"), "G-Mansion")
        self.assertEqual(self.module.main(rooms, "VACANCY 11:30 12:00"), "D-Tower")
        self.assertEqual(self.module.main(rooms, "BOOK 14:00 15:30 3"), "C-Cave")
        self.assertEqual(self.module.main(rooms, "BOOK 15:00 16:30 2"), "D-Tower")
        self.assertEqual(self.module.main(rooms, "BOOK 15:15 12:15 12"), Messages.INCORRECT_INPUT.value)
        self.assertEqual(self.module.main(rooms, "VACANCY 15:30 16:00"), "C-Cave G-Mansion")
        self.assertEqual(self.module.main(rooms, "BOOK 15:30 16:30 2"), "C-Cave")
        self.assertEqual(self.module.main(rooms, "VACANCY 15:45 16:00"), "G-Mansion")
        self.assertEqual(self.module.main(rooms, "BOOK 16:00 17:00 5"), "G-Mansion")
        self.assertEqual(self.module.main(rooms, "VACANCY 18:00 19:00"), Messages.NO_VACANT_ROOM.value)
        #self.assertEqual(self.module.main(rooms, "BOOK 18:00 19:00"), Messages.INCORRECT_INPUT.value)
