# MODULE OF MAKE_PIZZA

def make_pizza(size,*toppings):
    print(f"Making a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(topping)

def mean_numbers(mean,*numbers):
    total = 0
    for i in numbers:
        total += i
    return total / mean

def name_title(first,last):
    full_name = first.title() + ' ' + last.title()
    return full_name
