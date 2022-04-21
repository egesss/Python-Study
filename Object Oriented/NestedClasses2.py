class Car():
    class Engine():
        def __init__(self, name):
            self.carname = name
            self.cc = float(input("What is cc of engine (1.6/2.0): "))
        def engine_description(self):
            print(f"Capacity of the gasoline {self.carname} car is: {self.cc}")
    class Battery():
        def __init__(self, name):
            self.carname = name
            self.charge = int(input("What is capacity(70/85): "))
        def battery_description(self):
            print(f"Capacity of the electrical {self.carname} car is: {self.charge}")
    def __init__(self,name,model,source):
        self.name = name
        self.model = model
        self.year = 2020
        self.power = source
        self.engine = self.typeofCar(source)
    def description(self):
        print(f"Name: {self.name} " + f"Model: {self.model} " + f"Year: {self.year} ")
    def typeofCar(self,source):
        if source == 'e':
            return self.Battery(name = self.name)
        elif source == 'g':
            return self.Engine(name = self.name)

vw = Car('VW','POLO',input("What is source of car(e/g): "))
vw.description()
if vw.power == 'e':
    vw.engine.battery_description()
elif vw.power == 'g':
    vw.engine.engine_description()

car = Car('VW','POLO',input("What is source of car(e/g): "))
battery = car.Battery('VW')
battery.battery_description()  # LOOK AT THE DIFFERENCES BETWEEN THE ONE EXAMPLE WHICH BATTERY IS AN INNER CLASS
                                # AND THE OTHER ONE WHICH BATTERY IS ANOTHER CLASS OUTSIDE THE MAIN CLASS


