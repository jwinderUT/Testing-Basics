import unittest
from challenge import facto


if __name__ == '__main__':
    unittest.main()


class TestFactorial(unittest.TestCase):
    
    def testOne(self):
        self.assertEqual(facto(1), 1)

    def testTwo(self):
        self.assertEqual(facto(2), 2)

    def testZero(self):
        self.assertEqual(facto(0), 1)

    def TestNegative(self):
        self.assertEqual(facto(-4), "Cannot factorialize negative numbers.")

    def TestDataType(self):
        self.assertEqual(facto("bad data"), "Bad data type, please enter a whole number.")
    


