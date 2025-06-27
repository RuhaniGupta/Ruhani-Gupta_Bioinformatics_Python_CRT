'''
write a python program to read name,contact no., mail id and password and make sure that contact no has only  10 digit
and mail should have a valid structure name @  organization and passwpord should have 3 uppercase 
3 lowercase alphabets and 3 special characters and number and password should not be less than 10.'''
import re
def is_valid_contact(contact):
    return contact.isdigit() and len(contact) == 10
def is_valid_email(email):
    return re.match(email) is not None
def is_valid_password(password):
    if len(password) < 10:
        return False
    upper = sum(1 for c in password if c.isupper())
    lower = sum(1 for c in password if c.islower())
    digit = any(c.isdigit() for c in password)
    special = sum(1 for c in password if not c.isalnum())
    return upper >= 3 and lower >= 3 and special >= 3 and digit
name = input("Enter your name: ")
contact = input("Enter your 10-digit contact number: ")
email = input("Enter your email (name@organization): ")
password = input("Enter your password: ")
if not is_valid_contact(contact):
    print("Invalid contact number. It must be exactly 10 digits.")
elif not is_valid_email(email):
    print("Invalid email format. It should be in the form name@organization.")
elif not is_valid_password(password):
    print("Invalid password. It must have at least 3 uppercase, 3 lowercase, 3 special characters, a number, and be at least 10 characters long.")
else:
    print("All inputs are valid!")