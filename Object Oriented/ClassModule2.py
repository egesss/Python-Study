from ClassModule import Car # WE'VE IMPORTED CAR CLASS

class Battery():
    def __init__(self,battery_size):  # IT IS DEFUALT WE'LL MAKE IT USER CONTROLLED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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

# IT IS A MODULE CAR INVOLVED BY USING IMPORT TO CAR !!!!!