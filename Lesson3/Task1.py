"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""

def function1():
    print("Введите числа x и y, в дальнейшем они будут обработаны по формуле x/y и вам выведут результат")

    while True:
        x = input("Введите число x: ")
        if x.isdigit():
            x = int(x)
            break
        else:
            print("Вы ввели не число")

    while True:
        y = input("Введите число y: ")
        if y.isdigit():
            y = int(y)
            break
        else:
            print("Вы ввели не число")

    try:
        c = x / y
    except ZeroDivisionError:
        return print("На ноль делить нельзя, попробуйте ещё"), function1()

    return print(float(c))

function1()