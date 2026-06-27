import unittest

from solutions.problem6_add import add


class AddTest(unittest.TestCase):
    def test_adds_two_positive_numbers(self):
        self.assertEqual(add(5, 2), 7)

    def test_adds_negative_numbers(self):
        self.assertEqual(add(-5, -2), -7)

    def test_adds_mixed_sign_numbers(self):
        self.assertEqual(add(-5, 2), -3)

    def test_adds_zero(self):
        self.assertEqual(add(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
