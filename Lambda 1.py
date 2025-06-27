#Write a python program to print the addition of two numbers using lambda function.
add_numbers = lambda x, y: x + y
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is:", add_numbers(num1, num2))