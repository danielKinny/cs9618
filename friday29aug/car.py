
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

    def SetCoolness(self, cool):
        self.__IsCool = cool

    def SetHighestSpeed(self, speed):
        self.__HighestSpeed = speed

    def GetCarType(self):
        return (self.__CarType)
    
    def Coolness(self):
        return (self.__IsCool)
    
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
        print("The vehicle registration is: "+self.__Registration)
        print("The date of registration is: "+self.__DateOfRegistration)
        print("The engine size of the vehicle is: ",self.__EngineSize)
        print("The purchase price of the vehicle is: ",self.__PurchasePrice)

#structure is going to be vehicle id, engine size, purchase price, registration numb, and the date of.
corolla = Car("ABC123", 2500)
yaris = Car("ABC123", 3000)
rav4 = Car("ABC123", 3000)
landcruiser = Car("ABC123", 4000)
prado = Car("ABC123", 4000)

cars = [corolla,yaris,rav4,landcruiser,prado]

def highestPurchasePrice():
    highest = cars[0].GetPurchasePrice()
    for i in range(0,len(cars)):
        if cars[i].GetPurchasePrice() > highest:
            highest = i
    return cars[i]

def largestEngineSize():
    highest = cars[0].GetEngineSize()
    for i in range(0,len(cars)):
        if cars[i].GetEngineSize() > highest:
            highest = i
    return cars[i]

def averagePrice():
    total = 0
    for car in cars:
        total += car.GetPurchasePrice()
    return total / len(cars)

def findCar(reg):

    for car in cars:

        if car.GetRegistration() == reg:
            return car
    return None

for car in cars:
    pp = int(input("Enter purchase price of: "))
    reg = input("Enter registration of: ")
    doreg = input("Enter date of registration of: ")
    car.SetPurchasePrice(pp)
    car.SetRegistration(reg)
    car.SetDateOfRegistration(doreg)


