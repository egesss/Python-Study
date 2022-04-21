# CREATING A CLASS

class Dog():

    def __init__(self,name,age): # SPECIAL FUNCTIONS FOR CLASS !!!!! # It must comes before all other parameters
        self.name = name       # We pass name and age so that !!!!!
        self.age = age        # There is no return but it returns an instance representing dog
    def sit(self):
        print(self.name.title() + " is now sitting")
    def roll_over(self):
        print(self.name.title() + " is rolled over!")

my_dog = Dog('jo',6) # Python reads Jo and 6 and using __init__ takes parameters to initialize Dog !!!!!
print("My dog's name is " + my_dog.name.title() + ".")  # We can use parameter by using dot notation !!!!!!!!
print("My dog is " + str(my_dog.age) + " years old")

# Dot notation is used for accessing attributes when we declared a dict so that:
# dict {'key_1': value_1,...) we access its keys and values by dot notation so that !!!!! dict.items(),dict.keys(),dict.values() !!!!!

my_dog.sit()  # We make dog sit
my_dog.roll_over()  # We make dog rolled over !!!!!

your_dog = Dog('lucy',3) # We've created another dog !!!!!
print("Your dog name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old")
your_dog.sit()

class Warrior():
    def __init__(self,type,hitpoint,damage):
        self.type = type
        self.hitpoint = hitpoint
        self.damage = damage
    def attack(self):
        print(f"{self.type.title()} fighting now")
    def defense(self):
        print(f"{self.type.title()} defending now")

Swordsman1 = Warrior('swordsman',50,100)
print("Your soldier type is " + Swordsman1.type.title() + ".")
Swordsman1.attack()
print("Your swordsman hitpoint decreased to " + str(Swordsman1.hitpoint-15))
print("He cause " + str(Swordsman1.damage) + " damage.")
Swordsman1.defense()





