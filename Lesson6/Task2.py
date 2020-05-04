"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны
передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна. Использовать формулу: длинаширинамасса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
толщины полотна. Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self):
        massa1 = int(self._length) * int(self._width) * 25 * 5
        return massa1, 'кг'

m4 = Road (20000, 6)
print(m4.massa())

