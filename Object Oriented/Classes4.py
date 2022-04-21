from ClassModule2 import ElectricCar  # WE IMPORT MODULE2 THAT IS IMPORTING MODULE1 SO THEY ARE CONNECTED SO THAT !!!!!!
                                      # WE CAN IMPORT SO THAT !!!!! import ElectricCar, Battery, Car !!!!! BUT WE DONT' NEED TO IMPORT !!!!!!
my_new_tesla = ElectricCar('tesla','roadster','2018',100)
print(my_new_tesla.get_descriptive_name())
my_new_tesla.battery.describe_battery()
my_new_tesla.battery.get_range()

# IF WE IGNORE ALL ABOVE BELOW ARGUMENTS ALSO WORKS SEPERATELY !!!!!

import ClassModule2 as Cars

my_new_tesla = Cars.ElectricCar('tesla','roadster','2018',100)
my_new_vw = Cars.Car('volkswagen','passat','2010')
print(my_new_tesla.get_descriptive_name())
print(my_new_vw.get_descriptive_name())
my_new_vw.read_odometer()
my_new_tesla.battery.describe_battery()
my_new_tesla.battery.get_range()

# IF I WANT TO IMPORT ALL INFO, CLASSES, FROM A MODULE

from ClassModule2 import *  # I CAN USE THIS !!!!!








