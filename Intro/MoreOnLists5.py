digits = [1,2,3,4,5,6,7,8,9,0]
digits2 = [1,'a',2,'b',3,'c']
print("Min of the digits is",min(digits))
print("Max of the digits is",max(digits))
print("Min: ",min(digits),"Max: ",max(digits),"Sum: ",sum(digits))
# printing digits 2 cause error since it has strings between integer elements
sums = 0
for i in digits:
    sums += digits[i]
print(f"Sum of all digits is {sums}")
print("But it has a easy way to do",sum(digits)) # Easy way to add all digits in a list

# LIST COMPREHENSION FOR EASY WAY

squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)
print("\nANOTHER WAY TO DO THAT\n")
squares2 = [i**2 for i in range(1,11)]  # IT IS A LIST COMPREHENSION
squares3 = list(i**2 for i in range(1,11))  # Another way is using list function instead of using brackets
print(squares2)
print(squares3)
cubes = [cube**3 for cube in range(1,11)]
print(cubes)

# SLICING A LIST AND PRINT SPECIFIC ELEMENTS THAT LIES BETWEEN SOME ELEMENTS

colors = ['blue','red','green','yellow','purple']

print("1st",colors[1:3]) # It slice the elements included 1 not included 3
print("2nd",colors[0:5]) # So it'll print all the elements in the list # It is default of print(color)
print("3rd",colors[:3]) # It start from beginning of the list and goes to third element which is not included
print("4th",colors[1:]) # It start from the first element which is not included and goes to end of the list
print("5th",colors[-2:]) # Its perspective is from the last element and goes to third third element (color[2])


