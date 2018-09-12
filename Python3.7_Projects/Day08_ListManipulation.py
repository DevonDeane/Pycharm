#create a list (data structure) of pets
pets = ['dog','cat','bird','rabbit','fish','neighbour']

#Manipulating Lists and Regular Strings
print(','.join(pets))
readString = (','.join(pets))

read = input("csv for countries")  #regular input is captured as a single string (even if comma separated)

print (read)  #prints a string
readList = read.split(',')  #creates a list from the string and separates values by commas
print (readList)
print('\n')

#print each list item individually
print(pets[0])
print(pets[1])
print(pets[5], '\n')

#Logical Attempt
# for i in range(len(pets)):
#     print(pets[i])
print('\n')

#OR print using a for loop
for i in pets:
    print (i)

print('\n')

#Use a conditional statement with a while loop
i_have_20_dollars = 20

while(i_have_20_dollars < 35):
    print (i_have_20_dollars)
    i_have_20_dollars +=1
print('I still need more money for xyz')

print('\n')

#Print all numbers between 1500 and 1551 which are divisible by 7 and a multiple of 5
myList = []
for i in range(1501,1551):
    if (i%7==0) and (i%5==0):
        myList.append(str(i))
        #print(i)
print (','.join(myList))

#var.split(',')
#VS
#','.join(var)
#SPLIT CREATES A LIST FROM CS RAW STRING
#JOIN CREATES A RAW STRING FROM (NATURALLY) CS LIST

print('\n')

#Write a program to guess a number between 1 and 10

# import random
# #from random import *
# target_num, guess_num = random.randint(1,10) , 0  #initialize two vars by using comma separation
# x = target_num
# while(guess_num != target_num):
#     new_num = int(input('Please enter a new num:\n'))
#     guess_num = new_num
# print('Well done')

print('\n')

#create a cool printed triangle that looks like a sideways triangle

count = 0
for num in range(7):#0 to 6 is 7 iterations
    count+=1
    print('*' * count)

#Therefore count is now 7


for reverse in range(6):#so that it now starts printing 6 stars for symmetry
    count-=1
    print('*' * count)