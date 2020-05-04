"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.
"""

import os

file_path1 = os.path.join(os.path.dirname(__file__), 'task4-1.txt')
file_path2 = os.path.join(os.path.dirname(__file__), 'task4-2.txt')
dict1 = {'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'}

file2 = open(file_path2, 'w', encoding='UTF-8')

with open(file_path1, 'r', encoding='UTF-8') as file1:
    for line in file1:
        ent = line.split(' — ')
        ent[0] = dict1[ent[0]]
        string1 = str(ent[0] + ' - ' + ent[1])
        file2.writelines(string1)