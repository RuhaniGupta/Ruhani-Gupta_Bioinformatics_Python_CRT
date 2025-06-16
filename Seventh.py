#Write a python program to  print the multiplication table from 1 to n.
Num=int(input("Enter a value of Number:"))
for i in range(1,Num+1):
    print(f"Multiplication table of {i}:")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")