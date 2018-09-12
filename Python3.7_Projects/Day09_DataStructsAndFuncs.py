# reverse an inputted string

x = input("Please enter a string to be processed, reversed and returned!\n")
# y = '+'.join(x)
# print (y)
b = ''.join(reversed(x))
print('I am reversed:\t' +b+ '\n')
print(reversed(x))
# y = x[::-1]  # [] signify an index position (string like an array of characters still but subtly)
# z = x[::-2]  # :: signifies going to the beginning and the end of the string to and in stepwise fashion print in 1s from
# print(x[0])  # the back. That is if you say x[::-1] x[::1] should print word naturally x[::2] should print letters w/skip
# Examples
print(x[::1])
print(x[::2])
print(x[::-1])
print(x[::-2])
# well understood string manipulation trick
print(x[::-1])
print('\n')

# count even or odd from a series of numbers

def evenOddCount(lower_num,higher_num):
    total_even , total_odd = 0,0
    for i in range (lower_num,higher_num+1):
        if(i%2==0):
            total_even += 1
        else:
            total_odd += 1
    print(total_even,'\n')  # includes an automatic space unlike '+'
    # print(total_odd+'\n')  # N.B. cannot use + for string AND int
    print(total_odd,'\n')

lower_limit = 1
upper_limit = 2000
evenOddCount(lower_limit,upper_limit)

def evenOddCountList(listX):
    total_even , total_odd = 0,0
    for i in listX:
        if(i%2==0):
            total_even += 1
        else:
            total_odd += 1
    print(total_even,'\n') # includes an automatic space unlike '+'
    # print(total_odd+'\n')  # N.B. cannot use + for string AND int
    print(total_odd,'\n')

x = [1,2,3,4,5,6,7,8,9]
evenOddCountList(x)


def evenOddCountListButReturn(listX):
    total_even , total_odd = 0,0
    for i in listX:
        if(i%2==0):
            total_even += 1
        else:
            total_odd += 1
    return total_even, total_odd  # Amen, amen, amen...python returns multiple variables from functions Hallelujah!

x = [0,1,2,3,4,5,6,7,8,9,10]# 0 treated as even number (may be mathematically natural as well[perhaps as a tie breaker])
print(evenOddCountListButReturn(x))
a = (evenOddCountListButReturn(x))  # when multiple variables are returned they come as an unmutatable tuple
# print (a)
b = list(a)
print (b)
yes = a[0]  # can capture each returned value easily and safely (don't even need to convert to a list, wow)
print (yes)

# given the below list print out the item and its type
dataTypes = [1452,11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12] , {"class":'V', "section":'A'}]
# Note: A value of type 'complex' stems from initializing/declaring an alphanumeric value (mixed)
for some_i in dataTypes:
    print('Following data value', some_i, 'is of type', type(some_i))


# write a program to print all numbers (0 to 7) except 3 and 6

for i in range(8):
    if (i!=3 and i!=6):
        print (i)

print('\n')

# program a fibonacci sequence between 0 and 50. (I.e. the next number is the sum of the two numbers that preceeded it

# rangeOfNums = [i for i in range(50)]
# for i in range(51):
#
#         print(i)

# Fibonacci revealed/made simple
a = 0
b = 1
# a,b=0,1
# since we have to start with a 0 and a 1
print('Fibonacci:')
while b < 50:
    print(b)
    a,b = b, a+b  # 0 and 1 is 1 // 1 and 1 is 2 // 1 and 2 is 3 // 2 and 3 is 5 // 3 and 5 is 8 etc.
    # BOOM! In mind, I wanted a c, there is my c (c=a+b)

print('\n')
# Write a program iterating 0 to 50. If num is multiple of 3 print DIV3 instead of num.
# If num is multiple of 5 print DIV5. If num is multiple of of both print DIVKING

for i in range(51):
    if (i%3 == 0) and (i%5 == 0):
        print ('DIVKING')
    elif (i%3 == 0):  # benefit of elif instead of a nested if is that if the condition is met..
        print ('DIV3')  # subsequent elifs and elses are ignored! Very handy ^_^
    elif (i%5 == 0):
        print('DIV5')
    else:
        print(i)
