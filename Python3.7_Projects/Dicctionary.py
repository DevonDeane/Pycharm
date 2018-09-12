dictA = {'john': 5137, 'moses': 2486}
dictA['peter'] = 1213

print(dictA)

del dictA['moses']

print(dictA)

dictA['matthew']=1214

print (dictA)
print("\nKeys:")
print (dictA.keys())
print(list(dictA.keys()))

print("\nValues:")
print (dictA.values())
print(list(dictA.values()))
print(sorted(list(dictA.values())))
# del tel['sape']
# tel['irv'] = 4127
#
# list(tel.keys())
#
# sorted(tel.keys())
print()
#USE CTRL+/ to comment multiple lines of code

dictB = {'rhino' :1234, 'bull':8758, 'prancer': 5859}
print(dictB['rhino'])
del dictB['prancer']
print(dictB.keys())
print(list(dictB.keys()))
print(sorted(list(dictB.keys())))

#Find first reoccurring letter in a sequence of characters (numeric or otherwise)

print("\nPlease enter string for checking:")
letters = input()
listA = list(letters)
print (listA)
# listASorted = sorted(listA)
# print (listASorted)

def firstRecurrence(someList):
    #setA = set(someList)
    setA = set()

    for i in someList:
        if i in setA:
            return(i)
        else:
            setA.add(i)
    return None


# dictC = {'lion':1234, letters: 2345}
# print(dictC[letters])
result = firstRecurrence(listA)

print(result)