#Write a python program to print Uppercase alphabets from a to z including their a to z.
for i in range(1,27):
    print(chr(i+64),"--->",i+64)
for i in range(i,27):
    print(chr(i+96),"--->",i+96)

#write a python program to read a character as input from the user and print the asqui value of this character.
char = input("Enter a character: ")
if len(char) == 1:
    print("ASCII value of", char, "is", ord(char))
else:
    print("Please enter only a single character.")

#Write a python program to read a string as input from the user and replace all vowels with O's.
Str=input("Enter the Str")
modified = ""
for i in Str:
    if i in 'AEIOUaeiou':
        modified+='0'
    else:
        modified+='1'
    print(modified)

