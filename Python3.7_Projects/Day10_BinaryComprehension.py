#  take 2 digits m and n (representing a row and a col respectively) as inputs
#  Generate a 2d array (list)
#  The value in the i-th row and j-th column of the array should be i*j

rows = int(input("Number of rows:"))
cols = int(input("Number of cols:"))


twoDArr = [[0 for i in range(cols)] for i in range(rows)]
print(twoDArr,"\n")
#print("\n")

for i in range(rows):
    for j in range(cols):
        twoDArr[i][j] = i*j
print(twoDArr)


#  Write a Python program that accepts a sequence of lower case lines (with a blank line to terminate)
#  Print the lines as output (all characters in upper case)

list = []
while True:
    someInput = input("Please enter lower case characters terminated by blank line 'enter'")
    if someInput:
        list.append(someInput.upper())
    else:
        break

for line in list:
    print (line)


#  Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
#  Print the numbers that are divisible by 5 in a cs sequence

# if int(str(100),2) % 4 == 0:
#     print("This is how binary works!")

def binaryDiv5():
    cs = str(input("Enter cs binary numbers:"))
    csList = cs.split(',')

    for binaryNum in csList:
        if int(binaryNum,2)%5 == 0:
            print(binaryNum)
            #OR
            print(int(str(binaryNum),2))

binaryDiv5()
print()
# a = int(str(101),2)
# print (a)

#b for Better
b = int('1000',2)
print (b)

c = int('101',10)
print (c)

#Binary Comprehension
hundred = 100
d = int(str(hundred),2)  #Notice how this line ints the entire 'line' hence need for this structure to work (for now)
print (d)

