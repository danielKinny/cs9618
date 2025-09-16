def func(n):
    if n==0 or n==1:
        print(n)
    else:
        func(n//2)
        print(n%2)

func(19)