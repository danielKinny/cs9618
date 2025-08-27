#factorial

def factorial(n):
    if n-1 == 0:
        return n
    return n * factorial(n-1)

num = int(input("Enter the number: "))

print(factorial(num))

