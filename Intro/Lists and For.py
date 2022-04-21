hairs = ['brown', 'blonde', 'red']
eyes = ['brown', 'green', 'blue']
weights = [1,2,3,4]

for types in hairs:
    print(f"Bitches are {types}")
for colors in eyes:
    print("These bitches' eyes are {}".format(colors))
for number in weights:
    print("Their numbers are %d" % number)

change = [1,'pennies',2,'dimes',3,'quarters']

for i in change: # mix lists are also okey
    print(f"In change {i}",end = ' ')

elements = []

for i in range(0,6): # last item in the range function is not included !!!!!
    print(f"Adding {i} to the list")
    elements.append(i) # append is a function that lists understand append number to the list

for i in elements:
    print(f"Element was {i}")

points = [[1,2],[3,4],[5,6]]

for i in points:
    print(f"Points of the triangle {i}")  # elements in list one by one
print("----------------------")
for i,j in points:
    print(f"Points of the triangle {i,j}")  # we can write down the multiarrays like this
print("----------------------")
for i,j in points:
    print(f"Points of the triangle {i},{j}")
print("----------------------")
for i in points:
    for j in i:
        print(f"Points of the triangle {i},{j}")