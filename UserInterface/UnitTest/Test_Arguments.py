import unittest

import Arguments


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Arguments.add(3, 4), 7)
        self.assertEqual(Arguments.add(4, 5, 7), 16)
        self.assertEqual(Arguments.add(-1, 3, -2, 5), 5)

    def test_calculator(self):
        self.assertEqual(Arguments.calculate(0, add=4, subtract=2), 2)
        self.assertEqual(Arguments.calculate(0, add=3, multiply=4, divide=2), 6)


if __name__ == '__main__':
    unittest.main()
