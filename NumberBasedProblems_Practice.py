#---------------------------------------------> Number building <----------------------------------------

# Activity-1 [Swap of three variables]

#OUTPUT:: a-->c,b-->a,c-->b

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
t=a+b+c
a_o=a
b_o=b
c_o=c
a=t-(a_o+b_o)
b=t-(b_o+c_o)
c=t-(a_o+c_o)
print("a,b,c:",a,b,c)

#Activity-2

#problem: Given set of 3 students marks ,count of number of pass 

l=list(map(int,input("enter:").strip('[]').split(',')))
count=0
for i in l:
    if i>=35:
        count+=1
print("No of student passes:",count)

#Activity-3

#Problem::count of negative and non-neg elems in list of range 5

l=[]
c_p=0
c_n=0
for i in range(5):
    n=int(input("enter:"))
    l.append(n)
for i in l:
    if 0<=i<=100:
        c_p+=1
    else:
        c_n+=1
print("Non-negativ count:",c_p)
print("Negative count:",c_n)

#Activity-4

#Check for even or odd or zero


n=int(input("enter number:"))
if n%2==0:
    print("Even")
elif n%2!=0:
    print("Odd")
else:
    print("Zero")

# Activity-5

#sum of set of numbers

s=set(map(int,input("enter numbers:").split()))
print(sum(s))