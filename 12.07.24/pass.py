import random
from string import printable
random.seed()

password = ""

for p in range(32):
    password += random.choice(printable)

print(f"Password: {password}")