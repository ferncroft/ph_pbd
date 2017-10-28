import math

class Calculator(object):
    # Class does series of common calulator functions
    def checknos(self, x, y):
        # function that checks that input fields are numeric
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return True
        else:
            return False
 
    def add(self, x, y):
        # Calculation - add the two inputs together
        number_types = (int, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def subtract(self, x, y):
        # Calculation - subtract the second number from the first
        number_types = (int, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError

    def multiply(self, x, y):
        # Calculation - multiply inputs together
        if self.checknos(x,y):
            return x * y
        else:
            raise ValueError

    def divide(self, x, y):
        # Calculation - divide the second number into the first
        if self.checknos(x,y):
            if y == 0:
                return 'NaN'
            else:
                return x / y
        else:
            raise ValueError

    def exponent(self, x, y):
        # Calculation - the exponential of the 1st number to the power of the second
        if self.checknos(x,y):
            return x**y
        else:
            raise ValueError

    def sqroot(self, x):
        # Calculation - the square root of the input number
        if self.checknos(x,1):
            return math.sqrt(x)
        else:
            raise ValueError

    def factor(self, x):
        # Calculation - the factorial of the input number 
        try:
            return math.factorial(x)
        except:
            raise ValueError('Value must be a positive integer')

    def log(self, x):
        # Calculation - return the Log e value of the input
        try:
            return math.log(x)
        except:
            raise ValueError

    def log10(self, x):
        # Calculation - return the Log10 value of the input
        try:
            return math.log10(x)
        except:
            raise ValueError

    def circleperimeter(self, x):
        # Calculation - return the perimeter of a circle with the input radius
        if self.checknos(x,1):
            return 2 * math.pi * x
        else:
            raise ValueError

    def sin(self, x):
        # Calculation - return the sine of the input number
        try:
            return math.sin(x)
        except:
            raise ValueError


