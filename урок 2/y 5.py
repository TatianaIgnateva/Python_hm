my_list = [8, 7, 6, 5, 3, 3, 2]
new_num = int(input('Введите новый элнмент рейтинга: '))
i = 0

for el in my_list:
    if new_num <= el:
        i += 1

    else:
        new_num > el
        break

my_list.insert(i, new_num)
print(my_list)



