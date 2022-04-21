man = int(input("Enter number of man:\n"))
woman = input("Enter number of woman:\n")
woman = int(woman)

if man > woman:
    print("Man > Woman")
else:
    print("We need more man")
if woman > man:
    print("Woman > Man")
else:
    print("We need more women")
if man == woman:
    print("Always Sex")
if man in range(50,100):
    if 1 < woman < 10:
        print("That's a fucking destruction")
    else:
        print("That's a real orgy")


car = input("Enter number of cars:\n")
car = int(car)
driver = input("Enter number of drivers:\n")
driver = int(driver)

if car > driver:
    print("Lets ride")
elif driver > car:
    print("We need more car")

print("THERE IS AN OLD STORY\n\n")
print("You enter a dark rooom")

door = input("Select one of the door (1/2)>")
door = int(door) # to remove this code we need to write code below

if door == 1: # door == "1" then we do not need to assign str door to int door
    print("There is a bear, to do ?\n","1-Fight","2-Run")
    bear = input("(1/2)>")
    bear = int(bear)
    if bear == 1:
        print("You fucked up")
    elif bear == 2:
        print("You are running, you coward")
    else:
        print("You didnt do anything, you coward")
elif door == 2:
    print("You win")
else:
    print("Get the fuck out of here")



