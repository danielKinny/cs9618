global HashTable
global Spare

class NewRecord:
    def __init__(self):
        self.key = -1 #integer
        self.Item1 = -1 #integer
        self.Item2 = -1 #integer

HashTable = []
Spare = []

def Initialise():
    for i in range(200):
        if i < 100:
            Spare.append(NewRecord())
        HashTable.append(NewRecord())

def CalculateHash(key):
    return key%200

def InsertIntoHash(NewRecord):
    idx = CalculateHash(NewRecord.key)
    if HashTable[idx].key == -1:
        HashTable[idx].key = NewRecord.key
        HashTable[idx].Item1 = NewRecord.Item1
        HashTable[idx].Item2 = NewRecord.Item2
    else:
        ptr = 0
        while Spare[ptr].key != -1:
            ptr+=1
        Spare[ptr].key = NewRecord.key
        Spare[ptr].Item1 = NewRecord.Item1
        Spare[ptr].Item2 = NewRecord.Item2

def CreateHashTable():
    with open("HashData.txt", "r") as f:
        for rec in f:
            row = rec.strip().split(",")
            record = NewRecord()
            record.key = int(row[0])
            record.Item1 = int(row[1])
            record.Item2 = int(row[2])
            InsertIntoHash(record)

def PrintSpare():
    for record in Spare:
        if record.key != -1:
            print(record.key)

Initialise()
CreateHashTable()
PrintSpare()
    
    


        

        
