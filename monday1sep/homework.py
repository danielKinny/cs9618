import random

class Car:

    def __init__(self, n, e):
        self.__VehicleID = n
        self.__Registration = ""
        self.__DateOfRegistration = None
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


carjobs1 = [Car(str(random.randint(1000,9999)),random.randint(1000,3000)) for i in range(5)]
carjobs2 = []

for i in range(2):
    e = int(input("Enter engine size: "))
    v = input("Enter vehicle ID: ")
    carjobs2.append(Car(v,e))
    
for car in carjobs1:
    pp = int(input("Enter purchase price of the car: "))
    reg = int(input("Enter registration number: "))
    regdate = input("Enter date of registration: ")
    
    car.SetPurchasePrice(pp)
    car.SetRegistration(reg)
    car.SetDateOfRegistration(regdate)
    
for car in carjobs1:
    car.PrintDetails()
    
vehicleID = input("Enter vehicle ID to search for: ")
flag = False

for car in carjobs2:
    if car.GetVehicleID() == vehicleID:
        print("Match found")
        flag = True
        break
    
if not flag:
    print("Car with that vehicle ID not found")
    
    
