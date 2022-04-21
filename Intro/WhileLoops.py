number = 1

while number <= 5:
    print(number)
    number += 1
numberarr = []
i = 0
while i < 6:
    numberarr.append(i)
    print(numberarr)
    i+=1

task = ""
message = ""
prompt = "Select the task to be done\n1-Sum\n2-Extract\n3-Multiply\n4-Divide\n5-Quit\n"

while message != "quit":
    task = input("Select the task to be done\n1-Sum\n2-Extract\n3-Multiply\n4-Divide\n")
    message = input("Do you want to continue: If no (quit)\n")

active = True
while active:
    message = input(prompt)
    print(message)
    if message == "5":
        active = False
    else:
        print(message)
active = True
while active:
    message = input(prompt)
    if message == "5":
        break
    else:
        print("Do another task")
number = 0
numberarr2 = []
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    numberarr2.append(number)
print(numberarr2)

