def factorial(n):

    print("----------------------------")

    print("recursive call number: ",n)
    print("n==0: ",(n==0))

    if n==0:
        return 1
    else:
        print(n," * factorial(",n-1,")")

    result = n*factorial(n-1)
    print("---------------------")
    print("this part is : ", result)
    return result

print()
print("The result of the factorial is: ",factorial(6))