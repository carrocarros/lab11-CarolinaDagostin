# https://github.com/carrocarros/lab11-CarolinaDagostin
# Carolina Dagostin
# No partner since there was an odd number in the class

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    #2
    def test_add(self):
        self.assertEqual(add(1,2 ), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(2,1 ), 1)
        self.assertEqual(sub(-1, -2), 1)
        self.assertEqual(sub(-10, 9), -1)

    #1
    def test_multiply(self):
        self.assertEqual(mul(1,2 ), 2)
        self.assertEqual(mul(-1, -2), 2)
        self.assertEqual(mul(-1, 2), -2)

    def test_divide(self):
        self.assertEqual(div(2, 4), 2.0)
        self.assertEqual(div(5, -10), -2.0)
        self.assertEqual(div(2, 1), 0.5)


    #2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertEqual(log(1,2), 0.0)
        self.assertEqual(log(8, 2), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(10, 1)

    #1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(-5, 10)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-4)


if __name__ == "__main__":
    unittest.main()