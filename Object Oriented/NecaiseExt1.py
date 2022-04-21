# VARIABLE EQUALITY ?

class CashRegister():
    def __init__(self):
        self.balance = 0
    def addItem(self,cash):
        self.balance += cash
    def checkBalance(self):
        print(f"{type(self).__name__}",end='')
        print("'s balance is %.2f" % (self.balance))

reg1 = CashRegister()
reg1.addItem(2.95)
reg1.checkBalance()
reg2 = reg1
reg2.checkBalance()
reg2.addItem(3)
reg2.checkBalance()
if reg2 == reg1:
    print("SAME")
else:
    print("DIFFERENT")

# IF A VARIABLE CREATED BY ASSIGNING TO CREATED ONE EVEN IF THEY HAVE ALL VARIABLES DIFFERENT THEY ARE SAME

class Fraction():
    def __init__(self,numerator=0,denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator Cannot be Zero")
        elif numerator == 0:
            self.numerator = 0
            self.denominator = 1
        else:
            if (numerator < 0 and denominator >= 0 or numerator >= 0 and denominator < 0):
                sign = -1
            else:
                sign = 1
            a = abs(numerator)
            b = abs(denominator)
            while a % b != 0:
                tempA = a
                tempB = b
                a = tempB
                b = tempA % tempB

            self.numerator = abs(numerator) // b*sign
            self.denominator = abs(denominator) // b
    def __eq__(self,rhsvalue):
        return (self.numerator == rhsvalue.numerator and self.denominator == rhsvalue.denominator)
    def __add__(self, other):
        return ((self.numerator/self.denominator)+(other.numerator/other.denominator))
    def __abs__(self):
        return (abs(self.numerator/self.denominator))
    def __repr__(self):
        print(f"{self.numerator/self.denominator}")

frac1 = Fraction(1,8)
frac2 = Fraction(-2,4)
frac3 = Fraction(2,16)

if frac2 == frac1:
    print("for frac1 and frac2: SAME")
else:
    print("for frac1 and frac2: DIFFERENT")
if frac3 == frac1:
    print("for frac3 and frac1: SAME")
else:
    print("for frac3 and frac1: DIFFERENT")

#IF A VARIABLE CREATED WITH DIFFERENT INPUTS EVEN IF THEY HAVE ALL VARIABLE EQUAL TO EACH OTHER THEY ARE DIFFERENT

print(frac1+frac2)
print(frac2.numerator/frac2.denominator)
print(abs(frac2))
print(frac2)



