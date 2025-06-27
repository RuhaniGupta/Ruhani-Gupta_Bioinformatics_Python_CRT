'''write a python program to read password as input from the user and check whether to check it is a valid 
password'''
def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    return has_upper and has_lower and has_digit and has_special
pwd = input("Enter your password: ")
if is_valid_password(pwd):
    print("Valid password")
else:
    print("Invalid password")