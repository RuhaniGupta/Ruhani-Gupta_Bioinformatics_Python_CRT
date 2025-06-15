#write a python program to read a intput value from the user and check whether it is a three-digit number or not a three-digit number.
num = int(input("Enter a number: "))
if 100 <= abs(num) <= 999:
    print("It is a three-digit number.")
else:
    print("It is not a three-digit number.")
