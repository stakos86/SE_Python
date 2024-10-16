import pytest
import random

numbers_list = []

for i in range(50):
    numbers_list.append(str(random.randint(0, 50)) + "\n")

print(numbers_list)

with open('numbers.txt', 'w') as file:
    file.writelines([str(i) + "\n" for i in range(1, 51)])
