# WE'LL COMBINE LAST 2 OPERATION IN STORING DATA 1 HERE !!!

import json

filename = 'username.json'  # TRY FIRST AND SEE ELSE OPTION THEN NAME 'username.json2' and SEE WHAT HAPPENS !!!!!!!!!!!

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name: ")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back " + username)
else:
    print("Welcome back, " + username)



