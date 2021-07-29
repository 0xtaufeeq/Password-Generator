# Password-Generator
Generate a 12 digit strong password to keep you credentials safe
## Code

```import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/.,-_"

all = lowercase + uppercase + numbers + symbols
length = 12
password = "".join(random.sample(all,length))
print(password)
