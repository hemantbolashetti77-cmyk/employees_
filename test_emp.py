import unittest
from employee import calculate_bonus

class TestEmployeeBonus(unittest.TestCase):

    def test_bonus_26_days(self):
        self.assertEqual(calculate_bonus(26), 5000)

    def test_bonus_20_days(self):
        self.assertEqual(calculate_bonus(20), 3000)

    def test_bonus_15_days(self):
        self.assertEqual(calculate_bonus(15), 1500)

    def test_bonus_less_than_15(self):
        self.assertEqual(calculate_bonus(10), 0)

    def test_bonus_edge_case(self):
        self.assertEqual(calculate_bonus(0), 0)

if __name__ == "__main__":
    unittest.main()
