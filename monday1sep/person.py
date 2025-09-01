list = []

list.append("hi")
list.append("how")
list.append("are")
list.append("you")

print(list)

class Person:

    def __init__(self,name,age):

        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

danny = Person("Danny", 17)

print(danny.getName())
print(danny.getAge())
