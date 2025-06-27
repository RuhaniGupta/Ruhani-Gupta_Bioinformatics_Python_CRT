'''
K R I S H N A
K           A
K           A
K           A
K           A 
K           A
K R I S H N A
'''
Str="KRISHNA"
Length=len(Str)
for i in range(Length):
    for j in range(Length):
        if i==0 or i==Length-1 or j==0 or j==Length-1:
            print(f"{Str[j]}",end=" ")
        else:
            print(" ",end=" ")
    print()