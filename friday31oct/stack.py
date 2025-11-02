"""

stacks are lifo,
so it gets pushed to the top
and popped from the top

initialising:
> 8 nodes
> last node set to -1

notable change:
> print nodes print from 7 to 0 to mimic an actual stack

push:
> check if there are any existing nodes (if not set sp to first node > reset flp > make first node point to null)
> if there are existing nodes, traverse to the end of the stack using prevNode as a temp var
> set prevNode ptr to flp > set flp to next flp > set top node ptr to null

pop:
> check if first node is only node ( set sp to -1 > set flp to that node's idx > set that node's ptr to flp)
> traverse nodes to the end of the list if otherwise
> set prevNode ptr to null > set nodePtr to flp > set flp to nodePtr

"""








class Node:
    def __init__(self,v):
        self.data = v
        self.ptr = None
    
def initialise():
    stack = []
    for i in range(8):
        stack.append(Node("-"))
        stack[i].ptr = i+1
    stack[-1].ptr = -1
    return stack
    
def printNodes(nodes,flp,sp):
    print()
    print(f"Current FLP is: {flp} and SP is {sp}")
    for i in range(len(nodes)-1,-1,-1):
        print(f"Index: {i}, Data: {nodes[i].data}, Ptr: {nodes[i].ptr}")
    print()
        
def push(stack,flp,sp,val):
    #first check if it is the first element on the stack
    stack[flp].data = val
    if sp == -1:
        sp = flp #new start pointer is the first element
        flp = stack[flp].ptr #new flp is the ptr of the prev flp
        stack[sp].ptr = -1 #since last node on stack, null ptr
        return stack,flp,sp
    #if it isnt, find the last node in the stack
    nodePtr = sp
    while nodePtr != -1:
        prevNode = nodePtr
        nodePtr = stack[nodePtr].ptr #traversing stack
    #now they have found the end of the stack
    
    stack[prevNode].ptr = flp
    nextflp = stack[flp].ptr
    stack[flp].ptr = -1
    flp = nextflp
    
    return stack,flp,sp
    
def pop(stack,flp,sp):
    #this will pop off the last node in the stack
        
    #check if this is the first node
    if stack[sp].ptr == -1:
        stack[nodePtr].ptr = flp
        flp = nodePtr
        sp = -1
        return stack,flp,sp
        
    #now traverse the list till last node is found, keeping the previous node as a temp
    nodePtr = sp
    while stack[nodePtr].ptr != -1:
        prevNode = nodePtr
        nodePtr = stack[nodePtr].ptr
    #now nodePtr points to the last node on the list
    
    stack[nodePtr].ptr = flp
    flp = nodePtr
    stack[prevNode].ptr = -1
    return stack,flp,sp
    
def display():
    stack = initialise()
    flp = 0
    sp = -1
    
    choice = 2
    while choice != 0:
        print("1. Print stack nodes ")
        print("2. Push value on top ")
        print("3. Pop value on top")
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            printNodes(stack,flp,sp)
        elif choice == 2:
            if flp == -1:
                print("No more space left in stack")
            else:
                val = input("Enter value to be pushed: ")
                stack,flp,sp = push(stack,flp,sp,val)
                printNodes(stack,flp,sp)
        elif choice == 3:
            if sp == -1:
                print("There is nothing to pop \n")
            else:
                stack,flp,sp=pop(stack,flp,sp)
                printNodes(stack,flp,sp)
        else:
            print("we out")
        
display()