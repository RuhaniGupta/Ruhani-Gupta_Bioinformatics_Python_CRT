n=int(input("Enter the Size of List:"))
List=[]
List1=[]
for i in range (n):
    Temp=float(input("Enter the values:"))
    List.append(Temp)
for i in List:
    if i<5:
        List1.append("underexpressed")
    elif i>=5 and i<=15:
        List1.append("Normal")
    else:
        List1.append("Overexpressed")
print(List1)
