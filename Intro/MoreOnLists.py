color = ['blue', 'yellow', 'red',] # like C arrays elements in 0,1,2 !!!!!

print(color)
# print directly

for i in color: # 1st way
    print(f"1-Colors are {i}") # respectively
for i in range(0,3): # 2nd way
    print(f"2-Colors are {color[i]}")
for i in range(0,len(color)): # 3rd way
    print(f"3-Colors are {color[i]}")

message = "My eyes are" + " " + color[0].title() + "."
print(message)

for i in range(0,3):
    print(color[i].title())

print(color)
color[0] = 'purple'
print(color)
color.append('green') # append function adds element to list
print(color)

numbers = []
print("Enter random numbers:\n")
for i in range(1,6): # 1st way to insert
    numbers.append(input(f"{i}. number:"))
print(numbers)
numbers = []
print("Enter random numbers again:\n")

for j in range(0,5): # 2nd way to insert # we'll see not effective
    numbers.insert(j,input(f"{j+1}. number:")) # 1,6 and 0,5 are the same for insert function at first WHY ? See Below !!!!!
print(numbers)
print(numbers[0])

for j in range(1,6): # 2nd way to insert
    numbers.insert(j,input(f"{j}. number:")) # to see difference # insert does not overwrite !!!!!
print(numbers)
print(numbers[0])
numbers.insert(0, 15)
print(numbers)