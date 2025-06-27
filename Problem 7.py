'''Write a python program tp read the input from the user and check whether it is a leap year or not'''
Year = int(input("Enter the Year: "))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(f"{Year} is a Leap Year")
else:
    print(f"{Year} is not a Leap Year")