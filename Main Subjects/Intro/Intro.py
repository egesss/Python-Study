message = "Hello World Python"

print(message)
print("Hello World Fuckers")

name = "ege selvi"
print(name.title())  # title is a function that takes a string and make it title'd # . is act mechanism we'll come after

name1 = "Ege SELVİ"

print(name.upper())
print(name.lower())

a1 = 'This is a string'
a2 = "This is also a string"

print(a1,'-',a2)

firstname = "ege"
lastname = "selvi"
fullname = firstname + lastname  # for space we need to write firstname + " " + lastname
fullname1 = firstname + " " + lastname
print(fullname)
print(fullname1)

print("Hello Mr", fullname1.title(),'!')
print("Hello Mr", fullname1.title().upper())
message1 = "Hello " + fullname1.title() + " !"
print(message1)

print("Languages:\n1-C\n\t2-C++\n\t3-Python")

# "python" and "python " are different strings

lang = "python "
print(lang,'space')
print(lang.rstrip(),'no space') # handle spaces in a string temporarily # right strip (rstrip)
lang = lang.rstrip()
print(lang,'no space') # spaces handled permanently
lang1 = " python" # same process can be handled with lstrip() function to remove left space






