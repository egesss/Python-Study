from ClassModule import Car

class Battery():
    def __init__(self,battery_size = 70):  # IT IS DEFAULT WE'LL MAKE IT USER CONTROLLED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " +  str(self.battery_size) + " -kWh battery.")
    def get_range(self):  # WE SPECIFIED MORE ON BATTERY
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

# NOW WE'LL CHANGE THE ELECTRICCAR CLASS AND SHORTEN THE BATTERY ATTRIBUTES
# TO SEE DIFFERENCE COMPARE CLASSESINHERITANCE AND CLASSES3 !!!!!!!!!!!!!

battery1 = Battery()

print(f"Battery is {battery1.describe_battery()}")

my_tesla = ElectricCar('tesla','model r','2019')
my_tesla.fill_gas_tank()
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()  # WE FIRST TAKE OUTER VALUE AND GOES TO INNER VALUE !!!!!
my_tesla.battery.get_range()

# FOR INPUT !!!!!

class Battery():
    def __init__(self,battery_size):  # IT IS USER CONTROLLED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " +  str(self.battery_size) + " -kWh battery.")
    def get_range(self): # WE SPECIFIED MORE ON BATTERY
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = int((self.battery_size * 3) + self.battery_size/2)  # WE NEED TO WRITE self.variable to other functions inside a class !!!!!
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

class ElectricCar(Car):
    def __init__(self,make,model,year,battery_size):
        super().__init__(make,model,year)
        self.battery = Battery(battery_size)
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_new_tesla = ElectricCar('tesla','roadster','2019',int(input("What is the battery model(70/85): ")))
print(my_new_tesla.get_descriptive_name())
my_new_tesla.battery.describe_battery()
my_new_tesla.battery.get_range()


