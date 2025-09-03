import datetime

class LibraryItem:
    def __init__(self, title, author, itemID):
        self.__title = title
        self.__author = author
        self.__itemID = itemID
        self.__onLoan = False
        self.__dueDate = datetime.date.today()

    def getTitle(self):
        return self.__title
    
    def getAuthor(self):
        return self.__author
    
    def getItemID(self):
        return self.__itemID
    
    def borrowing(self):
        self.__onLoan = True
        self.__dueDate = self.__dueDate + datetime.timedelta(weeks=3)

    def printDetails(self):
        print("The name of the item is: " + self.getTitle())
        print("The item is authored by: "+ self.getAuthor())
        print("The item ID is: " + self.getItemID())
        if self.__onLoan:
            print("This item is on loan till: " + str(self.__dueDate) )
        else:
            print("This item is not on loan")

class Book(LibraryItem):

    def __init__(self, title,author,itemID):
        LibraryItem.__init__(self,title, author, itemID)
        self.__isRequested = False
        self.__repeatedly = 0

    def getRequested(self):
        return self.__isRequested
    
    def getRepeatedly(self):
        return self.__repeatedly
    
    def setRequested(self):
        self.__isRequested = True



book1 = Book("1984", "george orwell", "123A")
book1.borrowing()
book1.printDetails()

    
