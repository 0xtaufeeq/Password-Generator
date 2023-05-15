import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/.,-_"

length = int(input("Enter the length of the password: "))
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
include_numbers = input("Include numbers? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

all = ""
if include_lowercase:
    all += lowercase
if include_uppercase:
    all += uppercase
if include_numbers:
    all += numbers
if include_symbols:
    all += symbols

if not all:
    print("You must select at least one character type.")
else:
    num_passwords = int(input("Enter the number of passwords to generate: "))

    for _ in range(num_passwords):
        password = "".join(random.sample(all, length))
        print(password)
