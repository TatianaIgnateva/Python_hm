class OfficeEquipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.unit = {'Устройство': self.name, 'Цена': self.price, 'Колличество': self.quantity}

    def income(self):
        try:
            unin_n = input(f'Введите наименование устройства ')
            unin_p = int(input(f'Введите цену '))
            unin_q = int(input(f'Введите колличество '))

            item = {'Устройство': self.name, 'Цена': self.price, 'Колличество': self.quantity}
            self.unit.update(item)
            self.my_store.append(self.unit)
            print(f' Текущий список - {self.my_store}')
        except ValueError:
            return('Неверный ввод!')

        ex = input(f" 'q' - для выхода, Enter - продолжить").lower()
        if ex == 'q':
            self.my_store_full.append(self.my_store)
            print(f'На складе -\n{self.my_store_full}')
            return f'Выход'
        else:
            return OfficeEquipment.income(self)

class Printer(OfficeEquipment):
    pass

class Scanner(OfficeEquipment):
    pass

class Xerox(OfficeEquipment):
    pass


#p = Printer('0', 0, 0)  # неверный ввод
s = Scanner('uuu', 3456, 34)
x = Xerox('ttt', 3456, 34)

#print(p.income())
print(s.income())
print(x.income())
