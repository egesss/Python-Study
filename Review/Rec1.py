# RECURSION
# EXAMPLE 1

def main():
    area = triangleArea(50)
    print("Area:",area)
def triangleArea(sidelength):
    if sidelength <= 0:
        return 0
    elif sidelength == 1:
        return 1
    smallerlength = sidelength - 1
    smallerarea = triangleArea(smallerlength)
    area = smallerarea + sidelength
    return area
main()

# EXAMPLE 2

def main2():
    n = int(input("Enter n: "))
    for i in range(1,n+1):
        f = fib(i)
        print("fib(%d): %d" % (i,f))

def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

main2()