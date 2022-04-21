import FunctionsAndModules  # We import the name of the module having our function !!!!!
                            # FunctionsAndModules and all its functions available in UsingModule1 Now !!!!!

FunctionsAndModules.make_pizza(16,'Pepperoni') # and call it so that !!!!!
FunctionsAndModules.make_pizza(12,'Pepperoni','Mushroom','Cheese')
# module_name.function_name() !!!!!
print("\n")

# SPECIFIC FUNCTIONS # !!!!! from module_name import function_name

from FunctionsAndModules import mean_numbers

mean = mean_numbers(3,15,67,14)
print(mean)

def name_title(first,last): # We have same function and they will conflict then we write below !!!!!
    full_name = first.title() + ' ' + last.title()
    return full_name

from FunctionsAndModules import name_title as nt # from module_name import function_name as something !!!!!

print(name_title('ege','selvi'))
print(nt('ege','selvi')) # gives same result !!!!!

# MODULE RENAME # import module_name as something !!!!!

import FunctionsAndModules as modul1 # now our long name becomes modul1 !!!!!

mean = modul1.mean_numbers(3,15,67,84)
print(mean)

# IMPORTING ALL FUNCTIONS with '*'

from FunctionsAndModules import * # Now we can use all functions inside the FunctionsAndModules

# INSTEAD OF USING DOT NOTATION
# FunctionsAndModules.make_pizza(16,'Pepperoni') or modul1.mean_numbers(3,14,65,84) !!!!! WE CAN WRITE,

make_pizza(12,'Pepperoni')
mean = mean_numbers(3,14,25,36)
print(mean)








