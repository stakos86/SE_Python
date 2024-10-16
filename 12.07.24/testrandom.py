# Создать список из 10 любых чисел, из 10 букв, из 10 слов.
#
# Вывести случайное элемент из каждого из списков описанных выше.

import random
random.seed(1)
numbers: str = '0123456789'
letters: str = 'abcdifghij'
words: list[str] = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

print(random.choice(numbers))
print(random.choice(letters))
print(random.choice(words))
