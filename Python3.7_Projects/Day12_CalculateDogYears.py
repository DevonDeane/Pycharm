#  Create a program which calculates age in dog years
#  Note:
#  Dog year 0-2 = 10.5 human years each year
#  After 2 each dog year = 4 human years


while True:
    normalYrs = input("How many human years has the dog been alive?\n")
    try:
       normalYrs = int(normalYrs)  # if you can't convert it to an int then it was ~not an int to begin with.Hence check
       break
    except ValueError:
       print("That's not an int!")


if normalYrs <= 0:
    print("Okay then, bye!")
    exit()
elif normalYrs <= 2:
    dogYrs = normalYrs * 10.5
elif normalYrs > 2:
    remainder = normalYrs-2
    dogYrs = 21.0 + (remainder*4)
print('The dog is', dogYrs, 'in dog years!')


#  Write a program to decipher vowels from consonants

letter = input("Please enter an alphabetical letter:")
while True:
    try:
       letter = int(letter)  # if you can't convert it to an int then it was ~not an int to begin with.Hence check
       letter = input("Kindly enter a non-numeric single alphabetical letter:")
       continue
    except:
       pass

    if len(letter) == 1 and type(letter)==str:
        break
    else:
        letter = input("Kindly enter a single alphabetical letter:")


letter = letter.lower()

if letter in ('a','e','i','o','u'):
    print('{} is in fact a vowel!'.format(letter))
elif letter == 'y':
    print('a,e,i,o,u and sometimes {} are vowels indeed, so vowel!'.format(letter))
else:
    print('{} seems to be a consonant!'.format(letter))

