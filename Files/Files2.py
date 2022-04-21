# READING LINE BY LINE

filename = 'PI.txt'
count = 0
with open(filename) as file_object:
    for line in file_object:
        count += 1
        print(f"{count}.line {line.rstrip()}") # WE USE RSTRIP FOR REMOVE BLANK SPACE BETWEEN EVERY LINES DELETE AND SEE !!!!!

# MAKING A LIST FROM A FILE
print("\n")
count = 0
with open(filename) as file_object:
    lines = file_object.readlines()  # USE !!!!! READLINE() AND SEE WHAT HAPPENS !!!!!
    everyline = file_object.readline()  # SEE WHAT HAPPENS WHEN WE WANT TO READ AGAIN !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

for line in lines:
    count += 1
    print(f"{count}.line " + line.rstrip())
print(lines)
print(everyline) # WE WON'T SEE ANYTHING IN THE CONSOLE !!!!!

with open(filename) as file_object:
    lines = file_object.readline()
    everyline = file_object.readlines()  # SEE WHAT HAPPENS WHEN WE WANT TO READ AGAIN !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
count = 0
for line in lines:
    count += 1
    print(f"{count}.line " + line.rstrip())
print(lines)
print(everyline)





