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
Amount=int(input("enter a amount:"))
print("2000--------->",Amount//2000)
Amount=Amount%2000
print("500---------->",Amount//500)
Amount=Amount%500
print("200---------->",Amount//200)
Amount=Amount%200
print("100---------->",Amount//100)
Amount=Amount%100
print("50----------->",Amount//50)
Amount=Amount%50
print("20----------->",Amount//20)
Amount=Amount%20
print("10---------->",Amount//10)
Amount=Amount%10
print("5----------->",Amount//5)
Amount=Amount%5
print("2----------->2",Amount//2)
Amount=Amount%2
print("1----------->1",Amount//1)
Amount=Amount%1