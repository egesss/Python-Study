class Car():
    def __init__(self,name,model,source):
        self.name = name
        self.model = model
        self.year = 2020
        self.powersource = source
    def description(self):
        print(f"Name: {self.name} " + f"Model: {self.model} " + f"Year: {self.year} ")
    class Engine():
        def __init__(self,capacity,name):
            self.carname = name
            self.cc = capacity
        def engine_description(self):
            print(f"Capacity of the gasoline {self.carname} car is: {self.cc}")
    class Battery():
        def __init__(self,capacity,name):
            self.carname = name
            self.charge = capacity
        def battery_description(self):
            print(f"Capacity of the electrical {self.carname} car is: {self.charge}")
    def carType(self):
        if self.powersource == 'e':
            self.battery = self.Battery(int(input("What is capacity(70/85): ")),name = self.name)
        elif self.powersource == 'g':
            self.engine = self.Engine(float(input("What is cc of engine (1.6/2.0): ")),name = self.name)

vw = Car('VW','POLO',input("What is source of car(e/g): "))
vw.description()
vw.carType()
if vw.powersource == 'e':
    vw.battery.battery_description()
elif vw.powersource == 'g':
    vw.engine.engine_description()
