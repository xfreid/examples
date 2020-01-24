# Unit Testing Your Code with the unittest Module
# https://www.youtube.com/watch?v=6tNS--WetLI

# to run the unitest
#   cd example1
#   python -m unittest test_calc.py
# see the bottom for alternative

import unittest
# import the module to test
import calc

# inherit testcase.TestCase
class TestCalc(unittest.TestCase):

    # https://docs.python.org/3/library/unittest.html
    # https://docs.python.org/3/library/unittest.html#classes-and-functions
    # each test method MUST start with "test_"
    # if you rename the following method to "add_test", it will be skipped
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # we don't want to call the divide function directly like above
        # bcause it will throw the exception, and unittest would
        # think it fails
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # alternatively, we can use context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)



# if you want to run the unittest directly with test_calc.py
# e.g. click "Run Code" button in VS Code
# add the following section
if __name__ == '__main__':
    unittest.main() 