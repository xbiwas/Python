# Class Variables
class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

Car("TATA", "Safari")
Car("Tesla", "Model S")
print(Car.total_car)