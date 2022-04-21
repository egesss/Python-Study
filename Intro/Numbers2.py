n1 = abs(-10)
n2 = 1.84
n3 = 1.85
print(n1)
print(round(n2))
print(round(n2,1))
print(round(n3,1))
print(max(5,1,2,4,3))
print(min(5,1,2,4,3))

name = "Harry"

first = name[0]
last = name[len(name)-1]
print(first + last)

name = "John Smith "
name2 = name.replace("John", "Jane")
print("Welcome " , "Mr " , name , "& " , "Mrs " , name2)
print("Welcome" , "Mr" , name , "&" , "Mrs" , name2)
print("Welcome " + "Mr " + name + "& " + "Mrs " + name2)

code = 121212
price = 1.21596267441344
print("Price of the product: %.2f code after %d" % (price,code))

title1 = "Quantity:"
title2 = "Price:"
print("%10s %10d" % (title1,24))
print("%10s %10.2f" % (title2,17.29))  # right justify

print("%-10s %10d" % (title1,24))
print("%-10s %10.2f" % (title2,17.29))  # left justify