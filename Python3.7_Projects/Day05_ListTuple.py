#Convert a list into a tuple
#cs = comma separated

values = input('Give me some cs numbers:')
print (values)
#list = [] #Line not needed, split creates a list automatically
list = values.split(',') #separates individual values (by comma) and stores them separately in a list data structure
tuple = tuple(list) #convert list to tuple and store as a tuple named tuple
print(list, tuple)

print(list, tuple)

tupleA = (23, 'MJ')
listA = [24, ] #note just like in django, if list/tuple expected then a comma even after single value entry
#tupleA.append(23) #tuples are not modifiable like lists, hence above code instead
print (tupleA)
print (listA)

#tupleB[0] = 4 #also impossible since tuples are immutable objects
#print (tupleB)