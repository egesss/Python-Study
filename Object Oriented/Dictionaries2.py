alien = {'x pos': 0, 'y pos': 25, 'speed': 'med'}

print("Original x pos: " + str(alien['x pos']))

if alien['speed'] == 'slow':
    x_inc = 1
elif alien['speed'] == 'med':
    x_inc = 2
elif alien['speed'] == 'fast':
    x_inc = 3
alien['x pos'] += x_inc
print("Its pos now " + str(alien['x pos']))
alien['speed'] = 'fast'

if alien['speed'] == 'slow':
    x_inc = 1
elif alien['speed'] == 'med':
    x_inc = 2
elif alien['speed'] == 'fast':
    x_inc = 3
alien['x pos'] += x_inc
print("Its pos now " + str(alien['x pos']))

# TO REMOVE INFO

alien2 = {'color': 'red', 'points': '3'}
print(alien2)

list1 = [1,2,3,4,'cat']

del list1[0]
print(list1)
list1.remove('cat')
print(list1)
del alien2['color']
print(alien2)