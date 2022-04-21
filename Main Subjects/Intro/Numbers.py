print("Hens", 25 + 30/6)

print("Mod", 5 % 2)

print(5 + 2 < 3 - 5)
print(5 + 15 > -15 - 20)

print(0.1 + 0.10)

print("What is your age:")
age = int(input())
message = "Hello " + str(age) + "rd Birthday" # "Hello" + age + "rd Birthday gives error message
print(message)
print(f"Hello {age}rd Birthday")

cars = 100
space = 4.0
drivers = 30
passengers = 90
print("Available cars", cars - drivers)
print("Available cars", cars - drivers,"Have Nice Ride !!!")

my_name = 'Ege Selvi'
my_age = 22
my_height = 1.90
my_weight = 90
my_eyes = 'Blue'

print(f"Lets Talk about {my_name}") # f allow the write variable by its own name
print(f"My eyes are {my_eyes}")
total = my_age + my_height + my_weight
print(f"The total of my age, weight,and height is {total}")

print("My height is almost", round(my_height))