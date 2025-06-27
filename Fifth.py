#Write a python program to read amount as a input user and print the number of notes required in Indian Currency Dimension.
#Sample test cases: 
#Enter the total amount : 3864/-
#2000------------->1
#500-------------->3
#200-------------->1
#100-------------->1
#50--------------->1
#20--------------->0
#10--------------->1
#5---------------->0
#2---------------->2
#1---------------->0
amount = int(input("Enter the total amount : "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for note in notes:
    count = amount // note
    print(f"{note}-------------->{count}")
    amount = amount % note