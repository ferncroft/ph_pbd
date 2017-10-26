import unittest
from calculator import Calculator

# test the calculator functionality
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_add(self):
        result = self.calc.add(2, 4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -4)
        self.assertEqual(-2, result)
        result = self.calc.add(-2, 2)
        self.assertEqual(0, result)
        try:
            Calculator().add('2','5')
            self.fail('should throw error')
        except: ValueError
        pass
         

    def test_calculator_subtract(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)
        
    def test_calculator_multiply(self):
        result = self.calc.multiply(2, 2)
        self.assertEqual(4, result)
        result = self.calc.multiply(-2,4)
        self.assertEqual(-8, result)
        result = self.calc.multiply(-2, -4)
        self.assertEqual(8, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)
        result = self.calc.multiply(2, 0.2)
        self.assertEqual(0.4, result)

    def test_calculator_divide(self):
        result = self.calc.divide(2, 2)
        self.assertEqual(1, result)
        result = self.calc.divide(-2, 4)
        self.assertEqual(-0.5, result)
        result = self.calc.divide(-2, -4)
        self.assertEqual(0.5, result)
        result = self.calc.divide(0, 2)
        self.assertEqual(0, result)
        result = self.calc.divide(2, 0)
        self.assertEqual('NaN', result)
        result = self.calc.divide(2, 0.2)
        self.assertEqual(10, result)
        result = self.calc.divide(5, 2)
        self.assertEqual(2.5, result)

    def test_calculator_exponent(self):
        result = self.calc.exponent(2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(2,3)
        self.assertEqual(8, result)
        result = self.calc.exponent(-2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(2, 0)
        self.assertEqual(1, result)
        result = self.calc.exponent(4, -2)
        self.assertEqual(0.0625, result)

    def test_calculator_sqroot(self):
        result = self.calc.sqroot(4)
        self.assertEqual(2, result)
        result = self.calc.sqroot(1)
        self.assertEqual(1, result)
        try:
            Calculator().sqroot(-4)
            self.fail('should throw error')
        except: ValueError
        pass
   
    def test_calculator_factor(self):
        result = self.calc.factor(3)
        self.assertEqual(6, result)
        try:
            Calculator().factor(-3)
            self.fail('should throw error')
        except: ValueError
        pass
        result = self.calc.factor(0)
        self.assertEqual(1, result)
        try:
            Calculator().factor(2.5)
            self.fail('should throw error')
        except: ValueError
        pass
    
    def test_calculator_log(self):
        result = self.calc.log(2)
        self.assertEqual(0.6931471805599453, result)
        try:
            Calculator().log(-2)
            self.fail('should throw error')
        except: ValueError
        pass
        try:
            Calculator().log(0)
            self.fail('should throw error')
        except: ValueError
        pass
        result = self.calc.log(0.5)
        self.assertEqual(-0.6931471805599453, result)

    def test_calculator_log10(self):
        result = self.calc.log10(2)
        self.assertEqual(0.3010299956639812, result)
        try:
            Calculator().log10(-2)
            self.fail('should throw error')
        except: ValueError
        pass
        try:
            Calculator().log10(0)
            self.fail('should throw error')
        except: ValueError
        pass
        result = self.calc.log10(0.5)
        self.assertEqual(-0.3010299956639812, result)



    def test_calculator_cirleperimeter(self):
        result = self.calc.circleperimeter(2)
        self.assertEqual(12.566370614359172, result)
        result = self.calc.circleperimeter(0)
        self.assertEqual(0, result)
        try:
            Calculator().circleperimeter(-2)
            self.fail('should throw error')
        except: ValueError
        pass


if __name__ == '__main__':
    unittest.main()