#Write a python program to print natural numbers from 1 to n.
N=int(input("Enter the Value of n:"))
def NaturalNum(N):
    if N==0:
        return
    NaturalNum(N-1)
    print(N)
NaturalNum(N)

#Write a python program to print natural numbers from n to 1.
N=int(input("Enter the Value of n:"))
def NaturalNum(N):
    if N!=0:
        return
        print(N)
    NaturalNum(N-1)
NaturalNum(N)

#Write a python program to print Alphabets from A to Z using recursion.
def Alphabets(ch):
    if ch>=ord('A') and ch<=ord('Z'):
        print(chr(ch))
        return Alphabets(ch+1)
ch=65
Alphabets(ch)
print("------------------------------")

#Write a python program to print Alphabets from Z to A using recursion.
ch=65
Alphabets(ch)
print("------------------------------")
def Alphabets(ch):
    if ch>=ord('A') and ch<=ord('Z'):
        print(chr(ch))
        return Alphabets(ch-1)
ch=90
Alphabets(ch)

