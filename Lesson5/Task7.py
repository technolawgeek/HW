"""
Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила
убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json
import os

db1 = os.path.join(os.path.dirname(__file__), 'task7.txt')
db2 = os.path.join(os.path.dirname(__file__), 'task7.json')
db_dict_average = {'average': 0}
db_dict_all = {}

with open(db1, 'r', encoding='UTF-8') as file1:
    for line in file1:
        tmp = line.split(' ')
        profit = int(tmp[2]) - int(tmp[3])
        db_dict_all[tmp[0]] = profit
        if profit < 0:
            continue
        else:
            db_dict_average['average'] += profit
    db_dict_average['average'] = db_dict_average['average'] / len(db_dict_all)
    list = (db_dict_all, db_dict_average)

with open(db2, 'w', encoding='UTF-8') as file2:
    json.dump(list,file2)

print(list)
