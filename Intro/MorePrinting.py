people = 10

x = f"There are {people} people here"  # f allow us to write while we are writing values inside the ""
print(x)

yes = False
no = True
joke_evaluation = "Isn't that joke so funny! {}"

print(joke_evaluation.format(yes))  # format enters the input in the bracket

w = "Many people"
y = " are also here"

print(w + y)
print("It is not {}".format('funny'))  # we can put also like this
print('Ege ' * 10)  # we can print many strings like this

end1 = "E"
end2 = "g"
end3 = "e"
end4 = "R"
end5 = "u"
end6 = "n"
print(end4 + end5 + end6, end = ' ')  # we can delete the '\n' with end = ' '
print(end1 + end2 + end3)
print(end4 + end5 + end6)
print(end1 + end2 + end3)

formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(formatter,"1","",""))
print(formatter.format(formatter,formatter,"2",""))

days = "Sun\nMon\nTues\nWed\nThurs\nFri\nSat"

print(f"Months are: \n{days}")

# print("We write
# but cant jump to another line)

# double-quotes allow to do that
print("""
There's something
Here
We can write as much as we want
4 lines or may be 5 or 6
""")
