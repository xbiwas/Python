# Plymorphism
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

myCar = Car("TATA", "Safari")
# print(myCar.get_brand())
# print(myCar.full_name())

class ElectricCar(Car):
    def __init__(self, __brand, model, batterySize):
        self.batterySize = batterySize
        super().__init__(__brand, model)
    
    def fuel_type(self):
        return "Electric Charge"

myElectricCar = ElectricCar("TSLA", "Model S", "85KWH")
# print(myElectricCar.get_brand())
# print(myElectricCar.full_name())

print(myCar.fuel_type())
print(myElectricCar.fuel_type())