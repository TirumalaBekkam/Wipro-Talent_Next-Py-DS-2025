#-------------------------------------------------------------> 09/07/25 <---------------------------------------------------------
#----------------------------------------------- > Sys Module < ------------------------------------------------

# program-1

import sys
print("Script name:",sys.argv[0])
print("All args:",sys.argv[1:])
print("Number of items:",len(sys.argv))
print("Including file name:",sys.argv)
if len(sys.argv)>1:
    print("First arg:",sys.argv[1])
else:
    print("No arguments provided")

# program to multiply numbers

import sys
num1=int(sys.argv[1])
num2=int(sys.argv[2])
num3=int(sys.argv[3])
print("prodct:",num1*num2*num3)

# calculation of area of rectangle

import sys
if len(sys.argv) !=3:
    print("Usage: python Day-5 l b")
else:
    l=float(sys.argv[1])
    b=float(sys.argv[2])
    print("calculated area:",l*b)

#program

import sys
if len(sys.argv)<2:
    print("Usage: python file m1,n2...")
    sys.exit()
numbers=[int(arg) for arg in sys.argv[1:]]
total=sum(numbers)
print("Numbers:",numbers)
print("sum:",total)

#program 

import argparse
parser=argparse.ArgumentParser(description='Add 2 Numbers')
parser.add_argument('--X', type=int,required=True, help="First Number")
parser.add_argument('--Y', type=int,required=True, help="Second Number")
args=parser.parse_args()
result=args.X+args.Y
print("Sum is:",result)

#Calculator program 

import argparse
parser=argparse.ArgumentParser(description="Add 2 numbers")
parser.add_argument('--x',type=int,required=True,help="First number")
parser.add_argument('--y',type=int,required=True,help="Second number")
parser.add_argument('--opt',type=str,required=True, choices= ['add','sub','mul','div'],help="Operation")
args=parser.parse_args()
if args.opt=='add':
  result=args.x + args.y
elif args.opt=='sub':
  result=args.x - args.y
elif args.opt=='mul':
  result=args.x * args.y
elif args.opt=='div':
  result=args.x / args.y
print("Result is",result)

#-------------------------------------------------> OS MODULE <------------------------------------------------------

#read and list the files in that folder which contains sample.py file(folder)

import os
path="."                       #reads all the files in that folder and provides list of folders present in that particular folder 
files=os.listdir(path)
print("files and folders in current directory:")
for f in files:
   print(f)


#creates new folder in the folder which contains the sample.py files

import os
folder="new_folder"
if not os.path.exists(folder):
   os.mkdir(folder)
   print(f"Folder '{folder}' created.")
else:
   print(f"Folder '{folder}' already exists.")



#delete a file
#create a file in the folder before deleting!!!

import os
file="deletingfile.txt"
if os.path.exists(file):
    os.remove(file)
    print(f"{file} deleted.")
else:
    print("file not found")

# program

import os
file="shift.py"
if os.path.exists(file):
   size=os.path.getsize(file)
   print(f"{file} size:{size} bytes.")
else:
   print("file not Found")