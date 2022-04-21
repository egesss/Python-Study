def add_numbers(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total

print("We can do math inside of a function argument")
sum1 = add_numbers(10+20,2**5)
print(sum1)

print("And combine variables")
sum2 = add_numbers(sum1*10,sum1**(sum1*sum1))
print(sum2)

