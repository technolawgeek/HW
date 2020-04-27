"""
Реализовать формирование списка, используя функцию range() и возможности
генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce().
"""
from functools import reduce

data = [i for i in range(10, 1001) if (i % 2) == 0]
print(data)
mult_all = reduce(lambda a, b: a * b, data)
print(mult_all)
length = len(str(mult_all))
print(length)
