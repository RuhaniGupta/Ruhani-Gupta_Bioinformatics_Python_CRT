#
Num_list=[1,2,3,4,5,6,7,8,9]
print(Num_list)
print("Accessing the List Elements using:")
print(Num_list[0])
print(Num_list[1])
print(Num_list[2])
print(Num_list[3])
print(Num_list[4])
print(Num_list[5])
print(Num_list[6])
print(Num_list[7])
print(Num_list[8])
print("Accessing the list using -ve Index:")
print(Num_list[-9])
print(Num_list[-8])
print(Num_list[-7])
print(Num_list[-6])
print(Num_list[-5])
print(Num_list[-4])
print(Num_list[-3])
print(Num_list[-2])
print(Num_list[-1])

#Accessing the list elements using for loop without Index.
print(Num_list)
print("Accessing the list elements using for loop without Index:")
for i in Num_list:
    print(i)

#Accessing the list elements using for loop with Index.
print(Num_list)
print("Accessing the list elements using for loop with Index:")
for i in range(len(Num_list)):
    print(Num_list[i])

#Accessing the list elements using while loop with Index.
print("Accessing the list elements using while loop with Index:")
i=0
while(i<len(Num_list)):
    print(Num_list[i])
    i+=1

