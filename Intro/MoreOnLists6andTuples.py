colors = ['blue', 'red', 'green', 'yellow', 'purple']

for i in colors:  # Normal way to print all the elements in a list
    print(f"{i.title()}", end=' ')
print("\n")
for i in colors[:3]:  # Specific way to print # Goes until 3rd element
    print(f"{i.title()}")

# TO COPY A LIST

numbers = [1, 2, 3, 4]
numbers2 = []
numbers3 = []

numbers2 = numbers  # we can write also !!!!! numbers2 = numbers[:] It is better
numbers2.append(5)  # copied and added '5'
print("All the list is copied", numbers2)
numbers3 = numbers2[0:2]  #we can copy a part of the list
print("We copied the a part of the list", numbers3)

# TUPLES

triple = (5,10,15)
triple2 = 5,10,15

print(triple)
print(triple2)
print(f"First and Second Element of the Tuple Respectively is {triple[0]} and {triple[1]}")
print(f"Length of the Tuple is {len(triple)}")
print(f"Is Element 15 in Tuple {15 in triple}")
print(f"Is Element 20 in Tuple {20 in triple}")

for i in triple:
    print(f"{i+1}.Element is {i}")
print("--------------------------")
for i in range(0,len(triple)):
    print(f"{i+1}.Element is {triple[i]}")

colors_t = ('blue','red')
dimensions_t = (200,50)

print("Dimensions of the square is %d and %d" % dimensions_t)

for i in range(0,len(dimensions_t)): # It likes lists
    print(f"{dimensions_t[i]}")

# dimensions_t[0] = 150 TypeError: 'tuple' object does not support item assignment CAN NOT BE MODIFIED !!!

dimensions_t = (100,25)  # We can assign new values so that

for i in dimensions_t:
    print(f"{i}")

a = sum([1,3])
b = sum([1,7,2,9])

values = (a,b)

def sum(*value):
    total = 0
    for element in values:
        total += element
    return total

print(f"Tot1 = {a}, Tot2 = {b}, Tot1+Tot2 = {sum(values)}")

# USING TUPLES TO RETURN MULTIPLE VARIABLE FROM A FUNCTION

def ReadDate():
    month = int(input("Month: "))
    day = int(input("Day: "))
    year = int(input("Year: "))
    return (month,day,year)
date = ReadDate()
# OR WE CAN USE A TUPLE WITH THE SAME LENGTH OF THE OUTPUT OF THE FUNCTION
# (month,day,year) = ReadDate()
print(date)









