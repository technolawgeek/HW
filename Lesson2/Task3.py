"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

season_list = ('зима',
               'весна',
               'лето',
               'осень',
               )

season_dict = {'зима': (12, 1, 2),
               'весна': (3, 4, 5),
               'лето': (6, 7, 8),
               'осень': (9, 10, 11),
               }

while True:
    user_month_num = input('Введите номер номер месяца:\n')
    if user_month_num.isdigit():
        user_month_num = int(user_month_num)
        break
    else:
        print("Вы ввели не число, попробуйте ещё...")

season_idx = user_month_num // 3 % 4

for key, value in season_dict.items():
    if user_month_num in value:
        print (key)
        break

print(season_idx)
print(season_list[season_idx])