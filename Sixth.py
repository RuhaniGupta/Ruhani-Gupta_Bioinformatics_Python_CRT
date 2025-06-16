#Write a python program to read an integer value as an input from the user and print the multiplication of it.
num=int(input("Enter a number"))
[print(f"{num}*{i} = {num*i}") for i in  range(1,11)]