import datetime
import random

class LibraryItem:
    def __init__(self, title, author, itemID):
        self.__title = title
        self.__author = author
        self.__itemID = itemID
        self.__onLoan = False
        self.__dueDate = datetime.date.today()

    def setTitle(self, t):
        self.__title = t

    def setAuthor(self, a):
        self.__author = a

    def setItemID(self, i):
        self.__itemID = i

    def getLoaned(self):
        return self.__onLoan
    
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
        if self.getLoaned():
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
        
    def printDetails(self):
        print("--------------------------------------------")
        print("The name of the book is: " + self.getTitle())
        print("The book is authored by: "+ self.getAuthor())
        print("The book ID is: " + self.getItemID())
        if self.getLoaned():
            print("This book is on loan till: " + str(self.__dueDate) )
        else:
            print("This book is not on loan")
        if self.getRequested():
            print("This book is already requested")
            print("Repeated count: ",self.__repeatedly)
        else:
            print("This book has not been requested")
        

class CD(LibraryItem):

    def __init__(self, title,author,itemID):
        LibraryItem.__init__(self,title, author, itemID)
        self.__genre = "pop"

    def printDetails(self):
        print("-------------------------------------------")
        print("The name of the CD is: " + self.getTitle())
        print("The CD is authored by: "+ self.getAuthor())
        print("The CD ID is: " + self.getItemID())
        if self.getLoaned():
            print("This CD is on loan till: " + str(self.__dueDate) )
        else:
            print("This CD is not on loan")
        print("this genre of this CD is : "+self.__genre)

    def setGenre(self, genre):
        self.__genre = genre

    def getGenre(self):
        return self.__genre
    

#actual code
    
library = []

for i in range(5):
    print("-----------------------")
    t = input('Enter book title: ')
    a = input('Enter author: ')
    i = input('Enter book ID: ')
    library.append(Book(t,a,i))


for i in range(3):
    print("--------------------")
    t = input('Enter CD title: ')
    a = input('Enter author: ')
    i = input('Enter CD ID: ')
    library.append(CD(t,a,i))

for item in library:
    item.printDetails()




    
