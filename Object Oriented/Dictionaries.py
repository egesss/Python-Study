alien = {'color': 'green', 'points': 5} # like structures in C, C++ !!!!!

print(alien['color'])
print(alien['points'])

new_points = alien['points']
print("You have earned " + str(new_points) + " points!")

# ADDING NEW INFO

alien['x point'] = 0 # ADDING NEW ELEMENT TO DICT dict[element] !!!!!
alien['y point'] = 25
print(alien)

alien2 = {}
alien2['color'] = 'blue'
alien2['points'] = 4
print(alien2)

alien3 = {'color': 'yellow'}
print("The alien is " + alien3['color'] + ".")
alien3['color'] = 'blue'
print("The alien is now " + alien3['color'] + ".")

