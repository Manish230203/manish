""" #Ternary Operators
age=int(input('Enter your age'))
print('You are not an adult' if age<18 else'Just 18!' if age==18 else'Legally adult')

#using if,elif,else
age=int(input('Enter your age'))
if(age<18):
    print('You are not an adult yet')
elif(age==18):
    print('Just 18!')
else:
    print('Legally Adult')
"""


#in python for switch case there is keyword called match.
day=input('Enter a day of week')
match day:
    case 'Mon'|'mon'|'Monday'|'monday':
        print('Monday')
    case 'Tues'|'tues'|'Tuesday'|'tuesday':
        print('Tuesday')
    case 'Wed'|'wed'|'Wednesday'|'wednesday':
        print('Wednesday')
    case 'Thu'|'Thu'|'Thursday'|'thursday':
        print('Thursday')
    case 'Fri'|'fri'|'Friday'|'friday':
        print('Friday')
    case 'Sat'|'sat'|'Saturday'|'saturday':
        print('Saturday')
    case 'Sun'|'sun'|'Sunday'|'sunday':
        print('Sunday')
    case _:
        print('Incorrect Value')