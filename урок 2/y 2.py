numbers = input('Введите числа через пробел: ')
my_list = numbers.split()

for i in range(0, len(my_list), 2):
    my_list.insert(i + 1, my_list.pop(i))


print(my_list)


