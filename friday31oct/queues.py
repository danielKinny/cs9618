"""

icba to explain the logic for queues
queues are fifo

only difference im finding is in the dequeue func
we essentially use the same logic as deleting the beginning node in a linkedlist
enqueue logic is same as pushing onto a stack

"""






class Node:
    def __init__(self,v):
        self.data = v
        self.ptr = None
    
def initialise():
    queue = []
    for i in range(8):
        queue.append(Node("-"))
        queue[i].ptr = i+1
    queue[-1].ptr = -1
    return queue
    
def printNodes(nodes,flp,sp):
    print()
    print(f"Current FLP is: {flp} and SP is {sp}")
    for i in range(len(nodes)):
        print(f"Index: {i}, Data: {nodes[i].data}, Ptr: {nodes[i].ptr}")
    print()
    
def enqueue(queue,flp,sp,val):
    #check if queue is empty
    queue[flp].data = val
    if sp == -1:
        sp = flp
        nextflp = queue[flp].ptr
        queue[flp].ptr = -1
        return queue,nextflp,sp
    
    prevNode = -1
    nodePtr = sp
    while nodePtr!=-1:
        prevNode = nodePtr
        nodePtr = queue[nodePtr].ptr
    #end of the list
    
    queue[prevNode].ptr = flp
    nextflp = queue[flp].ptr
    queue[flp].ptr = -1
    return queue,nextflp,sp
    
def dequeue(queue,flp,sp):
    #check if this is the only node in queue
    if queue[sp].ptr == -1:
        queue[sp].ptr = flp
        flp = sp
        sp = -1
        return queue,flp,sp
    
    nextsp = queue[sp].ptr
    queue[sp].ptr = flp
    flp = sp
    return queue,flp,nextsp
    
        

def display():
    queue = initialise()
    flp = 0
    sp = -1
    
    choice = 2
    while choice != 0:
        print("1. Print queue nodes ")
        print("2. Enqueue ")
        print("3. Dequeue")
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            printNodes(queue,flp,sp)
        elif choice == 2:
            if flp == -1:
                print("No more space left in queue")
            else:
                val = input("Enter value to be pushed: ")
                queue,flp,sp = enqueue(queue,flp,sp,val)
                printNodes(queue,flp,sp)
        elif choice == 3:
            if sp == -1:
                print("There is nothing to dequeue \n")
            else:
                queue,flp,sp=dequeue(queue,flp,sp)
                printNodes(queue,flp,sp)
        else:
            print("we out")
            
display()