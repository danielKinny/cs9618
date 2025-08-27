import random

randomNum = random.randint(1,20)

num = -1

while num != randomNum:
    num = int(input("Guess the number: "))
    if num > randomNum:
        print("Guess is too high")
    elif num < randomNum:
        print("Guess is too low")
    else:
        print("You guessed right!")

