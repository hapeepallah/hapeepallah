import unittest

# This is the class we want to test. So, we need to import it
import Calculator as CalculatorClass

class Test(unittest.TestCase):
    calculator = CalculatorClass.Calculator() # instantiate the Calculator Class
    def test_0_add(self):
        result = self.calculator.add(4,8)
        self.assertEqual(result,12)

    def test_1_subtract(self):
        result = self.calculator.subtract(12,7)
        self.assertEqual(result,5)

    def test_2_multiply(self):
        result = self.calculator.multiply(3,5)
        self.assertEqual(result,15)

    def test_0_divi(self):
        result = self.calculator.divide(15,3)
        self.assertEqual(result,5)
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()