
# Задания 4 и 7.
# Задание 4:
        # Пользователь вводит целое положительное число.
        # Найдите самую большую цифру в числе.
        # Для решения используйте цикл while и арифметические операции.


numbers = input('Введите целое положительное число ')
length = len(numbers)  # длинна строки
print('Вы ввели число: ', numbers)

n = 1  # индекс элемента строки
i = numbers[n]
max_number = numbers[0]

while n < length:
    if numbers[n] >= max_number:
        max_number = numbers[n]
        n = n + 1
    else:
        n = n + 1

print('Максимальное число: ', max_number)

# Задание 7.
    # Спортсмен занимается ежедневными пробежками.
    # В первый день его результат составил a километров.
    # Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
    # Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
    # Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
    #Например: a = 2, b = 3.
    #Результат: 1-й день: 2
    #2-й день: 2,2
    #3-й день: 2,42
    #4-й день: 2,66
    #5-й день: 2,93
    #6-й день: 3,22
    # Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

a = int(input('Введите результат 1-го дня в киллометрах: '))
b = int(input('Введите показатель b: '))
n = 1  # номер дня
result = a  # результат первого дня

while result < b:
    print(f'{n}-й день: {result} км.')
    n = n + 1
    result = round((result * 1.1), 2)


print(f'На {n} -й день спортсмен достиг результата - не менее {b} км.')











