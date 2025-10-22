def bin(l,h):
    mid = (h+l)//2
    if h<l :
        return False, mid
    if arr[mid] == target:
        return True, mid
    elif arr[mid] > target:
        return bin(l,mid-1)
    else:
        return bin(mid+1,h)
   
global target
target = 8
arr = [1,2,3,4,5,6,7,8,9,10]
found, idx = bin(0,len(arr)-1)

if found:
    print(f"The number was found at index: {idx}")
else:
    print("The number is not found")
