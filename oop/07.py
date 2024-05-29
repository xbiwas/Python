# Static Method

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod #no need to write self
    def general_desc():
        return "Cars are four wheeler and are amazing."


myCar = Car("TATA", "Safari")
print(Car.general_desc())
