# INPUT !!!!!

# LIST IN A DICT

numbers = {
    'even': [2,4,6,8],
    'odd': [1,3,5,7]
}
for i in numbers.items():
    print(f"Item: {i} Key: {i[0]} Value: {i[1]}")  #We get dict items as tuples so we can reach them using brackets !!!
print("-------------------")
for i in numbers.keys():
    print(f"Key is {i}")
print("-------------------")
for i in numbers.values():
    print(f"Value is {i}")
print("-------------------")
list1 = [[1,2,3],[4,5,6],[7,8,9]]
for i in list1:
    for j in i:
        print(f"Element is: {j}")
print("-------------------")
for i in numbers.items():
    for j in i[1]:
        print(j)
print("-------------------")
for i,j in numbers.items():
    print(f"There are {i} numbers: {j}")
print("-------------------")


print("\n")
fav_languages = {
    'jen': ['python','java'],
    'sarah': ['C','C++'],
    'edward': ['ruby', 'java'],
    'phil': ['python','ruby']
}
for name,lang in fav_languages.items():
    print(f"{name.title()}'s fav languages are: {lang[:]}")
    if 'python'in lang:  # We can search a dict having a list
        print(f"Wow {name},so you like python")
def append_dict(dict,list):
    list.append(dict)
    return list
print("\n")

talks = []
active = True

while active:
    response = {}
    name = input("What is your name: ")  # name defined as a string so see ***
    fav_number = input("Fav number: ")
    response[name] = fav_number  # FOR INPUT WE NEED TO WRITE SO THAT !!!!!!!!!!! *** we dont 'name' here since it is already string
    append_dict(dict = response, list = talks)
    print(talks)
    repeat = input("Another person: (yes/no) ")
    if repeat == 'no':
        active = False

stuff = {}  # WE CAN USE DICT LIKE LIST LIKE THAT !!!!! NOT EFFICIENT
stuff['name'] = 'Ege'
stuff['surname'] = 'Selvi'
stuff[1] = 1.75
stuff[2] = 90
print(stuff,f"Name is: {stuff['name']}")




