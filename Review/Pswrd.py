from random import *

def randomCharacter1(example = "abcdefghijklmnoprstuvyzx"):
    random = randint(0,len(example)-1)
    randchar = example[random]
    return randchar

def randomCharacter2(example = "0123456789"):
    random = randint(0, len(example) - 1)
    randchar = example[random]
    return randchar

def randomCharacter3(example = "+-*/?!@#$%&"):
    random = randint(0, len(example) - 1)
    randchar = example[random]
    return randchar

def randomCharacter4(example = "ABCDEFGHIJKLMNOPRSTUVYZX"):
    random = randint(0,len(example)-1)
    randchar = example[random]
    return randchar

def charControl(password,randomchar):
    if randomchar in password:
        return True
    else:
        return False

def makePassword(length):
    password = ""
    randchar = ""
    for i in range(0,length,1):
        tempi = i
        funcindex = randint(1,4)
        if funcindex == 1:
            randchar = randomCharacter1()
            if charControl(password,randchar):
                i = tempi
                continue
            else:
                password += randchar
        elif funcindex == 2:
            randchar = randomCharacter2()
            if charControl(password,randchar):
                i = tempi
                continue
            else:
                password += randchar
        elif funcindex == 3:
            randchar = randomCharacter3()
            if charControl(password,randchar):
                i = tempi
                continue
            else:
                password += randchar
        elif funcindex == 4:
            randchar = randomCharacter4()
            if charControl(password,randchar):
                i = tempi
                continue
            else:
                password += randchar
    return password

passlength = int(input("Password length:"))
print("Random password is: " + makePassword(passlength))
