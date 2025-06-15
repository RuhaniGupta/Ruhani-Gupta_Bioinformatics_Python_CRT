#Write a pyhton program to read a intput value from the user and check whether it is a two digit number or not a tw
num = int(input("Enter a number: "))
if (num >= 10 and num <= 99) or (num <= -10 and num >= -99):
    print("It is a two-digit number")
else:
    print("It is not a two-digit number")
