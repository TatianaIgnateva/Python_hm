class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Машина {self.name} (цвет - {self.color}) - машина полицейская - {self.is_police}')

    def go(self):
        print(f'Машина {self.name} поехала')
    def stop(self):
        print(f'Машина {self.name} остановилась')
    def turn(self, direction):
        print(f"Машина {self.name} повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print(f'Скорость автомобиля {self.name}: {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        return f"{self.name}: скорость автомобиля - {self.speed}. Превышение скорости!" \
            if self.speed > 60 else f"{self.name}: скорость автомобиля - {self.speed}."

class Sport(Car):
    pass

class Work(Car):
    def show_speed(self):
        return f'{self.name}: скорость автомобиля - {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f'{self.name}: скорость автомобиля - {self.speed}.'

class PolisCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

p = PolisCar('ДПС', 'белый', 80)
p.go()
s = Sport('Феррари', 'красная', 280)
s.turn(1)
w = Work('Лаз', 'зеленый', 50)
print(w.show_speed())
t = TownCar('Равон', 'желтый', 70)
t.go()
print(t.show_speed())
t.stop()
