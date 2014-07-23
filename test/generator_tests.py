
import unittest

from src.generator import TimeSlotGenerator

class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.three_hours = TimeSlotGenerator(3)
        self.four_hours = TimeSlotGenerator(4)
        self.five_hours = TimeSlotGenerator(5)

    def tearDown(self):
        self.three_hours = None
        self.four_hours = None
        self.five_hours = None

    # make sure that all the times are
    # multiples of 15
    def test_divisibility(self):

        for slot in self.three_hours.time_slots:
            self.assertTrue(slot % 15 == 0)

        for slot in self.four_hours.time_slots:
            self.assertTrue(slot % 15 == 0)

        for slot in self.five_hours.time_slots:
            self.assertTrue(slot % 15 == 0)

    # make sure that the times add up
    # to the number of hours
    def test_schedule_filled(self):

        three_hour_total = 0
        four_hour_total = 0
        five_hour_total = 0

        # 3 hours
        for slot in self.three_hours.time_slots:
            three_hour_total = three_hour_total + slot

        self.assertEqual(three_hour_total/60, 3)

        # 4 hours
        for slot in self.four_hours.time_slots:
            four_hour_total = four_hour_total + slot

        self.assertEqual(four_hour_total/60, 4)

        # 5 hours
        for slot in self.five_hours.time_slots:
            five_hour_total = five_hour_total + slot

        self.assertEqual(five_hour_total/60, 5)

if __name__ == '__main__':
    unittest.main()
