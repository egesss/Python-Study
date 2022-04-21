# PASSING A DICT

def build_person(first,last): # TO RETURN A DICT !!!!!
    person = {'first': first, 'last': last}
    return person

musician = build_person(input("Name: "),input("Last: "))
print(musician)
print(f"My full_name is {musician['first'].title() + ' ' + musician['last'].upper()}")

def build_person(first,last,age = ''):  # we have default variable
    person = {'first': first, 'last': last}
    if age:  # if age is not '' (default,not given) that is True
        person['age'] = age
    return person

musician = build_person(input("Name: "),input("Last: ")) # Age is not specified
print(musician)
musician = build_person('Ege','Selvi',22) # Now we can put age inside the dict
print(musician)

# WITH A LOOP

def get_name_surname(first,last):
    full_name = first + ' ' + last
    return full_name.title()

active = True

while active:
    name_surname = get_name_surname(input("First name: "),input("Last name: "))
    print("\nHello, " + name_surname + "!")
    process = input("Do you want to continue(y/q): ")
    if process == 'q':
        break



