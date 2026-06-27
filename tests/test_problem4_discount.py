import unittest

from solutions.problem4_discount import get_discount


class GetDiscountTest(unittest.TestCase):
    def test_applies_discount_percentage(self):
        self.assertEqual(get_discount(1000, 10), 900)

    def test_zero_discount_returns_original_price(self):
        self.assertEqual(get_discount(1000, 0), 1000)

    def test_full_discount_returns_zero(self):
        self.assertEqual(get_discount(1000, 100), 0)

    def test_rejects_negative_discount_percent(self):
        with self.assertRaises(ValueError):
            get_discount(1000, -1)

    def test_rejects_discount_percent_above_100(self):
        with self.assertRaises(ValueError):
            get_discount(1000, 101)

    def test_rejects_negative_price(self):
        with self.assertRaises(ValueError):
            get_discount(-100, 10)

    def test_rejects_non_numeric_values(self):
        with self.assertRaises(TypeError):
            get_discount("1000", 10)

    def test_rejects_boolean_values(self):
        with self.assertRaises(TypeError):
            get_discount(True, 10)


if __name__ == "__main__":
    unittest.main()
