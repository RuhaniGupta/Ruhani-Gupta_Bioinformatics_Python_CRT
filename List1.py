#write a python program to read the list elements as input from the user & display the list element using for loop?
Size=int(input("Enter the Size of List:"))
Prog_lang=[]
#reading the list elements as input
for i in range(Size):
    Temp=input("Enter a Programming lang:")
    Prog_lang.append(Temp)
print("Elements of the List:")
print(Prog_lang)

