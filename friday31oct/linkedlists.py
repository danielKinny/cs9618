class Node:
    def __init__(self, data):
        self.data = data
        self.ptr = None

def initialiseNodes():
    nodes = []
    for i in range(8):
        nodes.append(Node("-"))
        nodes[i].ptr = i+1
    
    nodes[-1].ptr = -1
    return nodes
    
def printNodes(nodes,flp,sp):
    print()
    print(f"Current FLP is: {flp} and SP is {sp}")
    for i in range(len(nodes)):
        print(f"Index: {i}, Data: {nodes[i].data}, Ptr: {nodes[i].ptr}")

def insertNode(nodes,flp,sp,val):
    #sp represents the logical start of the list
    #flp represents the index to the free point in the arr
    #first we check if this is the first node in the list
    #we do this by checking

    #set the data no matter what
    nodes[flp].data = val
    nodePtr = sp #pointer that we're using to traverse will logically start at sp
    nextNode = nodes[sp].ptr #next node will be the ptr of sp
    
    if sp == -1: #this will trigger if this is the first node being inserted
        sp = flp
        flp = nodes[flp].ptr
        nodes[sp].ptr = -1
        return flp,sp,nodes
    
    if val < nodes[nodePtr].data: #this will trigger if the new node is going to be the smallest in the list
        sp = flp
        flp = nodes[flp].ptr
        nodes[sp].ptr = nodePtr
        return flp,sp,nodes
    
    while  nextNode != -1 and nodes[nextNode].data < val: #this is used to traverse the list
        nodePtr = nextNode
        nextNode = nodes[nextNode].ptr
    if nextNode == -1:
        #end of list
        nodes[nodePtr].ptr = flp #final node ptr now points to inserted node
        nextflp = nodes[flp].ptr #temp var for flp
        nodes[flp].ptr = -1 #setting ptr of new node to -1
    else:
        #insertion logic
        nextflp = nodes[flp].ptr #temp var for flp
        nodes[nodePtr].ptr = flp #current node ptr now points to inserted node
        nodes[flp].ptr = nextNode #new node ptr node points to next node
        
    return(nextflp,sp,nodes)

def deleteNode(nodes,flp,sp,tar):
    nodePtr = sp
    
    if sp == -1:
        print("There are no nodes to be deleted")
        return nodes,flp,sp
    
    if nodes[nodePtr].data == tar:
        nextsp = nodes[nodePtr].ptr
        nodes[nodePtr].ptr = flp
        flp = nodePtr
        return nodes,flp,nextsp
    
    while nodes[nodePtr].data != tar and nodePtr != -1:
        prevNode = nodePtr
        nodePtr = nodes[nodePtr].ptr
    if nodePtr == -1:
        print("Node to be deleted not found")
        return nodes,flp,sp
    else:
        nextNode = nodes[nodePtr].ptr
        nodes[nodePtr].ptr = flp
        flp = nodePtr
        nodes[prevNode].ptr = nextNode
    
    return nodes,flp,sp
        
    
def displayMenu():
    nodes = initialiseNodes() #initialising the nodes within the main subprog to avoid closure confusions
    flp,sp=0,-1 #first flp is 0, since empty list, subsequuently sp is also gunna be -1
    val = -1 #dummy val to enter while loop and force repeat menu display
    while val != 0:
        val = -1
        print("1. Print all Nodes ")
        print("2. Insert a Node ")
        print("3. Delete a Node ")
        while val > 3 or val < 0:
            val = int(input('Enter choice: '))

        if val == 1:
            printNodes(nodes,flp,sp)

        elif val == 2:
            if flp == -1: #checks if there is any more free nodes
                print("No more space left in list")
            else:
                valid = False
                while not valid:
                    data = input('Enter Input (A-Z): ')
                    valid = ord(data) >= 65 and ord(data) <= 90 #checks whether input is caps alphabets
                flp,sp,nodes = insertNode(nodes,flp,sp,data)
                printNodes(nodes,flp,sp)
        elif val == 3:
            valid = False
            while not valid:
                data = input('Enter Input (A-Z): ')
                valid = ord(data) >= 65 and ord(data) <= 90
            nodes,flp,sp = deleteNode(nodes,flp,sp,data)
            printNodes(nodes,flp,sp)
        else:
            print("WE OUTTA HERE")

        print()
                    
displayMenu()


        
        
    
    
