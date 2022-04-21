favourite_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}  # IT IS A BETTER WAY TO WRITE A LONG DICT !!!!!

for i in favourite_lang:  # To print all dict !!!!!
    print(f"{i.title()}'s fav lang is " + favourite_lang[i].title())

print(favourite_lang.items())

for name,lang in favourite_lang.items():  # Another way to print !!!!! items() take items in fav_lang !!!!! # two variable for loop Name takes first, Lang takes second
    print("\nName: " + name + "\nLang: " + lang)
print("\n")

print(favourite_lang.keys())

for name in favourite_lang.keys():  # keys only takes the initial values # default is 'name in fav_lang:' gives same output
    print(name.title())

friends = ['phil','sarah']

for name in favourite_lang.keys():
    print(name.title())
    if name in friends: # it name in friends == name in fav_lang if becomes True !!!!!
        print(" Hi " + name.title() + " Wow, Your fav lang is " + favourite_lang[name].title() + "!\n") # name subtitutes with values of keys() take which are names !!!!!

#Keys() is not just for LOOP !!!

if 'jon' not in favourite_lang.keys(): # we have use not for '!' likes in C,C++ !!!!!
    print("Jon tell us your fav lang\n")

# We can use sorted func

for name in sorted(favourite_lang.keys()):
    print(name.title() + ", thank you for taking the poll\n") # It is sorted temp in loop

favourite_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Taking Values

print(favourite_lang.values())

for lang in favourite_lang.values(): # values takes the second info which are values
    print(lang.title())
print("\n")
for lang in set(favourite_lang.values()): # set func takes unique values but not repetative ones !!!!!
    print(lang.title())






