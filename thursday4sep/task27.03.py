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
    
class Borrower:

    def __init__(self, name, email, bID, itemLoaned):
        self.__borrowerName = name
        self.__email = email
        self.__bID = bID
        self.__itemLoaned = itemLoaned

    def getBorrowerName(self):
        return self.__borrowerName
    def getEmail(self):
        return self.__email
    def getBorrowerID(self):
        return self.__bID
    def getItemsLoaned(self):
        return self.__itemLoaned
    def updateItemsOnLoan(self, n):
        self.__itemLoaned += n

    def printDetails(self):
        print("The name of this borrower is: "+ self.getBorrowerName())
        print("The email of the borrower is: "+ self.getEmail())
        print('The borrowed ID is: ',self.getBorrowerID())
        print("Number of items on loan are: ",self.getItemsLoaned())

borrowers=[]
library = []

#this initialises a list of borrowers
for i in range(1):
    name = input('Enter borrower name: ')
    email = input('Enter borrower email: ')
    bID = int(input("Enter your borrowed ID: "))
    itemsOnLoan = int(input("Enter items on loan: "))

    borrowers.append(Borrower(name, email, bID, itemsOnLoan) )


#this initialises 5 books and 5 CDs
for i in range(1):
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


#code that allows someone to borrow a book

for item in library:
    item.printDetails()

selection = input("Enter the ID of the item you want to borrow: ")
for item in library:
    if item.getItemID() == selection:
        borrowers[0].updateItemsOnLoan(1)
        item.borrowing()
    else:
        print("item not found")

borrowers[0].printDetails()

for item in library:
    item.printDetails()