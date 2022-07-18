
def div(arg_1, arg_2):
    try:
        arg_1, arg_2 = int(arg_1), int(arg_2)
        div_result = arg_1 / arg_2
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return round(div_result, 2)

print(div(input('Введите число a: '), input('Введите число b: ')))




