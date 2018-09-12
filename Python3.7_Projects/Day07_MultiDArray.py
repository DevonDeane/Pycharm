#  take 2 digits a and b as input and output a multidimensional array

input_for_system = input("Please enter some cs integer input:")#comma separated
# input_for_system contains a raw string E.g '3,4'
dimension = [
    int(x) #say 5 #maybe not passing anything in but idk yet #AH just used to convert each iterated value to an integer
    for x in input_for_system.split(',') #0 to 5 separate purely by commas (works because input_for_system is a workable string)
    #for each value in "input_for_system" separate it by a comma and store it in a variable (list) called dimension
]
#dimension contains a list of pure integers separated by commas E.g. [3,4]
rowindex = dimension[0]  #remember lists take strings hence conversion above #AH see below
colindex = dimension[1]  #these are like array positions
#rowindex contains value at the 0th position of the dimension list and so forth for colindex E.g. rowindex = 3 colin = 4
list = [
    [
        0   #(think of it as int y = 0...but idk) #AH place a zero in each position in list perhaps
        for cols in range (colindex)
    ]#AH what comes before the for in lists is what you will append to that list
    for rows in range(rowindex)
]

for row in range(rowindex):#for 0 to rowindex-1...which is still rowindex iterations
    for col in range (colindex):
        list[row][col] = row*col
print(list)

#Very interesting
#Now rewrite on your own

#accept two integer values and create a 2 dimensional array where first int serves as row num and second as col num

gridDimensions = input("Please enter two comma separated numbers for 2d array size:row_no,column_no")#expect = '4,5'
#note this (gridDimensions) is one string
#use gridDimensions.split(',')
grid = [int(x) for x in gridDimensions.split(',')] #place int(str) found in position x (starts at 0 and iterates up)
#grid = [3,4]
rows = grid[0]  #expect = 3
cols = grid[1]  #expect = 4

twoDimArr = [[0 for col in range(cols)]for row in range(rows)]
#store zeroes for each col in range of cols (4)
#result is a list (Alist) with int 0s in each position
#next
#store lists (Alist) for each row in range of rows (3)
#result is a list (Anotherlist) of with lists (Alists) in each position

#Populate 2D Array
for row in range(rows):  #0 to 3
    for col in range(cols):  #0 to 4
        twoDimArr[row][col] = row*col  #current position =

print(twoDimArr)



#Thoroughly impressive growth
#Now improve it

#Populate 2D Array
def populateGrid(row_num,col_num,twoDimensionalArray):
    for row in range(row_num):  #0 to 3
        for col in range(col_num):  #0 to 4
            twoDimensionalArray[row][col] = row*col  #current position =
    return twoDimensionalArray

num1 = 3
num2 = 4

twoDimArray = [[0 for col in range(num2)]for row in range(num1)]
print(twoDimArray)
print(populateGrid(num1,num2,twoDimArray))










