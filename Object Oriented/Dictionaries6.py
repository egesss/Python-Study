conference = {  # DICT IN DICT !!!!!
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'awards': ['photoelectric','special_relativity','general_relativity']
    },
    'mcurie':{
        'first': 'madam',
        'last': 'curie',
        'location': 'paris',
        'awards' : ['x-ray','radium','radiation']
        }
}

for i in conference.items():
    print(f"Key is: {i[0]}, Value is: {i[1]}")
print("-------------------")
for i in conference.keys():
    print(i)
print("-------------------")
for i in conference.values():
    print(i)
print("-------------------")
for i in conference.values():
    print(f"Item in Main Key is {i.items()}\n")
    print(f"Key in Main Key is {i.keys()}\n")
    print(f"Value in Main Key is {i.values()}\n")
print("-------------------")
for i,j in conference.items():
    print(f"Member: {i}, Name: {j['first'].title()}, Surname: {j['last'].title()}")
    if j['first'] == 'albert':
        for k in j['awards']:
            print(f"Sir {j['first'].title()}'s works is {k}")

if 'photoelectric' in conference['aeinstein']['awards']:
    print(f"Sir Einstein gain noble for his working on photoelectric")

print("\n-----------------FOR TEST-------------------\n")

print(conference['aeinstein']['awards'][0])
ab = {'a1':'a2','b1':'b2'}
cd = {'c1':'c2','d1':'d2'}
list1 = [ab,cd]
print(list1)
quantumphysics = {'particle': 'photoelectric effect','quantum':'bose-einstein condensation'}
relativity = {'special': 'special relativity', 'general': 'general relativity'}
conference2 = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'awards': [quantumphysics,relativity]
    },
    'mcurie':{
        'first': 'madam',
        'last': 'curie',
        'location': 'paris',
        'awards' : ['x-ray','radium','radiation']
        }
}

print("\n")

print(f"And nobel prize for the work {conference2['aeinstein']['awards'][0]['quantum']} goes to Einstein")






