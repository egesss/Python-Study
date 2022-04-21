colors = ['red', 'green', 'blue', 'yellow']
# deleted = del colors[0] it does not work because del is an operator

print(colors)
deleted1 = colors.pop()  # it deletes last item and we can return it to a value #default value is 0
print(colors)
print(deleted1)
deleted2 = colors.pop(0)
print(colors)
print(deleted2)
deleted3 = colors.pop(1)
print(colors)
print(deleted3)

shop_list = ["cheese", "egg", "milk", "butter", "ham"]
bought_item = []
for i in range(0,4):
    bought_item.append(shop_list.pop()) # we start from first element
    print(f"We bought {bought_item[i]}")
print("Bought Items:",bought_item)
print("Rest Items:",shop_list)

# TO REMOVE ITEM BY VALUE # remove() !!!!!

shop_list.remove('ham')
print(shop_list)

numbers = []

for i in range(0,10):
    numbers.append(i)
print(numbers)

for i in range(0,int(len(numbers)/2)): # we'll see this later but I used it !!!!! range(0,5) is enough
    numbers.remove(i*2) # it removes item we input to function directly
print(numbers)

for i in range(0,5):
    numbers[i] = 1
print(numbers)
numbers.remove(1)
print(numbers) # It only removes the first occurance we need a loop to delete all occurances !!!!!



