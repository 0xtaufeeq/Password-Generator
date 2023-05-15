# Password-Generator
Generate a 12 digit strong password to keep you credentials safe
## Code

```py
import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/.,-_"

all = lowercase + uppercase + numbers + symbols
length = int(input("Enter the length of the password - "))
password = "".join(random.sample(all,length))
print(password)
