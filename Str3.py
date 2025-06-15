Str="python program"
print(Str.capitalize())
print(Str.title())
print(Str.casefold())
print(Str.startswith('P'))
print(Str.find('o'))
print("Hi".center(30,"*"))

#write a python program to read a string as input from the user and print number of 
#print the count of uppercase letters.
#print the count of lowercase letters.
#print the count if numeric values.
#print the count of special characters.
Str=input("Enter the String")
Uppercase_Alpha=0
Lowercase_Alpha=0
Numeric=0
Special_char=0
for ch in Str:
    if ch.isupper():
        Uppercase_Alpha=+1
    elif ch.islower():
        Lowercase_Alpha+=1
    elif ch.isdigit():
        Numeric+=1
    else:
        Special_char+=1
    print(f"Count of Uppercase letters: {Uppercase_Alpha}")
    print(f"Count of Lowercase letters: {Lowercase_Alpha}")
print(f"Count of Numeric values: {Numeric}")
print(f"Count of Special Characters: {Special_char}")

#Write a python program to take name as input from the user and print the gender classification of name on basics of prefix.
Str=input("Enter the name with prefix(Ms/Mr) :")
if Str.startswith('Ms'):
    print("Female")
else:
    print("Male")

