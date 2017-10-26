# Define a class for my car

class Car(object):
    # implement the car object.
    
    def __init__(self, colour='', make='', mileage=0):
        self.__colour = colour
        self.__make = make
        self.__mileage = mileage
        self.engineSize = ''
        self.regno = ''

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage

    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage

class RentalCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.__outOnHire = False
        self.renter_name = ""
        
    def setOutOnHire(self, value):
        self.__outOnHire = value
        
    def getOutOnHire(self):
        return self.__outOnHire
    
class ElectricCar(RentalCar):
    
    def __init__(self):
        RentalCar.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

class PetrolCar(RentalCar):

    def __init__(self):
        RentalCar.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

class DieselCar(RentalCar):

    def __init__(self):
        RentalCar.__init__(self)

class HybridCar(RentalCar):

    def __init__(self):
        RentalCar.__init__(self)