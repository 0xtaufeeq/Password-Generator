import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/.,-_"

all = lowercase + uppercase + numbers + symbols
length = 12 #Change this number to change the length of your password
password = "".join(random.sample(all,length))
print(password)
