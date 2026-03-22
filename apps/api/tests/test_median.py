import unittest

from app.utils.median import calculate_median


class CalculateMedianTests(unittest.TestCase):
    def test_calculate_median_for_odd_values(self) -> None:
        self.assertEqual(calculate_median([18000, 12000, 15000]), 15000)

    def test_calculate_median_for_even_values(self) -> None:
        self.assertEqual(calculate_median([8, 2, 4, 10]), 6)

    def test_calculate_median_rejects_empty_values(self) -> None:
        with self.assertRaises(ValueError):
            calculate_median([])

