import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertAlmostEqual(actual, expected, "Expected different output when calling 'calculate()' with '[0,1,2,3,4,5,6,7,8]'")

    def test_calculate2(self):
        actual = calculate([9, 8, 7, 6, 5, 4, 3, 2, 1])
        expected = {
            'mean': [[6.0, 5.0, 4.0], [8.0, 5.0, 2.0], 5.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[9, 8, 7], [9, 6, 3], 9],
            'min': [[3, 2, 1], [7, 4, 1], 1],
            'sum': [[18, 15, 12], [24, 15, 6], 45]
        }
        self.assertAlmostEqual(actual, expected, "Expected different output when calling 'calculate()' with '[9,8,7,6,5,4,3,2,1]'")
        
    def test_calculate_with_few_digits(self):
        with self.assertRaises(ValueError):
            calculate([2, 6, 2, 8, 4, 0, 1])

if __name__ == "__main__":
    unittest.main()
