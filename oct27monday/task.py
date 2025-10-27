class Node:
    def __init__(self,v):
        self.v = v
        self.next = None

def initialise():
    stack = []
    for i in range(8):
        stack.append(Node("-"))
        stack[i].next = i-1
    stack[-1].next = -1
    stack[0].next = -1
        
    sp = 0
    flp = 0
    return stack,sp,flp
    
def output(stack):
    for i in range(len(stack)):
        print(f"[ {i} ] {stack[i].v}  {stack[i].next}")

def push(stack,sp,flp,v):
    if flp == -1:
        print("There is no space left on the stack")
    else:
        stack[flp].v = v
        stack[sp].next = flp
        flp = stack[flp].next
        
    return stack,sp,flp
        
stack,sp,flp = initialise()
output(stack)
print()
stack,sp,flp = push(stack,sp,flp,"V")
output(stack)

        
    
