#Write a python program to  print the reversed multiplication table of n.
n = int(input("Enter a number: "))
print(f"Reversed multiplication table of {n}:")
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n*i}")

#Write a python program to  print the reversed multiplication table of 1 to n.
n = int(input("Enter a number: "))
for num in range(1, n + 1):
    print(f"\nReversed multiplication table of {num}:")
    for i in range(10, 0, -1):
        print(f"{num} x {i} = {num * i}")

#Write a python program to  print the reversed multiplication table of n to 1.
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(f"\nMultiplication table of {i} in reverse:")
    for j in range(10, 0, -1):
        print(f"{i} x {j} = {i * j}")
