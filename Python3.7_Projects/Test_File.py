# def factorial(num):
#     if (num == 0) or (num==1):
#         return num
#     return num*factorial(num-1)
#
# number = factorial(5)
#
# print(number)
#
# import math
#
# x = math.factorial(1963)
# print(x)

import datetime
day = datetime.date(1959,12,23).weekday()

if day==0:
    day='Monday'
elif day == 1:
    day='Tuesday'
elif day==2:
    day='Wednesday'
elif day==3:
    day='Thursday'
elif day==4:
    day='Friday'
elif day==5:
    day='Saturday'
elif day==6:
    day='Sunday'

print(day)