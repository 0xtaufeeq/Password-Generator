import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/.,-_"

all = lowercase + uppercase + numbers + symbols
length = int(input("Enter the length of the password - "))
password = "".join(random.sample(all,length))
print(password)
