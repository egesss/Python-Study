print("How old are you: ", end = '')
age = input()
print("How tall are you: ", end = '')
height = input()
print("How much do you weigh: ", end = '')
weight = input()
print(f"So you are {age} years old, Your height is {height}, and your weight is {weight}")

name = input("Name? ") # We can combine above print process
print(f"Your name is: {name}")

colour = input("What colour do you like the most?: ")
print("So, " + colour + "!")

prompt = "Stop! Show your identity"
prompt += "\nor we'll shoot: "
answer = input(prompt)
print("Oh, sorry " + answer + "!")

drinkingage = 21
childage = int(input("How old are you young man?"))

# print(childage >= drinkiningage answer will be False or True but it causes en error because input gets string value !!!!!

#drinkingage = int(drinkingage) is not necessary input() takes as a str()
print(childage >= drinkingage)







