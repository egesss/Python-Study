names = ['Luigi','Gumbys', 'Spiny']

cast = set(names)  # It makes a Dict using elements in names !!!
print(cast)
# cast = set() To create a empty set

numberofcharac = len(cast)

for character in sorted(cast):
    print(character)
# for i in range(0,numberofcharac):  Cause ERROR !!!
    # print(cast[i])

cast2 = set(['Luigi','Arthur','James'])
print(cast)
cast2.add('Spiny')
print(cast2)
cast2.discard('James')  # Has no effect on error if item is not in the set
print(cast2)
cast2.clear()
print(cast2)

canadian = {'Red','White'}
british = {'Red','Blue','White'}
italian = {'Red','White','Green'}

if canadian.issubset(british):
    print("Canadian is also Italian")
if not italian.issubset(british):
    print("Italian is not also a British")

inEither = british.union(italian)
print(inEither)

inBoth = british.intersection(italian)
print(inBoth)

print(f"Difference between Italian And British Flag {british.difference(italian)}")


