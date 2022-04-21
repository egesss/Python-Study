# NESTING # !!!!!

alien1 = {'color': 'red', 'points': '3'}
alien2 = {'color': 'blue', 'points': '4'}
alien3 = {'color': 'green', 'points': '5'}

aliens = [alien1,alien2,alien3] # list of dictionaries !!!!!
print(aliens)
for alien in aliens:
    print(alien)
print("\n")
for alien in aliens:
    print(f"Attributes of aliens are: {alien.keys()}")
print("\n")
for alien in aliens:
    print(f"Color of one alien is : {alien['color']}")
# Lets make 3 aliens from the beginning
print("\n")

aliens = []

for i in range(0,5):
    new_alien = {'color': 'red', 'points': '3'}
    aliens.append(new_alien)
print(aliens)  # We make 5 red aliens

for alien in aliens[:3]:  # To show first 3
    print(alien)
print("Total number of aliens having been created is: " + str(len(aliens)))

# We want to modify some aliens

for alien in aliens[:3]:  # alien here substitute with all object in the dict list !!!!!
    if alien['color'] == 'red':
        alien['color'] = 'green'
        alien['points'] = 4
print(aliens) # first three have been changed and last two remained same





