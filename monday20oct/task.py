arr = [7,12,19,23,27,33,37,41,56,59,60,62,71,75,80,84,88,92,99]

found = False
l = 0
r = len(arr)-1
target = 34
c = 1

while r>=l and not found:
    print(f"iteration number {c}")
    mid = (r+l)//2
    
    if arr[mid] == target:
        found = True
    elif arr[mid] > target:
        r = mid-1
        
    else:
        l = mid+1
        
    c+=1

print()

if found:
    print("Number has been found")
else:
    print("This number is not within the list")
    
print(f"total iterations {c}")
