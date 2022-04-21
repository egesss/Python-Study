# TO PREVENT MODIFICATION

unprinted_designs = ['case','robot','model']
completed_models = []
def print_models(model1,model2): # we take 2 arrays to modify
    while model1:
        current_design = model1.pop()
        print("Printing object: " + current_design)
        model2.append(current_design)
def show_models(model2):
    print("\nThe following materials have been printed: ")
    for model in model2:
        print(model)
print_models(unprinted_designs[:],completed_models) # WE CAN SAVE THE ORIGINAL LIST SO THAT !!!!!!!!!!!!!!!!!!!!!!!!!!
show_models(completed_models)
print(f"Original of the list has been saved: {unprinted_designs}")
print_models(unprinted_designs,completed_models)
print(f"Original of the list has not been saved: {unprinted_designs}")

# PASSING ARBITRARY NUMBER OF ARGUMENTS !!!!! AS MUCH AS WE WANT

def name_list(*names):
    print(names)
name_list('Ege','Yusuf')
name_list('Ege','Yusuf','Murat','Hasan','Cem') # I can give countless input as much as I want !!!!!

def sum_num(*numbers):  # Does not work if inputs are given as a list in this example !!!
    total = 0
    for number in numbers:
        total += number
    return total
print(f"Sum of 10,11,12,13,14,15 is: {sum_num(10,11,12,13,14,15)}")
def sum_num_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
tot_list = [10,11,12,13,14,15]
print(f"Sum of {tot_list} is: {sum_num_list(tot_list)}")

# WE CAN DEFINE A FUNCTION USEFUL

def sum_num(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
def sum_num_input():
    numbers = []
    active = True
    while active:
        numbers.append(int(input("Enter number: ")))
        ctrl = input("Do you want to continue: (if no enter 0): ")
        if ctrl == '0':
            active = False
    return numbers
total = sum_num(sum_num_input())
print("Total is " + str(total))

print("-------------------------TEST-----------------------------")

# tupple_list = ([1,2,3],[4,5,6])  Function above sees input so that !!!

def list_element(*lists):
    for i in range(0,len(lists)):
        print(f"List is: {lists[i]}")
        for j in lists[i]:
            print(f"Element of list: {j}")

list1 = [1,2,3]
list2 = [4,5,6]

list_element(list1,list2)

dict1 = {'name':'ege','surname':'selvi'}
dict2 = {'major':'physics','school':'bogazici'}

tupple_dict = (dict1,dict2)
print(tupple_dict)
print("--------------------------------------")
def dict_element(*dicts):
    for i in dicts:
        print(f"Items are {i}")
    for i in range(0,len(dicts)):
        print(f"Dict is {dicts[i]}")
        print(f"Keys are {dicts[i].keys()}")
        print(f"Values are {dicts[i].values()}")

dict_element(dict1,dict2)


