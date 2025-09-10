def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)


print(factorial(6))

def fib(n):
    if n-1==0 or n-2==0:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(4))