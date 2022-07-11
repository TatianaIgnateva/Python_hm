def generator(number):
    n = 1
    if number == 0:
        yield f'Факториал числа {number} равен: 1'
    for i in range(1, number + 1):                    # (для меня) range не путать с randint
        n *= i
        yield f'Факториал числа {i} равен: {n}'

for el in generator(int(input('Введите факториал какого числа вы хотите найти '))):
    print(el)
