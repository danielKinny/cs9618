class Car:

    def __init__(self, n, e, cool, ct, hs):
        self.__VehicleID = n
        self.__Registration = ""
        self.__DateOfRegistration = None
        self.__EngineSize = e
        self.__PurchasePrice = 0.00
        self.__CarType = ct
        self.__IsCool = cool
        self.__HighestSpeed = hs

    def SetPurchasePrice(self, p):
        self.__PurchasePrice(p)
    
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
    
toyota = Car("ABC123", 2500, False, "sedann", 120)
ferrari = Car("ABC123", 3000, True, "sport", 240)
lambo = Car("ABC123", 2000, True, "sport", 320)
nissan = Car("ABC123", 2000, False, "sedan", 150)
pajero = Car("ABC123", 4000, True, "suv", 240)



