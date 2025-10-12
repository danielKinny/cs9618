import random

guesses = {
}

for i in range(5):
    string = input("Enter the name for user "+str(i+1)+": ")
    guesses[string] = 0

flag = True

for g in guesses:
    guess = random.randint(1,10)
    flag = True
    while flag:

        useinput = int(input(f"For user {g}, Enter number to search: "))
        if useinput == guess:
            print(f"User {g} Guessed it right!")
            flag = False
                
        elif useinput > guess:
            print("Guess is too high")
        else:
            print("Guess is too low")

        guesses[g] += 1

    print("----------------------------------------------------------------")

for g in guesses:
    print(f"User {g} took {guesses.get(g)} guesses")




