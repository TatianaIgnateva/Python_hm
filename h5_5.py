# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
#    разделённых пробелами.
#    Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('text_5.txt', 'w+', encoding='utf-8') as f:
    numbers = input('Введите числа через пробел - ')
    f.write(numbers)
    numb_list = numbers.split()
    print(f'Сумма введенных чисел равна: {sum(map(int, numb_list))}')


