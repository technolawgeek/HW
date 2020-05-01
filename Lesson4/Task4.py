"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""

data = [1, 6, 9, 3, 5, 7, 1, 5, 8, 9, 3, 4, 2]
result = [itm for itm in data if data.count(itm) == 1]
print(result)