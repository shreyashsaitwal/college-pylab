# Write a python program that accepts a string to setup a password with
# following requirements:
# - The password must be at least eight characters long
# - It must contain at least one uppercase letter
# - It must contain at least one lowercase letter
# - It must contain at least one numeric digit
# The program checks the validity of password.

inp = input("Enter password: ")
valid = True

if len(inp) < 8:
    print("Password must be at least 8 characters long")
    valid = False

if inp.islower():
    print("Password must contain at least one uppercase letter")
    valid = False

if inp.isupper():
    print("Password must contain at least one lowercase letter")
    valid = False

if not any(map(lambda x: x.isdigit(), inp)):
    print("Password must contain at least one number")
    valid = False

if valid:
    print("Password is valid")
