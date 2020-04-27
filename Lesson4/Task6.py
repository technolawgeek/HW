"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка,
определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from sys import argv
from itertools import count
from itertools import cycle

_name, number_or_list = argv

# тестовые переменные
# number = 10
# list = range(1, 11)

#скрипт №1
for i in count(number_or_list):
    print(i)

#скрипт №2
for i in cycle(number_or_list):
    print(i)


