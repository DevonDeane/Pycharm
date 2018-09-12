#compute the factorial of an inputted number. Return the result on a single line in csv format
#import math

def factorial(num):
    if (num==0 or num==1):
        return 1
    return num*factorial(num-1)

print("Please enter a number for factorial output:")
numb = int(input())
#OR
#numb = int(input("Please enter a number for factorial output:"))

print(factorial(numb))
#OR
import math
print(math.factorial(numb))

print('\n')

class SomeClass(object):
    def __init__(self,x):
        self.str = x
        self.num = 0
        self.float = 0.0

    def getter(self):
        return self.str
        #...

    def setter(self,x):
        self.str = x

obj = SomeClass('z')
print(obj.getter())
obj.setter('a')
print(obj.getter())