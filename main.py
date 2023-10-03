import unittest

def multiplyNum(x,y):
    return x*y

class testCase(unittest.TestCase):
    def testMultiply(self):
        result = multiplyNum(9,9)
        self.assertEqual(result, 81)

    def testMultiplyFloat(self):
        result = multiplyNum(9.5, 9.5)
        self.assertAlmostEqual(result, 90.0, places=0)


if __name__ == '__main__':
    unittest.main()