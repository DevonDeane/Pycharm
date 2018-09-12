#Hash Table Concise Implementation
table = [ [] for table in range(10) ]

def HashFunction(key):
    val = key % 10
    return val

def HashInsert(table,key,val):
    # value = [HashFunction(key)]
    # table[value].append(key)
    table[HashFunction(key)].append(val)

def HashLookup():
    #return("a=0\nb=1\nc=2\nd=3\ne=4\nf=5\ng=6\nh=7\ni=8\nj=9\nk=10\n")
    pass

#print(HashLookup())
response = "yes"

while (response == "yes"):
    print("Insert a key into the Hash Table:")
    key = int(input())
    print("Insert a value to store for that key:")
    val = input()
    HashInsert(table, key, val)

    print(table)
    print("Anymore values? (yes or no)")
    response = input()


# reply = "yes"
# while (reply == "yes"):
#     print("Please enter key to remove item?")
#     item = int(input())
#
#     print("Please enter name of item:")
#     val = input()
#     HashInsert(table, key, val)
#
#     print(table)
#     print("Anymore values? (yes or no)")
#     response = input()