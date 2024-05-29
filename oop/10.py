# Multiple Inheritance

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class EvCar(Car):
    def __init__(self, brand, model, battery):
        self.battery = battery
        super().__init__(brand, model)
    
myEv = EvCar("TSLA", "Model S", "45KWH")
# print(isinstance(myEv, Car))
# print(isinstance(myEv, EvCar))


class Battery:
    def battery_info(self):
        return "It has battery"


class Engine:
    def engine_info(self):
        return "It has enginee"

class EvTwo(Car, Battery, Engine):
    pass

myNewEv = EvTwo("TSLA", "Model S")
print(myNewEv.engine_info())
print(myNewEv.battery_info())