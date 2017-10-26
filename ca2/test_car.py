import unittest

from car import Car, ElectricCar, RentalCar

# test the car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())

    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())

# test the rental car functionality
class TestRentalCar(unittest.TestCase):
    def setUp(self):
        self.car = RentalCar()
    
    def test_carhire(self):
        self.assertEqual(False, self.car.getOutOnHire())
        self.car.setOutOnHire(True)
        self.assertEqual(True, self.car.getOutOnHire())

# test the electric car functionality
class TestElectricCar(unittest.TestCase):

    def setUp(self):
        self.car = ElectricCar()

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        
    def test_car_number_of_fuel_cells(self):
        self.assertEqual(1, self.car.getNumberFuelCells())
        self.car.setNumberFuelCells(15)
        self.assertEqual(15, self.car.getNumberFuelCells())

if __name__ == '__main__':
    unittest.main()
