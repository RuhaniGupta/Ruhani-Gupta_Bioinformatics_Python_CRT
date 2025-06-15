#write a python program to read a mail id as input from the user and print user name and organization name name@org.com.
Mail_id=input("Enter the Mail id :")
List=Mail_id.split('@')
print(List)
print(f"Username : {List[0]}")
Org=List[1]
List=Org.split('.')
print(f"Org Name :{List[0]}")

