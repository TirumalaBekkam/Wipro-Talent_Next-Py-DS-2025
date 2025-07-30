#-------------------------------------------------> list comprehension <----------------------------------------

"""" PROGRAM: CODE to take user input of random 20 numbers using list comprehension and print them"""

# x=[int(i) for i in input("enter:").split()[:] if int(i)%2==0]
# print(x)

######################################
""" code to take user input with space seperated and convert the 9 inputs into 3X3 matix form on display"""

# n=[int(i) for i in input("enter:").split()[:9]]
# m=[[n[i*3+j] for j in range(3)] for i in range(3)]
# for x in m:
#     print(x)

########################################
'''
Write a code to convert dec to binary matrix by considering even and odd manipulations for 
user defined variabls of an nXn matrix where n =3 and 
list=[[1,2,3],[3,3,3],[4,5,6]]
output:
1 0 1
1 1 1
0 1 0'''

# list=[[1,2,3],[3,3,3],[4,5,6]]
# for i in list:
#     for j in i:
#         if j%2==0:
#             print("0",end=" ")
#         else:
#             print("1",end=" ")
#     print( )

# Another way

# list_=[[1,2,3],[3,3,3],[4,5,6]]
# n=[[0 if j%2==0 else 1 for j in i]for i in list_]
# for i in n:
#     print(i)

######################################

# PRINT PATTERN
    #j
  #i# * * * * * * *
    # * * *   * * *
    # * *       * *
    # *           *
    # * *       * *
    # * * *   * * *
    # * * * * * * *
# n=9
# P=[" ".join(" " IF (abs(i-n//2)+ abs(j-n//2) <n//2)and i !=0 and i!=n-1 else "*" for j in range(n) for i in range(n))]
# for r in P:
#     print(r)
