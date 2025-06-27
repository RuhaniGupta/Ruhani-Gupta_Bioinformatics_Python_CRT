Str="KRISHNA"
for i in range(len(Str)):
    for j in range(len(Str)):
        print(f"{Str[j]}",end="")
    print()

#For reverse
Str="KRISHNA"
Length=len(Str)
for i in range(Length):
    for j in range(Length):
        print(f"{Str[Length-j-1]}",end="")
    print()