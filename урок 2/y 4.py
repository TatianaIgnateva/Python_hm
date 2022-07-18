
# Задание 4:
words = input('Введите слова через пробел: ').split()

for i, word in enumerate(words, 1):
    print(f'{i}) {word[:10]}')

