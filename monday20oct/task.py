arr = [1,2,3,4,5,6,7,8,9,10]

found = False
l = 0
r = len(arr)-1
target = 1
c = 1

while r>l and not found:
    print(f"iteration number {c}")
    mid = (r+l)//2
    
    if arr[mid] == target:
        found = True
        print("Number has been found")
    elif arr[mid] > target:
        r = mid-1
    else:
        l = mid+1
        
    r-=1
    l+=1
    c+=1
    
print(f"iteration number {c}")
