"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно
не запрашивать у пользователя, а указать явно, в программе.
"""

list = [1, 2.2, 'hello', False]

for itm in list:
    itm = type(itm)
    print (itm)