Num=int(input("Enter the Integer number:"))
#using if-else
if(Num>0):
    print(f"{Num} is +Ve Number")
elif(Num<0):
    print(f"{Num} is -Ve Number")
else:
    print(f"{Num} is 0")
#using ternary operator
Res="+Ve Num" if(Num>0)else "-Ve Num"
print(f"{Num} is {Res}")

