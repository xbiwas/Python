class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

mero_car = Car("Tata", "safari")
print(mero_car.full_name())

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

mero_naya_car = ElectricCar("Tesla", "Model S", "85kwh")
print(mero_naya_car.full_name())

