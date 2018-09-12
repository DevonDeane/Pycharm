#  Accept a string returning the number of alphabetical characters and the number of digits

someStr = input("Please enter your 'random' string:")
alphas , digits = 0,0

for char in someStr:
    if char.isalpha():
        alphas+=1
    elif char.isdigit():
        digits+=1
    else:
        pass

print(alphas,"alphabetical characters were read!")
print(digits, "digits were read!")


#  Check the validity of a password
#  Rules:
#  At least 1 lowercase alphabetical character and at least 1 uppercase alphabetical character
#  At least 1 integer number
#  At least 1 special character E.g. $,#,@
#  Minimum length 6 characters, maximum length 16 characters

import re  # regular expressions (matching operations)

p = input("Please enter a password:")
weak = True
# Proper inline comment syntax below
while True:
    if len(p) < 6 or len(p) > 16:
        break
    if not re.search('[a-z]', p):  # if search for a to z in p is true (not means not true/false)
        break
    if not re.search('[A-Z]', p):
        break
    if not re.search('[0-9]', p):
        break
    if not re.search('[$#@]', p):
        break
    if re.search('\s', p):
        break
    else:
        weak = False
        break


if weak:
    print("The password you entered is too weak or does not meet requirements outlined!")

if not weak:
    print("Password successfully meets stipulated criteria!")


# Find even numbers BETWEEN 100 and 400 (inclusive)
# Print output in csv format

evenDigits = []

# for i in range(100,401):
#     if i % 2 == 0:
#         evenDigits.append(str(i))
# OR

for i in range(100,401):
    s= str(i)
    if int(s[0]) % 2==0 and int(s[1]) % 2==0 and int(s[2]) % 2 ==0:
        evenDigits.append(s)

csv = (','.join(evenDigits))
print(csv)
