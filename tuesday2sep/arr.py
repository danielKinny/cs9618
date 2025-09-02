import random

class Car:

    def __init__(self, n, e):
        self.__VehicleID = n
        self.__Registration = ""
        self.__DateOfRegistration = ""
        self.__EngineSize = e
        self.__PurchasePrice = 0.00

    def SetPurchasePrice(self, p):
        self.__PurchasePrice = p

    def SetRegistration(self, r):
        self.__Registration = r
    
    def SetDateOfRegistration(self, r):
        self.__DateOfRegistration = r

    def SetCarType(self, ct):
        self.__CarType = ct

    def SetHighestSpeed(self, speed):
        self.__HighestSpeed = speed

    def GetCarType(self):
        return (self.__CarType)
    
    def GetHighestSpeed(self):
        return (self.__HighestSpeed)
    
    def GetVehicleID(self):
        return (self.__VehicleID)
    
    def GetRegistration(self):
        return (self.__Registration)
    
    def GetDateOfRegistration(self):
        return (self.__DateOfRegistration)
    
    def GetEngineSize(self):
        return (self.__EngineSize)
    
    def GetPurchasePrice(self):
        return (self.__PurchasePrice)
    
    def PrintDetails(self):
        print("---------")
        print("The vehicle ID is : ",self.__VehicleID)
        print("The vehicle registration is: ",self.__Registration)
        print("The date of registration is: "+self.__DateOfRegistration)
        print("The engine size of the vehicle is: ",self.__EngineSize)
        print("The purchase price of the vehicle is: ",self.__PurchasePrice)

#initialising the array with random vehicle ID and engine sizes

arr = [Car(str(random.randint(1000,9999)),random.randint(1000,3000)) for i in range(5)]
for car in arr:
    car.SetPurchasePrice(random.randint(10000,150000))
#all cars are given in the array with random purchase prices


#use bubble sort to sort the array

noSwap = True
while noSwap:
    noSwap = False
    for i in range(len(arr)-1):
        if arr[i].GetPurchasePrice() > arr[i+1].GetPurchasePrice():
            arr[i], arr[i+1] = arr[i+1], arr[i]
            noSwap = True

for car in arr:

    print(car.PrintDetails())
