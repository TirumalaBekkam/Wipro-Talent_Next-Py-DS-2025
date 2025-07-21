#-------------------------------------------------> Loop Based <------------------------------------

# PROBLEM: Display number  separated with ','

n=int(input("enter n:"))
s=str(n)
print(','.join(s))

#Activity-1: count number od digits

n=int(input("enter:"))
s=str(n)
print(len(s))

#Activity-2:sum of number

n=int(input("enter:"))
sum=0
for i in str(n):
    sum=sum+int(i)
print(sum)

#Activity-3

#PROGRAM to display binary value

n=int(input("enter:"))
print(bin(n)[2:])

#Activity-4

#--->PROGRAM to display binary equivalent number

b=input("enter:")
print(int(b,2)) # the int(b,2) the 2 will tell the interperter that is of base 2

#Activity-5

# PROGRAM to diaplay the smallest exact diviser of that number 

import math
num=int(input("enter:"))
l1=[]
for i in range(2,int(math.sqrt(num))+1):  # because the diviser can be beyond sqart of number
    if num%i==0:
        l1.append(i)
if l1:
    print(min(l1))
else:
    print("No exact divisor found")

