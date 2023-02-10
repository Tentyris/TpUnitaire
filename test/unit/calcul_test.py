import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        
    def test_add(self):
        result = self.calculator.add(1, 2)
        self.assertEqual(result, 3)
        
    def test_subtract(self):
        result = self.calculator.subtract(4, 2)
        self.assertEqual(result, 2)
        
    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)
        
    def test_divide(self):
        result = self.calculator.divide(4, 2)
        self.assertEqual(result, 2)
        
    def test_power(self):
        result = self.calculator.power(2, 3)
        self.assertEqual(result, 8)
        
    def test_square_root(self):
        result = self.calculator.square_root(9)
        self.assertEqual(result, 3)
        
if __name__ == '__main__':
    unittest.main()