def greet_user():  # EXPECTED TWO BLANK LINES AFTER FUNCTION FOR GOOD CODING
    print("Hello User")


greet_user()


def greet_user2(username):
    print("Hello," + username.title())


greet_user2('jesse')


def describe_pet(name,type):
    print(f"I have {type}\nand its name is {name}")


describe_pet(input("What is your pet name: "),input("What type of it: ")) # We also directly put our variables

for i in range(0,2):
    describe_pet(input("Name is: "),input("Type is: "))

describe_pet(type = 'Dog', name = 'Jo')  # We write variables reversed but we declare variable so that each select declared variables !!!!!

# DEFAULT VALUES


def describe_pet2(name,type = 'Dog'): # We declared that we'll take just name of the dogs
    print(f"I have {type} and its name is {name}")

describe_pet2('Jo')
describe_pet2('Jo','Cat') # If we put a variable a function having a default value it'll substitute with this default variable















