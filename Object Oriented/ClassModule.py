class Car():

    def __init__(self,make,model,year):  # Every attribute needs and initial value even if it is empty string or 0 !!!!!
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # It does not come from a value, It creates itself in time and this attribute is specified with Car() !!!!!
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):  # We define a function to update odometer !!!!!
                                        #self.odometer_reading = mileage just defined at the beginning we made a modification !!!!!
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):  # We define a function to increment odometer
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print("Our fuel tank is full now!")