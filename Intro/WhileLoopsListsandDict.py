unconfirmed_users = ['Ege', 'Caglar','Oguz']
confirmed_users = []

print(f"Unconfirmed Users {unconfirmed_users}")
print(f"Confirmed Users {confirmed_users}")

while unconfirmed_users: # [] implies 0 means False !!!!!
    current_user = unconfirmed_users.pop()  # default value of .pop(0) is zero
    print("Verifying User: " + current_user.title())
    confirmed_users.append(current_user)
print(f"Unconfirmed Users {unconfirmed_users}")
print(f"Confirmed Users {confirmed_users},\n\n")

pets = ['cat','dog','cat','goldfish','rabbit','cat']

while 'cat' in pets: # when all cats are removed 'cat' in pets return 0 means False !!!!!
    pets.remove('cat')
print(pets)


