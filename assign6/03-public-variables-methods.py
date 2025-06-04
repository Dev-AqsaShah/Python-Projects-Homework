# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        return f'{self.brand} is starting.'
    
car:Car = Car("Toyota")
print(car.brand)
print(car.start())