#Creating a working Class
class ClassName:
    pass
#Instance of the Class
instance = ClassName()
#Class Initialization
class Students:                                 #init has TWO (2) underscores
    def __init__(self, name, age, grade):       #self references the object to call the object
        self.name = name                        #this is how constructors work in Python basically..use self
        self.age = age                          #init means which parameters do you want to make mandatory
        self.grade = grade                      #when you create your object

student1 = Students("Alex", 7, "2nd Form")      #object name replaces self above
print(student1.name)
print(student1.age)                             #each parameter must be passed in via constructor structure
print(student1.grade + "\n")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age= age

    def displayStudent(self):
        #Notice integers have to be converted to strings when displaying via str()
        return("Student's name is " + self.name + " and their age is " + str(self.age) + "!") # (=

    def prompt(self):
        print("Please enter a value for i")
        value = int(input())
        return value

student3 = Student("Bob Marly", 47)
#Statement below works in IDLE
#student3.displayStudent()


#i = 1   #Input test

i = student3.prompt()
oldi= str(i)
while(i<=4):         #   5
    print(student3.displayStudent())
    #print("i = " + str(i))
    i=i+1


print("Should have printed 5 - "+oldi+" times!")


