"""#add missing month's names below complete list
monthNames=list(("Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec")) #list declaration
num=int(input("Enter a number between 1 to 12:-")) #taking input from user
print("The Month corresponding to given number is:-",monthNames[num-1]) #logic of code:-it will print name of month related to num

daysOfWeek=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print(daysOfWeek[:3]) #this will read only till 3 elements from index 0. here before there will be value of index before colon and after colon there will be given number of elements to be read.

daysOfWeek=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print(daysOfWeek[3:])""" # this read value from index 3 to end of list.

rainfallData=["""index of this is:-0 """[1,"Arunachal Pradesh",2],"""1"""[2,"Sikkim",5],"""2"""[3,"West Bengal",1],"""3"""[4,"Odisha",4],"""4"""[5,"Uttarakhand",3]]
#print(rainfallData[3][0],rainfallData[3][1]) #this will print value of 3rd index's 0th and 1st indices's values. 
print(rainfallData[0][0],rainfallData[0][1],rainfallData[0][2])