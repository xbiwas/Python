# Encapsulation

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    # Encapsulation is done here
    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"


# my_car = Car("TATA", "Safari")
# print(my_car.full_name())
# print(my_car.get_brand())
class ElectricCar(Car):
    def __init__(self, __brand, model, batterySize):
        super().__init__(__brand, model)
        self.batterySize = batterySize

my_electric_car = ElectricCar("TSLA", "Model S", "85KWH")
print(my_electric_car.full_name())
# print(my_electric_car.__brand)
print(my_electric_car.get_brand())
