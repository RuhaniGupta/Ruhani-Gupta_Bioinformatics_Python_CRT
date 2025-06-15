#Write a python program to read a sentence as input from the user and print the list of words from the sentence.
Sentence="We are learning Python"
List=Sentence.split()
print(List)

#Write a python program to read a string as input from the user.
#Reverse the string.
#Covert the string into lower case.
#convert the string into uppercase.
#convert the string into uppercase to lowercase and lowercase to uppercase.
#Check if the string is starting  with letter A.
#Print the count of character A from the given string and replace all letter P to letter J.
Str=input("Enter the string:")
print(Str[::-1])
print(Str.lower())
print(Str.upper())
print(Str.swapcase())
print(Str.startswith('P'))
print(Str.count('P'))
Str=Str.lower()
print(Str.replace('p','j'))

#write a python program to read the list of characters as input from the user and converted into a word.
Size=int("Enter the length of list:")
Char_List=[]
for i in range(Size):
    ch=input("Enter the characters :")
    Char_List.append(ch)
print(Char_List)
Str="-".join(Char_List)
print(Str)

