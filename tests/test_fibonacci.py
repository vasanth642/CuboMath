import unittest
from src.Inventory.fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_small_values(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_large_values(self):
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(50), 12586269025)
        self.assertEqual(fibonacci(70), 190392490709135)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            fibonacci(5.5)
        with self.assertRaises(TypeError):
            fibonacci("10")


if __name__ == "__main__":
    unittest.main()