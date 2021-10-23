import unittest


class TestTower(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from meeting_rooms import Tower
        cls.module = Tower()

    def test_init(self):
        self.assertEqual(self.module.name, "D-Tower")
        self.assertFalse(self.module.fully_booked)
        self.assertEqual(self.module.capacity, 7)

    def test_operator_overloading(self):
        self.assertFalse(3 >= self.module)
        self.assertTrue(1 < self.module)
        self.assertTrue(6 <= self.module)
        self.assertTrue(21 > self.module)
        self.assertFalse(5 >= self.module)
