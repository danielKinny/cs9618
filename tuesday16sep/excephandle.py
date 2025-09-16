try:
    print(1/0)
except:
    print("there was a runtime error")
finally:
    print("This prints at the end")