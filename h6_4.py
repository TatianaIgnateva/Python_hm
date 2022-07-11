from itertools import count, cycle
print('Программа генерирует челые числа в указанном диапазоне.')
m = int(input('Введите стартовое число '))
n = int(input('Введите конечное число '))
for i in count(m):
    if i > n:
        break
    else:
        print(i)

print('Программа пронумерует ваш список друзей.')
friends = input('Введите имена друзей через пробел ').split()
print(friends)

n = 1
for i in cycle(friends):
    if n > 9:
        break
    else:
        print(n, i)
        n += 1
