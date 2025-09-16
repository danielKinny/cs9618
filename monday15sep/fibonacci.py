def fib(n):
    if n-1==0 and n-2==0:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    