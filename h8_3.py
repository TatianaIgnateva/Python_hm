
def uuu():
    a = []

    while True:
        try:
            f = int(input('Введите "q" или число для заполнения списка '))
            a.append(f)
            print(a)
            if f == 'q':
                print(f'Ваш список {a}\nВыход') # Не получается вывести эту строку и выполнить выход из программы.
                break
        except ValueError:
            print('Ввод только чисел.')
print(uuu())