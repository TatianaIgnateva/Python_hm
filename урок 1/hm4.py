
number_in_list = int(input('Введите целое положительное число '))
maximum = number_in_list % 10  # отрываем последнее число, делаем его максимальным
number = number_in_list        # создаем переменную для работы с циклом

while number > 0:
    digit = number % 10
    if digit > maximum:
        maximum = digit

    if digit == 9:
        break

    number = number // 10
print(f'Наибольшая цифра в числе {number_in_list} равна: {maximum}')

