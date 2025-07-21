#functions,modules,packages
#math module
#functions--sqrt,factorial,pow,floor,ceil,pi"""

#-------------------->Math Module<--------------------

import math
num=int(input("enter the number:"))
print("square root",math.sqrt(num))
print("factorial",math.factorial(num))
print("pi value",round(math.pi,4))
print("pi operstion:",math.pi*2)

#--------------------->Random module<-------------------------

#random -generate numbers , random choices , shuffle , random.sample 
#randint

import random
# from random import randint
print("Random number from 10 to 50:", random.randint(10,50))
# if we use random.random --> it is dinamically used
print("Random number from 0 to 1:", random.random())
# for floating random number (uniform)
print("Random number from 1.5 to 5.5:", random.uniform(1.5,5.5))
# choice 
fruits=['banana','apple','orange','mango']
print("Random choice from list:", random.choice(fruits))
print("Random choice from list:", random.choices(fruits))
num=[1,2,3,4,5]
random.shuffle(num)
print("shuffle list:",num)
random.seed(26)
print(random.randint(1,100))

#---------------->DateTime Module<----------------------


# datetime ,
# datatime,now()--> it fetch data from the machine
# datetime.strptime()--->str time to general time 
# datetime.strftime()---> string format time
# timedelta
# date.today()
# datetime.date

from datetime import datetime,date, timedelta

#current time and date
now=datetime.now()
print("current datetime:",now)

#only date

print("today date:",date.today())

# formatted datetime

formatted=now.strftime("%d-%m-%Y %H:%M:%S")
print("formatted datetime:",formatted)

#parsed datetime 

date_str="24-12-2000 14:55:00"
parsed= datetime.strptime(date_str,"%d-%m-%Y %H:%M:%S")
print("parsed data:", parsed)

#timedelta 

tomorrow = now+timedelta(days=1)
print("Tomorrow:",tomorrow)
yesterday= now-timedelta(days=1)
print("yesterday:",yesterday)
ftime= now+timedelta(hours=3,minutes=30)
print("future time after 3.5 hrs:",ftime)

# time zone changing

now=datetime.now()
#%I-->0-12
#%p-->AM/PM
#%H--> 0-23
format_12hr=now.strftime("%d/%m/%Y %I:%M:%S %p")
print("zone conversion:",format_12hr)
