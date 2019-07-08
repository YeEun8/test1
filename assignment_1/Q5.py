num = int(input("enter the number : "))

def myFactorial (n) :
    if n == 1:
        return 1
    return n * myFactorial(n-1)

print("{0}! : {1}".format(num, myFactorial(num)))
