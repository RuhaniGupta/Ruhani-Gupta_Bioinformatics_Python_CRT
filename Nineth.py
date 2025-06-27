#write a python program
#a)To print natural number from 1 to n.
n=int(input("Enter a number"))
print(f"Natural number from 1 to {n}:")
for i in range(1,n+1):
    print(i)

#b)To print natural number from n to 1.
n=int(input("Enter a number"))
print(f"Natural number from n to {1}:")
for i in range(n,0,-1):
    print(i)

#c)To print squares of 1 to n.
n=int(input("Enter a number"))
print(f"Squares from n to {1}:")
for i in range(1,n+1):
    print(i*i)

#d)To print squares of n to 1.
n=int(input("Enter a number"))
print(f"Squares from n to {1}:")
for i in range(n,0,-1):
    print(i*i)
#e)To print cubes of 1 to n.
n=int(input("Enter a number"))
print(f"cubes from 1 to {n}:")
for i in range(1,n+1):
    print(i*i*i)
#f)To print cubes of n to 1.
n=int(input("Enter a number"))
print(f"cubes from n to {1}:")
for i in range(n,0,-1):
    print(i*i*i)