import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.sub(5, 2), 3)
        self.assertEqual(calculator.sub(2, 5), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.log(2, 8), 3)
        self.assertAlmostEqual(calculator.log(10, 100), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(-1, 10)
        with self.assertRaises(ValueError):
            calculator.log(2, -10)
        with self.assertRaises(ValueError):
            calculator.log(0, 100)


if __name__ == "__main__":
    unittest.main()
