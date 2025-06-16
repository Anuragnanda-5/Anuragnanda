#Factorial
input('enter a number: ')
def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)

res = factorial(5)
print('factorial of 5 is ',res)

