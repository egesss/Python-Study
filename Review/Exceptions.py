# print(5/0) # WE GET ZeroDivisionError: division by zero ERROR

try:         # INSTEAD OF ERROR WE GET ANOTHER MESSAGE WE'VE WRITTEN !!!
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")

print("\nGive me two numbers, and I'll divide them")
print("Enter 'q' to quit.")

def division():
    while active:
        first_number = input("\nFirst Number: ")
        if first_number == 'q':
            break
        second_number = input("\nSecond Number: ")
        if second_number == 'q':
            break
        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("You can't divide by zero")
        else:                                 # ELSE HERE IS CONNECTED TO IF,TRY,EXCEPT BLOCK !!!!!!!!!!!!!!!!!!!!!!!!!
            print(answer)


active = True  # LOOK AT THE ACTIVE IN THE FUNCTION WE CAN ASSIGN ACTIVE VALUE EVEN AFTER THE FUNCTION !!!!!!!!!!!!!!!!
division()



