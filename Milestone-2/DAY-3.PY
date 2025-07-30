##---------------------------------------------> LAMBDA FUNCTION <---------------------------------------------

"""Nested lambda to return expression"""

# l2=lambda a: lambda b,c: (a+b)*c
# l1=l2(2)
# value=l1(1,3)
# print(value)

'''or'''

# o=(lambda a: lambda b,c: (a+b)*c)(5)(3,2)
# print(o)

##########################################

"""(a+b)*(c+d)"""

# o=(lambda a,b: lambda c,d:(a+b)*(c+d))(1,2)(1,2)
# print(o)

'''or'''

# o=(lambda a: lambda b: lambda c,d: (a+b)*(c+d))(1)(2)(3,4)    #universal(global(local))
# print(o)

############################################

"""PROBLEM : (a-b)/(c-d)"""
# try:
#     o=(lambda a: lambda b: lambda c,d: (a-b)/(c-d))(10)(5)(2,1)
#     print(o)
# except ZeroDivisionError:
#     print("Division is not possible by zero")
#except TypeError:
#     print("Invalid datatype!")

#############################################

# num=int(input("enter a:"))
# n=int(input("enter x:"))
# numsq=lambda a: lambda x: (a+x)**2
# res=numsq(num)
# print(res(n))

###########################################

# o=(lambda a: lambda b: lambda c,d:a+ '-' +b+ '-'+c+'-' +d)('Hii')('all')('GoodMorg','seeyaaa!')
# print(o)

##############################################

# o=(lambda a: lambda b: lambda c,d:a.upper() + '-' +b+ '-'+c.upper()+'-' +d)('Hii')('all')('GoodMorg','seeyaaa!')
# print(o)

#################################################

# o=(lambda a: lambda b: lambda c,d:a[::-1] + '-' +b[::-1]+ '-'+c[::-1]+'-' +d[::-1])('Hii')('all')('GoodMorg','seeyaaa!')
# print(o)

###################################################

# num=[4,6,3,8]
# clist=[12,12,9,16]
# res=lambda x: [i*2 if i>5 else i*3 for i in num]
# print(res(None))

###################################################

numbers=lambda x: lambda a : a*2 if a>x else a*3
above_5=numbers(5)
num=[4,6,3,8]
res=list(map(above_5,num))
print(res)