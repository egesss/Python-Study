message = ''
for i in range(0,5):
    message += 'Hello '
print(message)
print(len(message))

file_name = 'PI.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
pi_string2 = ''
for line in lines:
    pi_string += line.rstrip()
for line in lines:
    pi_string2 += line.strip() # IT REMOVES BLANK SPACES LEFT SIDE OF THE FILE !!!!!
print(pi_string)
print(pi_string2)
print(len(pi_string))

# LARGE FILES

file_name = 'Test_File\PI_ONEMILLIONDIGIT.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string3 = ''  # IT IS AN EMPTY STRING !!!!!
for line in lines:
    pi_string3 += line.strip()
print(pi_string3[:30] + "...")  # IT SHOWS US TO FIRST 30 DIGIT OF PI !!!!!
print(len(pi_string3))          # WE CAN USE STRINGS LIKE ARRAYS !!!!!

# IS MY DATA CONFINED IN MY FILE ?

file_name = 'Test_File\PI_ONEMILLIONDIGIT.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string4 = ''
for line in lines:
    pi_string4 += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string4:
    print("Your birthday in PI!")
else:
    print("Does not appear in PI!")






