class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма коммплексных чисел равна - {self.a + other.a} и {self.b + other.b}'

    def __mul__(self, other):
        return f'Произведение комплексных чисел равно - {self.a * other.a} и {self.b * other.b}'

    def __str__(self):
        return f'Комплексное число: {self.a} и {self.b}'

com1 = ComplexNumber(2, 7)
com2 = ComplexNumber(2, 3)

print(com1)
print(com2)
print(com1 + com2)
print(com1 * com2)
