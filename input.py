# base class
class vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def info(self):
        print(self.name, self.color, self.price)

# Child Class
class car(vehicle):

    def change_gear(self, no):
        print(self.name, 'change gear to number', no)

# Create object of car
car_obj = car('BMW X1', 'Black', 35000)
car_obj.info()
car_obj.change_gear(5)
