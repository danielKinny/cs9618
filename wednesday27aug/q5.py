string = input("Enter a string: ")
L = 0
R = len(string) - 1

while L < R:
    if string[L] != string[R]:
        print("The string is not a palindrome")
        break
    L += 1
    R -= 1

if L >= R:
    print("The string is a palindrome")
