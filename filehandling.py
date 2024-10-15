#python allows a file to be operated in text or binary format.
#allows to perform a wide range of operation such as creating,opening,reading,writing file.
#to handle file it should be first loaded in primary memory.
#syntax for opening file: fileObject=open(r"filename","access mode").here r is used to tell interpreter to treat filename as string and don't override it.
#syntax for closing file: fileObject.close().
#fileObject=handler to point to a file.
# r = read,r+ = read and write,w = write.

"""myfile=open("ABC.txt",'r')
#print(myfile.read())
myfile.seek(0) #using seek method pointer is positioned.
print(myfile.read(4))
print('Current file pointer location is at character: ',myfile.tell()) #tell method is used to know file pointer position.
myfile.seek(10)
print('File pointer repositioned')
print(myfile.read(10)) #to read file from current position to given numbers of line i.e. here 10 characters.

print('Reading line by line without using readline()')
myfile.seek(0)
for line in myfile:
    print(line)
    
#use of readline() method

myFile=open('ABC.txt','r')
filedata=myFile.readline()
while filedata:
    print(filedata)
    filedata=myFile.readline()
print('The whole file was read using readline()')

#use of readlines() method

myFile=open('ABC.txt','r')
filedata=myFile.readlines()
while filedata:
    print(filedata)
    filedata=myFile.readlines()
print('The whole file was read using readline()')
 
#use of write() method.
myFile=open('StudentData.txt','a')#'w')
addMore=True
while addMore:
    stNm=input('Enter name of student:')
    myFile.write(stNm)
    #myFile.write('\n')
    st=input('Enter F/f if you want to stop adding names.Else enter any key')
    if st=='F' or st=='f':
        addMore=False
print('All Names are added to file')
#below code is to check whether entered data is added to file or not.
myFile=open('StudentData.txt','r')
print('The names added to file are as given below:')
stNm=myFile.readlines()
for nm in stNm:
    print(nm)
myFile.close()"""

myFile=open('MultiLine.txt','w')
content=[]
addMore=True
while addMore:
    stNm=input('Enter name of student:')
    content=content+[stNm+'\n']
    st=input('Enter F/f if you want to stop adding names.Else enter any key')
    if st=='F' or st=='f':
        addMore=False
myFile.writelines(content)
myFile.close()
print('File written successfully')