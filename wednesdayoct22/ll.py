import random
class Node:
    def __init__(self,v):
        self.__next = None
        self.__prev = None
        self.__val = v
        
    def setNext(self,n):
        self.__next = n
        
    def getNext(self):
        return self.__next
        
    def getVal(self):
        return self.__val
        
arr = [Node(random.randint(1,100)) for i in range(10) ]
for node in arr:
    print(node.getVal())

print()

flag = True
while flag:
    flag = False
    for i in range(0,len(arr)-1):
        if arr[i].getVal() > arr[i+1].getVal():
            arr[i], arr[i+1] = arr[i+1], arr[i]
            flag = True
            if i+2 < len(arr):
                arr[i].setNext(arr[i+1])
                arr[i+1].setNext(arr[i+2])
            else:
                arr[i].setNext(arr[i+1])
                arr[i+1].setNext(None)
            
                

for node in arr:
    print(node.getVal())
    
for i in range(0,len(arr)-1):
    arr[i].setNext(arr[i+1])
    
            

    
    
    
