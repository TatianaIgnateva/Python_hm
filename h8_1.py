# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import datetime

class Data:

    def __init__(self, data):
        self.data = data


#    @classmethod
#    def get_data(cls, data):
#        inp_data = [_ for _ in data.split('-')]
#        # return f"{cls, int(inp_data[0])}.{cls, int(inp_data[1])}.{cls, int(inp_data[2])}"
#        return f'Введена дата - {int(inp_data[0])}.{int(inp_data[1])}.{int(inp_data[2])}'

    @classmethod
    def get_data(cls, data):
        print('Далее следует проверка введенных данных: ')
        try:
            day, month, year = [int(_) for _ in data.split('-')]
            return f"Корректные данные. Введена дата - {day}.{month}.{year}."
        except ValueError:
            return f'\nНеверный ввод данных!!'

    @staticmethod
    def validator(day, month, year):
        print('Проверка валидатора: ')
        if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 3000:
            return f"Введена дата - {day}.{month}.{year}. Данные введены корректно."
        else:
            return f"Введена дата - {day}.{month}.{year}. Данные введены Некорректно!!"

    @staticmethod
    def main():
        today = datetime.today()
        print(f'Текущая дата {today.strftime("%d.%b.%Y")}')
    if __name__ == "__main__":
        main()





print(Data.get_data('11 11 1111'))
print(Data.get_data('11-11-1111'))

print(Data.validator(1, 12, 1956))
print(Data.validator(41, 12, 1956))
