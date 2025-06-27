'''Write a python program to read the string as input from the user has done and 
print the string as a list of individual characters.
#Find the length of string.
#Find the minimum element after converting String into List.
#Find the number of spaces present in the string without using any built-in function from the user.'''

user_input = input("Enter a string: ")

# Print as list of individual characters
char_list = [ch for ch in user_input]
print("List of characters:", char_list)

# Find the length of string
print("Length of string:", len(user_input))

# Find the minimum element after converting string into list
print("Minimum element in list:", min(char_list))

# Find the number of spaces without using any built-in function
space_count = 0
for ch in user_input:
    if ch == ' ':
        space_count += 1
print("Number of spaces:", space_count)