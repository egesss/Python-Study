print("\nANOTHER WAY TO CHANGE LİST\n")
numbers = [1,2,3,4,5]
numbers2 = [1,2,3,4,5]
print(numbers2)
for i in range(1,6):
    numbers2[i-1] = int(input(f"Change {i}. element in list: "))
print(numbers2)

# TO DELETE

del numbers2[0]
print("Deleted >",numbers2)
print(f"{numbers2[0]} was the second element now first") # old 1st element takes 0 position in list

for i in range(0,4): # difference between str() and int() input and initialization " str() = '11' int() = 11 " !!!!!
    del numbers2[0]
    print(numbers2)
for i in range(0,5):
    del numbers[0] # it deletes the element so we write numbers[0] !!!!!
    print(numbers)

print("ANOTHER WAY TO EMPTY LIST\n")
numbers2 = [1,2,3,4,5]

for i in range(0,5):
    numbers2[i] = ''  # it empty the element so we write numbers[i] !!!!!
    print(numbers2)

numbers3 = [1,2,3,4,5]
print(numbers3)
for i in range(len(numbers3)-1,-1,-1):
    del numbers3[i]
print(numbers3)



