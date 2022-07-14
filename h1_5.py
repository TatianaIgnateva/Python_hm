# 1. Создать программный файл в текстовом формате,
#    записать в него построчно данные, вводимые пользователем.
#    Об окончании ввода данных будет свидетельствовать пустая строка.

with open('text.txt', 'w+', encoding='utf-8') as f:
    line = input('Введите строку текста - ')
    while line:
        f.write(f'{line}\n')
        line = input('Введите новую строку - ')
        if not line:
            break
    f.seek(0)
    content = f.read()
    print(content)




