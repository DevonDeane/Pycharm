#Create a class with 2 functions/methods in it
#1) Get string (accessor)
#2) Print string

# class Printer(object):
#     def __init__(self):
#         self.str = ''
#         self.num = 0
#     def getString(self):
#         self.str = input("Please enter a valid string to be capitalized:\n")
#         #string stored in object as str
#     def printString(self):
#         print(self.str.upper())
#         #print the selfsame calling object's string based on the contructor definition which says it has one (a string)
#         #upper function works such that "string variable".upper()
# #Notice therefore that 's' (or "str") basically represents an arbitrary object derived from the Printer class
# printObj = Printer()
#
# printObj.getString()
# printObj.printString()


class Number(object):
    def __init__(self):
        self.someStr = ''
        self.someInt = 0

    def getter(self):
        return self.someInt

    def setter(self,x):
        self.someInt = x

myNum = Number()
print("Enter a number:")
num = int(input())
myNum.setter(num)
print(myNum.getter()+1) #integer form preserved

