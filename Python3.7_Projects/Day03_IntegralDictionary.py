#given int n, create a dictionary with the function that creates the square of n (and its children)
#int is a whole number assigned to a function

print("Please enter an integer value for...squaring it and it's predecessors")
num = int(input())

dictA= dict()       #think of this as a much cooler array (values accessed by key and not position)
                    #by extension think of lists as arrays

for x in range(1, num+1): #(for each x starting at 1 until (num+1-1)[since non-inclusive])
    dictA[x] = x*x

#so dictA[0] means pass in key 0 and not position 0 (but key can still be position)

#so basically dictionaries have keys which are like settable positions

print(dictA)
print(dictA[2])