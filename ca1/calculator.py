import math

class Calculator(object):
    
    def checknos(self, x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return True
        else:
            return False
 
    def add(self, x, y):
        number_types = (int, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def subtract(self, x, y):
        number_types = (int, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError

    def multiply(self, x, y):
        if self.checknos(x,y):
            return x * y
        else:
            raise ValueError

    def divide(self, x, y):
        if self.checknos(x,y):
            if y == 0:
                return 'NaN'
            else:
                return x / y
        else:
            raise ValueError

    def exponent(self, x, y):
        if self.checknos(x,y):
            return x**y
        else:
            raise ValueError

    def sqroot(self, x):
        if self.checknos(x,1):
            return math.sqrt(x)
        else:
            raise ValueError

    def factor(self, x):
        try:
            return math.factorial(x)
        except:
            raise ValueError

    def log(self, x):
        try:
            return math.log(x)
        except:
            raise ValueError

    def log10(self, x):
        try:
            return math.log10(x)
        except:
            raise ValueError

    def circleperimeter(self, x):
        if self.checknos(x,1):
            return 2 * math.pi * x
        else:
            raise ValueError


