numbers = [i for i in range(0,21)]
print(numbers)

for i in numbers:
    if i % 2 == 0:
        print(f"{i} is an even number")
for i in numbers:
    print(numbers[i] % 2 == 0, end=' ')  # It'll print one true one false
print("\n")
for i in numbers:
    print(numbers[i] % 2 != 0, end=' ')  # It'll print one false one true
print("\n")
car = 'Audi'
print(f"\nIs it {car.lower() == 'audi'}")

# TO CHECK A VALUE WHETHER IN A LIST

print("Is 2 in the numbers list", 2 in numbers)
print("Is 21 in the numbers list", 21 in numbers)










