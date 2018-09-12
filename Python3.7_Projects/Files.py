wfile = open('sample.txt','w')

wfile.write('Writing some stuff in new text file\n')
wfile.write('Haha :P\n')
wfile.close()

rfile = open('sample.txt','r')

stringVar = rfile.read()  #store info in sample.txt
print(stringVar)
rfile.close()