# FILE

def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)
def print_a_line(line_count,f):
    print(line_count,f.readline())

current_file = open('Read.txt')  # default of the function is 'r' mode !!!

print("First print all file: ")
print_all(current_file)
print("We'll dont see anything: ")
print_all(current_file)
print("Now we'll see when we rewinded: ")
rewind(current_file)
print_all(current_file)
rewind(current_file)
current_line = 1
print_a_line(current_line,current_file)
current_line += 1
print_a_line(current_line,current_file)
current_line += 1
print_a_line(current_line,current_file)

# CLASS OBJECTS

class Animal(object):
    pass

class Dog(Animal):
    def __init__(self,name):
        self.name = name
class Cat(Animal):
    def __init__(self,name):
        self.name = name

class Person(object):  # object is the default value and equivalent is !!! class Person(void) !!!
    def __init__(self,work):
        self.name = name
class Employee(Person):
    def __init__(self,name,salary):
        super(Employee, self).__init__(name)
        self.salary = salary

# ANALYZING TEXT .split operator !!!

title = "Alice in Wonderland"
splitted_title = title.split()
for title in splitted_title:
    print(f"{title}")
print(splitted_title)

# pass STATEMENT !!!

even = []

for i in range(1,10):
    if i % 2 == 0:
        even.append(i)
    else:
        continue
    if i % 2 != 0:
        print("There are also odd numbers")
print(f"{'-'*10}" + "PASS ARGUMENT" + f"{'-'*10}\n")
for i in range(1,10):
    if i % 2 == 0:
        even.append(i)
    else:
        pass
    if i % 2 != 0:
        print("There are also odd numbers")