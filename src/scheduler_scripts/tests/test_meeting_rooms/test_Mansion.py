import unittest


class TestMansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from meeting_rooms import Mansion
        cls.module = Mansion()

    def test_init(self):
        self.assertEqual(self.module.name, "G-Mansion")
        self.assertFalse(self.module.fully_booked)
        self.assertEqual(self.module.capacity, 20)

    def test_operator_overloading(self):
        self.assertFalse(3 >= self.module)
        self.assertTrue(1 < self.module)
        self.assertTrue(10 <= self.module)
        self.assertTrue(21 > self.module)
        self.assertFalse(6 >= self.module)
