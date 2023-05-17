import unittest
from main import sum, divide

class CalcTest(unittest.TestCase):

    def test_sum(self):
        a = 4
        b = 2
        expected_result = 6
        actual_result = sum(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_divide(self):
        a = 4
        b = 2
        expected_result = 2
        actual_result = divide(a, b)
        self.assertEqual(expected_result, actual_result)






if __name__ == '__main__':
    unittest.main()