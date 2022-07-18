# Задание 6:

products = []
data_dict = {'название': '', 'цена': '', 'колличество': '', 'единица измерения': ''}

analytics = {'название': [], 'цена': [], 'колличество': [], 'единица измерения': []}
number = 0
while True:
    if input('Для выхода нажмите Q, для продолжения Enter: ').upper == 'Q':
        break
    number += 1
    for f in data_dict.keys():
        character = input(f'Введите значение {f} - ')
        data_dict[f] = int(character) if f in ('цена', 'колличество') else character
        analytics[f].append(data_dict[f])
    products.append((number, data_dict.copy()))
    print(f'\nСтруктура товаров:\n{products}\n')
    print(f'Всего товаров:')
    for key, value in analytics.items():
        print(f'{key}:{value}')


