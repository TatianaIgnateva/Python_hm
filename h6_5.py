class Stationary:
    def __init__(self, title="титульного листа"):
        self.title = title
    def draw(self):
        print(f"Запуск отрисовки")
class Pan(Stationary):
    def draw(self):
        print(f"Рисуем набросок {self.title} ручкой")

class Pencil(Stationary):
    def draw(self):
        print(f"Рисуем набросок {self.title} карандашом")

class Handle(Stationary):
    def draw(self):
        print(f"Рисуем набросок {self.title} маркером")

stationary = Stationary()
stationary.draw()
pan = Pan()
pan.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
