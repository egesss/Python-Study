# WORKING WITH CLASSES

class Car():

    def __init__(self,make,model,year): # Every attribute needs and initial value even if it is empty string or 0 !!!!!
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
    def increment_odometer(self,miles): # We define a function to increment odometer
        self.odometer_reading += miles
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer() # We can not give odometer but it is defined inside the class difference is this !!!!!
print(f"My car maker is {my_new_car.make.title()}")
# MODIFYING ATTRIBUTE VALUES !!!!!

# DIRECTLY MODIFYING

my_new_car.odometer_reading = 23 # DIRECTLY CHANGE !!!!!
print("Directly changed: ", end=' ')
my_new_car.read_odometer()

# THROUGH A METHOD

my_new_car.update_odometer(23)
print("Through a defined function in class: ", end=' ')
my_new_car.read_odometer()
print("Now we'll get an error when we put a value smaller than old: ",end=' ')
my_new_car.update_odometer(22)

# INCREMENTING AN ATTRIBUTE'S VALUE THROUGH A METHOD

my_new_car.increment_odometer(25)
print("I used my car 25 miles and now its odometer is: ", end = ' ')
my_new_car.read_odometer()
my_new_car.update_odometer(25)








