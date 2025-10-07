arr = [93,54,47,28,17,6]
swaps = True
counter = 1
print("Bubble Sort")
while swaps:
    print(f"This is swap number {counter}: ", end="")
    print(arr)
    swaps = False
    for i in range(len(arr)-1):
        fe = arr[i]
        le = arr[i+1]
        if fe > le:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            swaps = True
    counter+=1
    
print("----------------------------------------------")
print("Insertion Sort")
arr1 = [47,6,54,17,93,28]
scounter = 1
for pointer in range(1,len(arr1)):
    
    print(f"This is swap number {scounter}: ",end="")
    print(arr1)
    scounter +=1
    
    currentItemPointer = pointer - 1
    itemToBeInserted = arr1[pointer]
    while currentItemPointer > -1 and (itemToBeInserted < arr1[currentItemPointer]):
        arr1[currentItemPointer+1] = arr1[currentItemPointer]
        currentItemPointer -= 1

    arr1[currentItemPointer + 1] = itemToBeInserted
