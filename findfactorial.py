def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defind for negetive numbers.")
else:
    factorial = fact(num)
    print("Factorial of",num, "is",factorial)
    
    