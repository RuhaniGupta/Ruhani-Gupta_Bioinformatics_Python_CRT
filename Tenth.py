#write a python program to read the input values from the user and find the number of digits present in that particular number.
#Sample input : 12345
#Sample output : 12345 has 5 digits
#              rem      quot
#12345//10----->5       1234
#1234//110----->4       123
#123//10------->3       12
#12//10-------->2       1
#1//10--------->1       0

Num=int(input("Enter the value of Num:"))
Temp=Num
DigitCount=0
while(Num>0):
    Num=Num//10
    DigitCount+=1#DigitCount=Digitcount+1
print(f"{Temp} has {DigitCount} digits")
