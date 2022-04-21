def make_pizza(*toppings):  # '*' creates a tupple toppings(value_1,value_2...) temporarily !!!!!
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(topping)
make_pizza('Pepperoni')
make_pizza('Mushrooms','Green Peppers','Extra Cheese')
print("\n")

# Mixing Arguments

def make_pizza2(size,*toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(topping)
make_pizza2(16,'Pepperoni') # size = 16 cause error !!!!!
make_pizza2(12,'Mushrooms','Green Peppers','Extra Cheese')
print("\n")

ege = ['blue','tall','physics']
def build_profile(name,surname,user_profile): # !!!!! write function (name,surname,*user_profile) and SEE WHAT HAPPENS !!!!!
    profile = {}                              # If we write *user_profile func sees input so that (name,surname, !!!!! tuple(user_profile[],...) !!!!!
    profile['first_name'] = name
    profile['last_name'] = surname
    profile['feature'] = []
    for i in user_profile:
        profile['feature'].append(i)          # And it turns two times because tuple has at least two elements !!!!!
    return profile
print(build_profile('ege','selvi',ege))

ege2 = {'eye':'blue','height':'tall','major':'physics'}
def build_profile2(name,surname,user_profile): # If we write !!!!!*user_profile func sees tuple({...:...},...) and cause error !!!!!
    profile = {}
    profile['first_name'] = name
    profile['last_name'] = surname
    for i,j in user_profile.items():
        profile[i] = j
    return profile
print(build_profile2('ege','selvi',ege2))

# Using Arbitrary Keyword Arguments

def build_profile3(first,last,**user_info): # '**' double asteriks creates a dict user_info{'key_1': value_1,'key_2':value_2...} so that temporarily !!!!!
    profile = {}                            # above example we give our input from a dict now we give arguments ourself !!!!!
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile3('ege','selvi',eye = 'blue',height = 'tall', major = 'physics') # same input with above !!!!!
print(user_profile)

