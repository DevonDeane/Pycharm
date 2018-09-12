#create a cool calculator

c = 60
h = 40

#apply this formula Q = square root of [(2*c*d)/h]
#find d

import math
x = [] #emptyList
y = [i
    for i in (input('give me a number:')).split(',') #input has split function it can use    #'4,5,6'.split(',') = '4','5','6'
]

for d in y: # 0th position in list y maybe?
    x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))  #round it likely still leaves a rounded float
print(','.join(x))

#join method is for strings as learnt before, hence conversion 2 lines above

z = []
n = [str(i) for i in range(1,10)]
z.append(str(1))
z.append(str(2))
print (n)#((',').join(str(n)))
print (','.join(n))
print(z)
print(','.join(z))