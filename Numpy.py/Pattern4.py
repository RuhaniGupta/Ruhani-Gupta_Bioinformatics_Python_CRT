'''
K 
K R 
K R I 
K R I S 
K R I S H 
K R I S H N 
K R I S H N A
'''
Str="KRISHNA"
Length=len(Str)
for i in range(Length):
    for j in range(i+1):
        print(f"{Str[j]}",end="")
    print()
'''
K
R R
I I I
S S S S
H H H H H 
N N N N N N 
A A A A A A A 
'''
Str="KRISHNA"
Length=len(Str)
for i in range(Length):
    for j in range(i+1):
        print(f"{Str[i]}",end="")
    print()
