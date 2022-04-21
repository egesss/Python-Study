# JSON MODULE !!! JAVA SCRIPT OBJECT NOTATION !!!

import json

numbers = [i for i in range(2,20,3)]

filename = 'numbers.json'

with open(filename,'w') as f_obj:  # WE CAN WRITE SO THAT
    json.dump(numbers,f_obj)
numbers = []
print(numbers)
with open(filename) as f_obj:  # WE CAN GET INFO SO THAT
    numbers = json.load(f_obj)
print(numbers)

# SAVING AND READING USER GENERATED DATA !!!

username = input("What is your name: ")

filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back " + username)

filename = 'username.json'

with open (filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username)


