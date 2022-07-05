#1
def my_func(x, y):
    x, y = float(x), int(y)
    result = x ** y
    return result

print(my_func(0.5, -2))

#2

def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "x олжен быть больше 0, а y меньше 0"
        else:
            result = 1
            for i in range(abs(y)):
                result *= 1 / x
            return f'Pезультат возведения х в степень у равно: {round(result, 4)}'
    except ValueError:
        return 'Программа работает только с числами'

print(my_func(0.5, -2))




