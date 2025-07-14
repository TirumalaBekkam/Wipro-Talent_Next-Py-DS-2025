# Activity-1

#--->Problem: accept 10 elemts and print sum of them

l=[]
for i in range(10):
    a=int(input("enter:"))
    l.append(a)
print(sum(l))

#Activity-2

#--->Problem: print max 3 and min 3 elements from array without using sort

l1=[]
l2=[]
l=[20,10,50,60,30,100,400,500]
for i in range(3):
    ma=max(l)
    mi=min(l)
    l1.append(ma)
    l2.append(mi)
    l.remove(ma)
    l.remove(mi)
res=l1+l2
print(res)

# (or) Another way 

l=[20,10,50,60,30,100,400,500]
max_list=[float('-inf')]*3
min_list=[float('inf')]*3
for num in l:
    if num>max_list[0]:
        max_list=[num] + max_list[:2]
    elif num>max_list[1]:
        max_list=[max_list[0],num,max_list[1]]
    elif num >max_list[2]:
        max_list[2]=num
    if num < min_list[0]:
        min_list = [num] + min_list[:2]
    elif num < min_list[1]:
        min_list = [min_list[0],num, min_list[1]]
    elif num < min_list[2]:
        min_list[2]=num 
print(max_list)
print(min_list)

# Activity-3
# --->Problem: program to reverse a list 

l=[10,20,30,40,50]
l.reverse()
print(l)

# without using reverse function

l=[10,20,30,40,50]
print(l[::-1])

# manual doing

l=[10,20,30,40,50]
l1=[]
for i in range(len(l)-1,-1,-1):
    l1.append(l[i])
print(l1)