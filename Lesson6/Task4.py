"""
Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go,
stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При
значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните
доступ к атрибутам, выведите результат. Выполните вызов методов и
также покажите результат.
"""


class Car:
    def __init__(self, speed: int = 0, color: str = '', name: str = '', is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        if direction in ('налево', 'навправо'):
            print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Машина едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def name_class(self):
        print("Это городской автомобиль")

    def show_speed(self):
        print(f'Машина едет со скоростью {self.speed} км/ч')
        if self.speed > 60:
            print('Машина едет с превышением скорости')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def name_class(self):
        print("Это спортивный автомобиль")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def name_class(self):
        print("Это рабочий автомобиль")

    def show_speed(self):
        print(f'Машина едет со скоростью {self.speed} км/ч')
        if self.speed > 40:
            print('Машина едет с превышением скорости')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool = True):
        super().__init__(speed, color, name, is_police)

    def name_class(self):
        print("Это полицейский автомобиль")


car1 = TownCar(70, 'blue', 'Rover', False)
car2 = SportCar(120, 'green', 'Mazda', False)
car3 = WorkCar(35, 'grey', 'Toyota', False)
car4 = PoliceCar(80, 'blue', 'VAZ', True)

print(car1)
print(car2)
print(car3)
print(car4)

car1.name_class()
car1.go()
car1.show_speed()
car1.turn('налево')
car1.turn('направо')
car1.stop()


car2.name_class()
car2.go()
car2.show_speed()
car2.turn('налево')
car2.turn('направо')
car2.stop()


car3.name_class()
car3.go()
car3.show_speed()
car3.turn('налево')
car3.turn('направо')
car3.stop()


car4.name_class()
car4.go()
car4.show_speed()
car4.turn('налево')
car4.turn('направо')
car4.stop()


