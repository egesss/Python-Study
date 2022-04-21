def get_formatted_name(first,last):
    full_name = first + ' ' + last
    return full_name.title() # It returns a value

print(f"My full name is {get_formatted_name(last='selvi',first='ege')}")

def get_formatted_name2(first,middle,last): # extra argument here but may we do not need middle name !!!!!
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()

my_name = get_formatted_name2(last='selvi',first='ege',middle='mercan')
print(my_name)

def get_formatted_name3(first,last,middle = ''):  # we assign a default value to use efficiently
    if middle:  # If middle name defined, otherwise '' emphasize 0 !!!!!
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

my_name = get_formatted_name3('ege','selvi') # It is more efficient and now we don't need to function number 2 !!!!!
print(my_name)
my_name = get_formatted_name3('ege','selvi','mercan')
print(my_name)



