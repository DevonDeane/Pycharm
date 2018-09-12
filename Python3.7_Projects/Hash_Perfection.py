def insert(nextInput):

    while(nextInput!="0"):

        strInp = nextInput
        asciiSum=0
        for char in strInp:
            charVal = ord(char) #use chr() to reconvert (although pretty much unnecessary)
            #print(charVal)
            asciiSum = asciiSum + charVal

        print(asciiSum)

        hashVal = asciiSum%10
        L[hashVal] = strInp
        print (L)

        print("Please enter a new value to store into the hash table (terminated by 'ENTER')")
        nextInput = input()
    #end
def retrieve(value):
    print("Not done")


#Build list of size 10
L = [None] * 10
#Print empty List
print (L)

print("Please enter a new value to store into the hash table (terminated by '0')")
stringInput = input()
insert(stringInput)



#Next is retrieval



