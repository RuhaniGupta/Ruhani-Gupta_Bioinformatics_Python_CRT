#Write a python program to read a string as input from a user and print the count of 
#Uppercase Vowels 
#Lowercsase Vowels 
#Uppercase Consonants
#Lowercase Consonants

Str=input("Enter the String :")
U_Vowels,L_Vowels,L_Consonants,U_Consonants=0,0,0,0
for ch in Str:
    if(ch.isalpha and ch.isupper):
        if ch is 'AEIOU':
            U_Vowels+=1
        else:
            U_Consonants+=1
    if(ch.isalpha() and ch.islower()):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print("Uppercase Vowel Consonants(L_Vowels)")
print("Lowercase Vowel Consonants(U_Vowels)")
print("Lowercase Consonants Count(L_Consonants)")
print("Uppercase Consonants Count(U_Consonants)")
