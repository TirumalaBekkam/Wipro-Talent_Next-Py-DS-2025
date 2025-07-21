############### 1.print True if last digits are same for two integers

# num1=int(input("enter:"))
# num2=int(input("enter:"))
# str1=str(num1)
# str2=str(num2)
# if str1[-1]==str2[-1]:
#     print(True)
    
################ 2.Check for given number is prime or not

# import math
# num=int(input("enter:"))
# if num==0 or num==1:
#     print("Not prime")
# elif num>2:
#     for i in range(2,num):
#         if num%i==0:
#             print("NOt prime")
#             break
#     else:
#         print("prime")
# else:
#     print("Not prime")

################ 3.print prime numbers from 10 to 99

# l=int(input("enter l:"))
# h=int(input("enter h:"))
# l1=[]
# l2=[]
# for num in range(l,h+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 l1.append(num)
#                 break
#         else:
#             l2.append(num)
# print(l2)

################## 4.to print sum of all digits of given number
# num=1234
# sum=0
# for i in str(num):
#     sum+=int(i)
# print(sum)

################ 5.program to print reverse of numbers
"""
num=12345
print(str(num)[::-1])"""


################ 6.chcek for palindrome

# s=110011
# if str(s)==str(s)[::-1]:
#     print("Palndrome")
# else:
#     print("Not ")