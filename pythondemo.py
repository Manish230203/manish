""" while(True):
    num=int(input("Enter a number:-"))
    if(num%2==0):
        print('Even Number')
        continue #this keyword will make code go on 
    else:
        print('Odd Number')
        break #this will break code
print('here is cursor now')

message='Hello World'
for i in message:
    print(i)
    
myList=['ABC',1,2,'PQR',True]
for i in myList:
    print(i)

for i in range(1,15,2):
    print(i) 
    
myTelephoneDiary={"ABC":1234,"PQR":5678,"XYZ":2343,"QWE":7890}
for ky in myTelephoneDiary:
    print(f'The value for{ky}is{myTelephoneDiary[ky]}')   
    
message=input("Enter a string:-")
for i in range(0,len(message),2):
    print(message[i]) """

import sys
while True:
    status=input('Enter Y to continue or N to Exit:- ')
    if status=='Y':
        num=int(input('Enter a number to determine if it is odd or even:- '))
        if num%2==0:
            print(num,'is even number.')
        else:
            print(num,'is odd number')
    elif status=='N':
        print('Thank you!See you again')
        sys.exit() #exit is a method to terminate code
        print('hello')
        
