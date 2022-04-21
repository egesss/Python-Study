def get_name_surname(first,last):
    full_name = first + ' ' + last
    return full_name.title()


office = {'People': [], 'Age': []}
office2 = {}
for i in range(0,3):
    office['People'].append(get_name_surname(input("Name: "), input("Surname: ")))
    office['Age'].insert(i,input(f"How old {office['People'][i]}: "))
print(office)
for i in range(1,4):  # We'll define three person !!!!!
    office2[f'{i}.Person'] = get_name_surname(input("Name: "), input("Surname: "))
print(office2)

# PASSING A LIST !!!!!

def greet_names(names): # we'll put many variables !!!!!
    for name in names:
        print("Hello " + name.title() + "!")

usernames = ['ege','cago','oguz'] # we put many variables to function !!!!!
greet_names(usernames)

def greet_names(names):  # another way to pass list of arguments to function
    for i in range(0,len(names)):
        print("Hello " + names[i].title() + "!")
greet_names(usernames)

# MODIFYING LISTS

unprinted_designs = ['case','robot','model']
completed_models = []

while unprinted_designs: # we'll modify this array and when we've removed all elements it'll be '[]' means 0 while loop ends !!!!!
    current_design = unprinted_designs.pop()
    print("Printing objects: " + current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model,end=' ')

# WE'LL WRITE THIS PROGRAM WITH 2 FUNCTIONS

unprinted_designs = ['case','robot','model']
completed_models = []
print("\n")
def print_models(model1,model2): # we take 2 arrays to modify
    while model1:
        current_design = model1.pop()
        print("Printing object: " + current_design)
        model2.append(current_design)
def show_models(model2):
    print("\nThe following materials have been printed: ")
    for model in model2:
        print(model)
print_models(unprinted_designs,completed_models)
show_models(completed_models)
print("Unprinted designs", unprinted_designs)
print("Printed models", completed_models)


