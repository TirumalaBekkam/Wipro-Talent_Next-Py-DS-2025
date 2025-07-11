#-------------------------------------------------> 07/07/25 <------------------------------------------------------------

#-------------------------------------------------> TOPIC:=IO OPERATIONS <---------------------------------------------------------

# opening a file and reading in binary      

#way-1
file=open('file1.txt','rb')
print(file)

#way-2
with open('file1.txt','r') as f:
    content=f.read()
    print(content)

# writing into a file

with open('file1.txt','w') as f:
    for i in range(2):
        a=input("enter data:")
        f.write(a +'\n')


# append into the file

with open('file1.txt','a') as f:
    f.write('Im tirumala this is appended data')


#binary format

data=b'this is sample binary data'
with open('binaryfile.bin','wb') as file:
    file.write(data)

# reading of data in the binary file

with open('binaryfile.bin','rb') as file:
    content=file.read()
    print(content)

# using r+ mode

with open('file1.txt','r+') as file:
    content=file.read()
    file.seek(0)
    file.write("modification is done ")

# using a+ mode

with open("file1.txt",'a+' ) as file:
    file.write('\n Appended data new')
    file.seek(5)                         
    print(file.read())

# readline function

with open('file1.txt','r') as file:
    lines=file.readlines()                     # reads the entire file in list format by sentences                      
for i in lines:
    print(i.strip())  #here the strip function removes the spaces between the sentences

# using list_comprehension 

with open('file1.txt','r') as file :
    separate_lines=[line.strip() for line in file.readlines()] # display the result in one single list
    print(separate_lines)

#close function
file=open('file1.txt','r') 
print(file.closed)
file.close()
print(file.closed)

#program
#program to create a txt file access the text file data and use the data to split the lines into series of words and use space to perform split operation
#sample.txt
# data:- hello students 
# how are you today
#output: ['hello','students','how','are','you','today']

with open('sample.txt','w+') as file:
    for i in range(2):
        data=input("enter data:")
        file.write(data + '\n')
    file.seek(0)  #points to the beginning of the file
    content=file.read()  # Read entire file content
    words=content.split()   # Split content into words based on whitespace
print(words)


# accessing of multiple files

with open('file1.txt','r') as f1 , open('file2.txt','r') as f2:
    content1=f1.read()
    content2=f2.read()
    print("data of file1:")
    print(content1)
    print("data of file2:")
    print(content2)
    f1.close()
    f2.close()