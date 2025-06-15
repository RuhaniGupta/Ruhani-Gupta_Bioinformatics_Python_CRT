#Write a python program to build a function using which prints the multiplication table of n.
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")
multiplication_table(5)