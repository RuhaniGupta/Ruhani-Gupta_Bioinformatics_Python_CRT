'''
      K
      R
      I
K R I S H N A
      H
      N
      A
'''
Str = "KRISHNA"
length = len(Str)
mid = length // 2  # Middle index
for i in range(length):
    for j in range(length):
        if i == mid:
            print(Str[j], end=" ")
        elif j == mid:
            print(Str[i], end=" ")
        else:
            print(" ", end=" ")
    print()


