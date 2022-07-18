from time import sleep
class TrafficLight:
    __color = "Черный"
    def running(self):
        n = 0
        while True:
            print("Зеленый - Движение разрешено.")
            sleep(7)
            print("Желтый - Разрешено завершить маневр.")
            sleep(2)
            print("Красный - Движение запрещено!!!")
            sleep(7)
            n += 1
            if n > 1:
                break

t = TrafficLight()
t.running()

import time
import itertools

class TrafficLight:
    __color = [["Движение разрешено", [7, 32]],["Разрешено завешить маневр", [2, 33]], ["Движение запрещено!", [7, 31]]]
    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])

t = TrafficLight()
t.running()
