ArrayNodes = [ [0 for i in range(3)] for j in range(20)]

RootPointer = -1
FreeNode = 0

def AddNode(arr, rp, fnp):
    val = int(input('Enter value of node to be added: '))
    if rp == -1:
        arr[fnp][1] = val
        arr[fnp][0] = -1
        arr[fnp][2] = -1
        rp = fnp
        fnp += 1
        return arr, rp, fnp
    else:
        nodePtr = rp
        while True:
            if arr[nodePtr][1] > val:
                if arr[nodePtr][0] == -1:
                    arr[fnp][1] = val
                    arr[fnp][0] = -1
                    arr[fnp][2] = -1
                    arr[nodePtr][0] = fnp
                    fnp += 1
                    return arr, rp, fnp
                else:
                    nodePtr = arr[nodePtr][0]
            else:
                if arr[nodePtr][2] == -1:
                    arr[fnp][1] = val
                    arr[fnp][0] = -1
                    arr[fnp][2] = -1
                    arr[nodePtr][2] = fnp
                    fnp += 1
                    return arr, rp, fnp
                else:
                    nodePtr = arr[nodePtr][2]

def PrintAll(ArrayNodes):
    for node in ArrayNodes:
        print(f" {node[0]} \t {node[1]} \t {node[2]} ")
        print()

def InOrder(arr, rp):
    if arr[rp][0] != -1:
        InOrder(arr, arr[rp][0])
    print(arr[rp][1])
    if arr[rp][2] != -1:
        InOrder(arr, arr[rp][2])
    print()

for i in range(10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)
PrintAll(ArrayNodes)
InOrder(ArrayNodes, RootPointer) 