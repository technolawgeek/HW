"""
Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует
пустая строка.
"""


import os

file_path = os.path.join(os.path.dirname(__file__), 'task1.txt')

with open(file_path, 'a', encoding='UTF-8') as file1:
    while True:
        user_data = input('Введите данные:\n')
        if not user_data:
            break
        file1.write(f'{user_data}\n')