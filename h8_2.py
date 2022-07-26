# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):

    @staticmethod
    def div(a, b):
        pass


print("Деление целых и дробных чисел:")
while True:
    if input("Для выхода из программы нажмите q, для продолжения Enter:  ").lower() == 'q':
        print("Программа завершена.")
        break
    try:
        a = input("1) - ввдите число a   ")
        b = input("2) - ввдите число b   ")

        a, b = float(a), float(b)
        if b == 0:
            raise OwnError("На ноль делить нельзя!")


    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)

    else:
        print(f"{a} / {b} = {round((a / b), 3)}")




