Color=['White','red','pink','grey','green']
print(Color)
del(Color[2])
print(Color)
del Color[-3]
print(Color)

#Write a python program to read the size of list as input from the user and pick the list elements also from the input from the user and find the max element/number present in the list and minimum element and summation from the list & print sorted list in ascending order.
Size=int(input("Enter the size of list:"))
Num=[]
for i in range(Size):
    Temp=int(input(f"Enter the Element at {i} index :"))
    Num.append(Temp)
print(f"Given list:{Num}")
print("Maximum Element:",max(Num))
print("Minimum Element:",min(Num))
print("Summation Element:",sum(Num))
print("Sorted List:",sorted(Num))

