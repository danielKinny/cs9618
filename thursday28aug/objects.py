class Car:

    def __init__(self, n, e):
        self.__VehicleID = n
        self.__Registration = ""
        self.__DateOfRegistration = None
        self.__EngineSize = e
        self.__PurchasePrice = 0.00

    def SetPurchasePrice(self, p):
        self.__PurchasePrice(p)
    
    def SetRegistration(self, r):
        self.__Registration = r
    
    def SetDateOfRegistration(self, r):
        self.__DateOfRegistration = r

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
    

        

