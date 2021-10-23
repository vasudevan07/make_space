import unittest


class TestCave(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from meeting_rooms import Cave
        cls.module = Cave()

    def test_init(self):
        self.assertEqual(self.module.name, "C-Cave")
        self.assertFalse(self.module.fully_booked)
        self.assertEqual(self.module.capacity, 3)

    def test_operator_overloading(self):
        self.assertTrue(3 >= self.module)
        self.assertTrue(1 < self.module)
        self.assertTrue(2 <= self.module)
        self.assertTrue(5 > self.module)
        self.assertFalse(6 <= self.module)
