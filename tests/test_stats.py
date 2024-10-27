import unittest
from src.stats import mean, median


class TestStats(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(mean([1.0, 2.0, 3.0, 4.0, 5.0]), 3.0)
        self.assertIsNone(mean([]))
        self.assertEqual(mean([7.0]), 7.0)
        self.assertEqual(mean([-1.0, -2.0, -3.0, -4.0, -5.0]), -3.0)

    def test_median(self):
        self.assertEqual(median([1.0, 2.0, 3.0]), 2.0)
        self.assertEqual(median([1.0, 2.0, 3.0, 4.0]), 2.5)
        self.assertIsNone(median([]))
        self.assertEqual(median([7.0]), 7.0)


if __name__ == "__main__":
    unittest.main()
