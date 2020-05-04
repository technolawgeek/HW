"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'task2.txt')
count = 0

with open(file_path, 'r', encoding='UTF-8') as file1:
    for line in file1:
        count += 1
        print('Это длина строки №', count, '-', len(line))
    print('Всего строк в файле:', count)
