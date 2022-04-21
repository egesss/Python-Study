# INHERITANCE
# IT COMES BEFORE CLASSES 3 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# IT TAKES ONE OLD CLASS AND ALL ITS ATTRIBUTES

from ClassModule import Car  # WE'VE IMPORTED CAR CLASS

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)  # Super function helps Python to take old initials of Car !!!!!!!!!!!!!!!!!!!
        self.battery_size = 70              # Super comes from SUPERCLASS that is Car() and ElectricCar is CHILDCLASS !!!!! We have now new attribute here !!!!!!
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -kWh battery.")
    def fill_gas_tank(self):                # Override the old value again !!!!!
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# OVERRIDING METHODS

# WE CAN OVERRIDE ANY METHOD DOESN'T FIT FOR OUR CHILD CLASS GAS-ELECTRIC DIFFERENCE !!!!!

my_tesla.fill_gas_tank()










