char = ['c','b','d','a']
char.sort() # sort the list
print(char)
char.sort(reverse=True)
print(char) # in reverse order
char = ['c','b','d','a']
print("Original",char)
print(f"Original {char} vs Temp Sorted {sorted(char)}")
print(f"Original is saved {char}")
char.reverse() # reverse the list
print(char)

print(f"Length of the list char is {len(char)}") # finding length
char.append('e')
print(f"We added a new char and now is {len(char)}")

numbers = [1,2,3]
for i in numbers:
    print(f"The number is {i}")

    print("These are all the numbers we have\n") # Indexation error we need to be careful about the line

# CREATING A LIST

numbers2 = list(range(0,30))
print("Our list is",numbers2)

even_numbers = list(range(2,11,2)) # range(x,y,z) # z allow us to add z by z
print("Our even number list is",even_numbers)
divided_by_three = list(range(3,50,3))
print("Numbers that can be divided by three below 50 are\n", divided_by_three)

squares = []

for value in range(1,11):
    squares.append(value**2)
print("Square of every number below 100", squares)




