"""
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
"""


def sum_of_2_biggest(a:float, b:float, c:float):
    min1 = 0
    if a < b and a < c:
        min1 = a
    elif b < a and b < c:
        min1 = b
    else:
        min1 = c

    return a + b + c - min1


print(sum_of_2_biggest(234, 234, 12))

