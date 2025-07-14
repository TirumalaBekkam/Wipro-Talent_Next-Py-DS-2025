# Activity-1

# PROGRAM  to print reverse of string

s=input("enter:")
print(s[::-1])

# Another way

l1=[]
s=input("enter:")
for i in range(len(s)-1,-1,-1):
    l1.append(s[i])
print(''.join(l1))

#Activity-2

# PROGRAM to replace 'z' in string with vowels 

s=input("enter:")
vowel='aeiou'
found=False
result=''
for char in s.lower():
    if char in vowel:
        result+='z'
        found=True
    else:
        result+=char
if found:
    print(result)
else:
    print("NO vowels present")

# Activity-3

# string concatenation

str1=input("enter:")
str2=input("enter:")
result=str1+str2
print(result)

#  Activity-4

# count the characters in the string

from collections import Counter
s=input("enter:")
count=Counter(s)
print(dict(count))
for i,j in count.items():
    print(f'{i}-{j}')

# Activity-5

#PROGRAM to concatenate two strings after reverse of second string

str1=input("enter:")
str2=input("enter:")
res=str2[::-1]
print(str1+res)