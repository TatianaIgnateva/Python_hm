number = 0
try:
    while number != 'q':
        for i in map(int, input('Введите числа через пробел или наберите q для выхода: ').split()):
            number += i
        print(number)

except ValueError:
    print(number)

