Cartoons=["Chota bheem","oggy","tom & jerry","Doremon"]
print(Cartoons)
print("After appending:")
Cartoons.append('Shinchan')
print(Cartoons)
Cartoons.insert(0,'Benten')
print(Cartoons)
Cartoons.pop()
print(Cartoons)
Cartoons.pop(0)
print(Cartoons)

#
Cartoons=["Chota bheem","oggy","tom & jerry","Doremon"]
print(Cartoons)
Cartoons.remove('oggy')
print(Cartoons)
print(Cartoons.index('tom & jerry'))
Cartoons.reverse()
print(Cartoons)

#Reverse a list without using reverse function.
Num=[11,22,33,44,55,66,77,88,99]
print(Num[0:])
print(Num[1:4+1])
print(Num[::1])
print(Num[::2])
print(Num[::1])

#reverse a list using extend function.
Prog_lang=['C','C++','Java','Python','Go-Lang']
print(Prog_lang)
Front_End=['HTML','CSS','JAVASCRIPT','REACT JS']
print(Front_End)
Prog_lang.extend(Front_End)
print(Prog_lang)
print(Prog_lang.count('HTML'))Color=['White','red','pink','grey','green']
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


