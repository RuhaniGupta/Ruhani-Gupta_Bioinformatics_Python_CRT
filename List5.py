'''write a python program  to reverse a list of numbers without using reverse method.(-ve slicing,not done)
write a python program to sort a list of numbers without using sort method.(not done)
#write a python program to remove the duplicate values from the list'''
List=[5,5,19,19,2,2]
print("Original List:")
print(List)
New_List=[]
for i in List:
    if i in New_List:
        New_List.append(i)
    print(New_List)

#write a python program to read the list element as input from the user and print a new list of number which are multiples of 5.
Size=int(input("Enter the Element:"))
New=[New_List]
for i in range(Size):
    Temp=int(input("Enter Elements:"))
    New.append(Temp)
print(New)
for i in List:
    if(i%5==0):
     print(New_List)


