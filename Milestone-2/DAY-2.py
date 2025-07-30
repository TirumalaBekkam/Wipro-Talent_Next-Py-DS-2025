#---------------------------------------------> Lambda function <-------------------------------------------

"""PROBLEM:  data=[10,'hi',4.5,'students',3,100] from the list containing numbers and strings, extract only integers using lambda function and list comprehension"""

# data=[10,'hi',4.5,'students',3,100] 
# res=[x for x in data if(lambda v:type(v)==int)(x)]
# print(res)

##########################################

"""PROGRAM: calculate the factorial of n using recursion of lambda function"""

# fact=(lambda f: lambda n: 1 if n==0 else n*f(f)(n-1))(lambda f: lambda n:1 if n==0 else n*f(f)(n-1))
# print(fact(4))

###########################################

"""PROGRAM: SUM of digits : 3426 """

# dsum=(lambda f: lambda n:0 if n==0 else n%10 + f(f)(n//10))(lambda f: lambda n:0 if n==0 else n%10 +f(f)(n//10))
# print(dsum(1234))

##########################################

""""SYNTAX"""
# pvar= lambda v1,v2...............: operation /condition /boolean exp

#---->EXAMPLE 

# add_=lambda num1,num2: num1+num2
# print(add_(11,22))

#####################################

# accessing single elememt

# big= lambda x,y : x if x>y else y
# print(big(5,2))

####################################

# nums=[1,2,3,4,5,6,7,8,9,10]
# res=list(filter(lambda num : num%2!=0,nums))  # filter selects or chooses where map evaluates
# print(res)

#####################################

# packs=[(11,99),(2,11),(66,66)]
# result=sorted(packs,key=lambda x:x[1])
# print(result)

####################################

# def b(n):
#     return lambda x: x*n
# a=b(2)
# print(a(5))

###################################

# LC WITH LAMBDA

# data=['pen','cap','bat']
# upper=[(lambda x: x.upper())(d) for d in data]
# print(upper)

###################################

""""PROGRAM : program to print reverse string using lambda and list comprehension"""

# str_='Hello'
# res=lambda x:str_[::-1]
# print(res(None))

#another away

# str_="Hello"
# res=lambda x :''.join([x[i] for i in range(len(str_)-1,-1,-1)])
# print(res(str_))

#####################################

"""PROGRAM: program to reverse a str within the list"""

# words=['Tiru','Sri','Akira','Vini']
# rw=[(lambda w: w[::-1])(word) for word in words]
# print(rw)

######################################

"""PROGRAM :  to remove spaces in list and it """

l=['hi','','students','','bye']
res=[s for s in l if(lambda x: x!="")(s)]
print(res)