# Activity-1

# list in descending order

l1=[10,30,20,60,40,50]
l1.sort(reverse=True)
print(l1)

#Another way

l1=[10,30,20,60,40,50]
n=len(l1)
for i in range(n):
    for j in range(n-1-i):
        if l1[j]<l1[j+1]:   #if > then ascending order
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)

#Activity-2

# PROGRAM to remove dupliacte elements

l1=[10,30,20,60,60,40,50,30,40,10]
res=list(set(l1))
res.sort()
print(res)

#another way

from collections import Counter
l1=[10,30,20,60,60,40,50,30,40,10]
l2=[]
res=Counter(l1)
print(res)
for i,j in res.items():
    if j>=1:
        l2.append(i)
l2.sort()
print(l2)

# Activity-3

#PROGRAM to finc max element and find it index of first occurrence and last occurence

l1=[10,30,20,60,60,10,40,50,30,40,10,60]
ma=max(l1)
first_index=l1.index(ma)
last_index=len(l1)-1-l1[::-1].index(ma)
print(first_index)
print(last_index)