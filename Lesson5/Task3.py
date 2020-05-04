"""
Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников
имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'task3.txt')
count = 0
workers_salary = {}
list1 = []

with open(file_path, 'r', encoding='UTF-8') as file1:
    for line in file1:
        ent = line.split()
        workers_salary.update({ent[0]: ent[1]})

for key, value in workers_salary.items():
    if int(value) < 20000:
        list1.append(key)

sum = 0
for value in workers_salary.values():
    sum += int(value)

sum = sum / len(workers_salary)


print('Средняя зарплата сотрудников:', sum)
print('Список сотрудников с зарплатой меньше 20 000 руб.:\n', list1)

