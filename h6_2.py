class Road:
    def __init__(self, length, width):

        self._length = length
        self._width = width

    def square(self):
        return f'{self._length} м * {self._width} м 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т'
road = Road(5000, 20)
road1 = Road(3000, 20)
print(road.square())
print(road1.square())
