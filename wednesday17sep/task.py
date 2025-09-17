arr = [
    ["reading books" , 1, 0],
    ["computer games" , 2, 0],
    ["sports" , 3, 0],
    ["programming" , 4, 0],
    ["watching tv" , 5, 0]
]

flag = True
while flag:
    print("----------------------------------------------------------------")
    for hobby in arr:
        print(f"{hobby[1]}. {hobby[0]}")

    inp = -1

    print("----------------------------------------------------------------")

    try:
        inp = int(input("Enter the number of the hobby you want to pursue: "))
    except:
        print("\n Enter an integer \n")

    if inp == 0:
        flag = not flag
    elif not (inp>0 and inp<6):
        print("Enter a number between 1-5, or enter 0 to quit \n")
    else:
        arr[inp-1][2] += 1


#delimiting it using a comma

with open("hobbies.txt", "w") as f:
    for row in arr:
        f.write(f"{row[1]},{row[0]},{row[2]} \n")

#reading it back

with open("hobbies.txt", "r") as re:
    print(" \n")
    for line in re:
        line = line.strip().split(",")
        print(f"This is hobby number {line[0]}, it's name is {line[1]}, and you have chosen it {line[2]} number of times")
    
    
