"""
Создать (программно) текстовый файл, записать в него программно набор
чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел
в файле и выводить ее на экран.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'task5.txt')

with open(file_path, 'w', encoding='UTF-8') as file1:
    while True:
        user_data = input('Введите числа через пробел (если ничего не ввести то запись прекратиться):\n')
        if not user_data:
            break
        file1.write(f'{user_data}\n')

sum = 0
with open(file_path, 'r', encoding='UTF-8') as file1:
    for line in file1:
        ent = line.split(' ')
        for value in ent:
            sum += int(value)

print(sum)