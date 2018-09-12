#Iterate through a range of numbers printing the numbers divisible by 7 and the number not divisible (cleanly)
#by 5 (Use a range of 2000 to 3000(inclusive)). Print a list (hint: data structure-> []) separated by a comma


emptyList = []
List = ['4',"4",4] #doesn't allow double quotes in lists I.e. Holds strings

for Z in range(2000,3001):
    if ( Z%7 == 0) and ( Z%5 != 0 ):
        emptyList.append(str(Z)) #Join function below works with strings, hence conversion

print (','.join(emptyList)) #join function format = 'string separator'.join(pass in string)
#separates what's in the list with commas
print(emptyList)
print(List)

#Notice we append strings to the list and not ints, hence the conversion