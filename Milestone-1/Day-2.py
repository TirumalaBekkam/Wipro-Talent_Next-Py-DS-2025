
#---------------------------------------------------> 02-07-2025 <------------------------------------------------------------

#-------->json module<-----------


import json
name = input("enter your name:")
age=int(input("enter yu age:"))
data={'name':name,'age':age}
print(data)
stringify_json=json.dumps(data)
print("serialized data of json:",stringify_json)

#json dump and load

import json 
name=input("enter the name:")
age=int(input("enter age:"))
user={"name":name ,'age':age}
with open("user.json",'w') as f:
    json.dump(user,f)
print("data written to json file")

with open("user.json",'r') as f:
    loaded=json.load(f)
    print("read from file", loaded)


#------------------->CSV Module<-----------------------
import csv
with open("people.csv",'w',newline="") as file:
    writer= csv.writer(file)
    writer.writerow(["name",'age'])
    for _ in range(2):
        name=input("enter name:")
        age=int(input("enter age:"))
        writer.writerow([name,age])
print("data written on csv file")

with open("people.csv",'r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)

#------------------------ OS Module <------------------------------------

import os 
folder=input("enter folder name to create:")
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder '{folder}' created!")
else:
    print("Folder already exists")

#--------------------------> Itertools Module <---------------------------

import itertools
data=input("enter characters:")
permute = list(itertools.permutations(data))
print("All permutations")
for p in permute:
    print(' '.join(p))

#-------------------------> Collections Module <------------------------

from collections import Counter
text=input("enter a text:")
counter= Counter(text)
print("characters frequencie:", dict(counter))


#-------------------------------> request package <-----------------------

import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response)
print("status code:",response.status_code)
print("response JSON:",response.json())

# one more program

import requests
url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":"Hii Students",
    "body":"Wipro Geeks",
    "userId":1
}
response= requests.post(url, json=data)
print("Status code",response.status_code)
print("Response json",response.json())

#-----------------------------------------------> Exception Handling<-----------------------------------------------

#Zero Division Error

num=int(input("enter the nuerator:"))
deno=int(input("enter the denominator:"))
try:
    quo=num/deno
    print("Quotient:",quo)
except ZeroDivisionError:
    print("Denominator can't be zero")

#multiple Exceptions

try:
    num=int(input("enter number:"))
    print(num*4)
except (KeyboardInterrupt,ValueError,TypeError):
    print("number should be entered..............program terminated")
print("bye")

#IO Error

try:
    file=open('people.csv')
    str=file.readline()
    strr=file.readline()
    print(str)
    print(strr)
except IOError:
    print('error occured during input take....')
else:
    print("successfully fetched the data")

# raise [exception [,args[,traceback]]]
try:
    num=11
    print(num)
    raise ValueError
except:
    print("exception occured")
    

#--------------------> finally block <---------------------
try:
    print("raising exception")
    raise NameError
except NameError:
    print("exception caught")
finally:
    print("performance clean-up finally")

#AssertionError

c=int(input("enter temp in c:"))
f=(c*9/5)+32
assert(f<=32),"it's cold"
print("fahrenheit:",f)

# StopIteration Eoor

def display(n):
    while True:
        try:
            n=n+1
            if n==21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n,end=" ")
i=0
display(i)

# Random Error


import random
class RandomError(Exception):
    pass
try:
    num=random.random()
    if num<0.1:
        raise RandomError
except RandomError as e:
    print("RandomError generated")
else:
    print("%.4f"%num)

#-------------------> Calender module <-----------------

import calendar
year=int(input("enter a year number:"))
month=int(input("enter a month number:"))
str=calendar.month(year,month)
print(str)


#-------------------->LEAP YEAR USING CALENDER MODULE <-------------------
import calendar
y=int(input("enter the year:"))
if calendar.isleap(y):
    print(y,"is leap year")
else:
    print(y,'is not a leap year')

#------------> print date for 10 days<---------------

from datetime import *
d=date.today()
print(d)
for x in range(1,10):
    nextdate=d+timedelta(days=x)
    print(nextdate)

#------------------->epoch time<--------------

import time
epoch=time.time() # prints the secs from jan 1 1970 to now
print(epoch)
current=time.ctime(epoch)
print("current time calculated from epoch time:",current)


#-------------------------------------------------------> command line arguments <------------------------------------

import sys
if len(sys.argv)<2:
    print("Usage: Hello h1.py <name>")
else:
    name=sys.argv[1]
    print(f"Student,{name}")