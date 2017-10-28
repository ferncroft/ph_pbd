import unittest
from calculator import Calculator

# test the calculator functionality
class TestCalculator(unittest.TestCase):

    def setUp(self):
    #inititaion
        self.calc = Calculator()

    def test_calculator_add(self):
        # test add function - covers 0, integer, negatives, alphabetics and fractions
        result = self.calc.add(2, 4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -4)
        self.assertEqual(-2, result)
        result = self.calc.add(-2, 2)
        self.assertEqual(0, result)
        result = self.calc.add(2.5, 1.25)
        self.assertEqual(3.75, result)
        try:
            Calculator().add('2','5')
            self.fail('should throw error')
        except: ValueError
        pass
         

    def test_calculator_subtract(self):
        # test add function - covers 0, integer, negatives and fractions
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)
        result = self.calc.subtract(2, -0.5)
        self.assertEqual(2.5, result)
        
    def test_calculator_multiply(self):
        # test add function - covers 0, integer, negatives and fractions
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
        result = self.calc.multiply(5, 2.5)
        self.assertEqual(12.5, result)

    def test_calculator_divide(self):
        # test divide function - covers 0, integer, negatives and fractions
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
        result = self.calc.divide(0.5, 2)
        self.assertEqual(0.25, result)
        result = self.calc.divide(2, 0.5)
        self.assertEqual(4, result)

    def test_calculator_exponent(self):
        # test exponential function - covers 0, integer, negatives and fractions
        result = self.calc.exponent(2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(2,3)
        self.assertEqual(8, result)
        result = self.calc.exponent(-2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(2, 0)
        self.assertEqual(1, result)
        result = self.calc.exponent(2, 0.5)
        self.assertEqual(1.4142135623730951, result)
        result = self.calc.exponent(0.5, 2)
        self.assertEqual(0.25, result)
        result = self.calc.exponent(0.5, 1.5)
        self.assertEqual(0.3535533905932738, result)
        result = self.calc.exponent(4, -2)
        self.assertEqual(0.0625, result)

    def test_calculator_sqroot(self):
        # test sqroot function - covers 0, integer, negatives and fractions
        result = self.calc.sqroot(4)
        self.assertEqual(2, result)
        result = self.calc.sqroot(0)
        self.assertEqual(0, result)
        result = self.calc.sqroot(0.5)
        self.assertEqual(0.7071067811865476, result)
        result = self.calc.sqroot(1)
        self.assertEqual(1, result)
        try:
            Calculator().sqroot(-4)
            self.fail('should throw error')
        except: ValueError
        pass
   
    def test_calculator_factor(self):
        # test add function - covers 0, integer, negatives and fractions
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
        # test add function - covers 0, integer, negatives and fractions
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
        # test add function - covers 0, integer, negatives and fractions
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
        # test add function - covers 0, integer, negatives fractions
        result = self.calc.circleperimeter(2)
        self.assertEqual(12.566370614359172, result)
        result = self.calc.circleperimeter(0)
        self.assertEqual(0, result)
        result = self.calc.circleperimeter(1.5)
        self.assertEqual(9.42477796076938, result)
        try:
            Calculator().circleperimeter(-2)
            self.fail('should throw error')
        except: ValueError
        pass

    def test_calculator_sin(self):
        # test add function - covers 0, integer, negatives and fractions
        result = self.calc.sin(2)
        self.assertEqual(0.9092974268256817, result)
        result = self.calc.sin(0)
        self.assertEqual(0, result)
        result = self.calc.sin(-4)
        self.assertEqual(0.7568024953079282, result)
        result = self.calc.sin(3.55)
        self.assertEqual(-0.3971481672859598, result)



if __name__ == '__main__':
    unittest.main()