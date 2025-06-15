#Set={10,20,30,40,50,60,70,80,90,100}
#print(Set)
#print(type(Set))

fruits={'banana'}
fruits.add(101)
#Add method
fruits.add('orange')
print(fruits)
#Update method
fruits.update(['apple','banana'])
print(fruits)
#remove method
fruits.remove('banana')
print(fruits)
#Pop method
fruits.pop()
print(fruits)
#Discard mathod
fruits.discard('apple')
print(fruits)
#Clear method
fruits.clear()
print(fruits)

#Union 
Set1={1,2,3}
Set2={3,4,5}
print(Set1|Set2)

#intersection
Set1={1,2,3}
Set2={3,4,5}
print(Set1&Set2)
print(Set1-Set2)
print(Set1^Set2)
