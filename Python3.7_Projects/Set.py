#Set Data Structure using direct input and lists as entries

#Union
def union(setA,setB):
    #A union B --> |
    print("Here is what A union B looks like:")
    return(setA | setB)

#Intersection
def intersect(setA, setB):
    #A intersect B --> &
    print("Here is what A intersect B looks like:")
    return(setA & setB)

print("Please enter list of elements for set A")
setA = input()
print("Please enter list of elements for set B")
setB = input()

if(setA.isnumeric() or setB.isnumeric()):
    print("You entered in some numbers, cool!")

#Placing input into two separate lists

listA = []
listB = []

for i in setA:
    listA.append(i)

#Alternatively
#listA = list(setA)

for j in setB:
    listB.append(j)



#Placing input into two separate sets

#Placing an list/array into a set
#Can also pass into set function setA (direct input) instead
A = set(listA)

#Placing direct input into a set
#Can also pass into set function listB (list/array) instead
B = set(setB)

#Produce Union Set
setC = union(A,B)
print(sorted(setC))

#Produce Intersection Set
setD = intersect(A,B)
print(sorted(setD))