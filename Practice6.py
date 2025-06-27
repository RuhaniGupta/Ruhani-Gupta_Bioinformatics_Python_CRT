'''write python program to read a string as input from the user and split the string into 3 equal halves 
using slicing.'''
s = input("Enter a string: ")
n = len(s)
part = n // 3
first = s[:part]
second = s[part:2*part]
third = s[2*part:]
print("First part:", first)
print("Second part:", second)
print("Third part:", third)