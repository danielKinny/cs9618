try:
    print(1/0)
except:
    print("there was a runtime error")
finally:
    print("This prints at the end")

while True:

    string = input("Enter an integer: ")
    try:
        result = int(string)
        break
    except:
        print("The thing thats been entered is not an integer")
    finally:
        print('This try-catch block has finished')