# Property Decorator
class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    def full_name(self):
        return f"{self.brand} {self.__model}"
    
    @property
    def model(self):
        return self.__model
    

    


my_car = Car("TATA", "Safari")
# my_car.model = "Nexon"

print(my_car.model)
