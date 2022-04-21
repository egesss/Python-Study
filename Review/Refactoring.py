# TO RUN THIS CODE EFFICIENTLY DELETE FILES AFTER PY IS WORKED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import json
print("Function1:\n")
def greet_user():
    filename = 'username1.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name: ")
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you " + username)
    else:
        print("Welcome back " + username)
greet_user()
print("Function2:\n")

def get_stored_name():
    filename = 'username2.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user2():
    username = get_stored_name()
    if username:  # IF THERE IS NO USERNAME MEANS NONE WHICH IS '0' NO ENTER TO IF BLOCK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print("Welcome back, " + username)
    else:
        username = input("What is your name: ")
        filename = 'username2.json'
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you " + username)
greet_user2()
print("Function3:\n")

def get_stored_name2():
    filename = 'username3.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("What is your name: ")
    filename = 'username3.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username
def greet_user3():
    username = get_stored_name2()
    if username:
        print("Welcome back, " + username)
    else:
        username = get_new_username()
        print("We'll remember you " + username)
greet_user3()

