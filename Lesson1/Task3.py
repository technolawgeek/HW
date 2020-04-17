"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.

"""

while True:
    user_num = input('Введите целое число "n":\n')
    if user_num.isdigit():
        user_num = int(user_num)
        break
    else:
        print("Вы ввели не число, попробуйте ещё...")

print('Cумма чисел n + nn + nnn =')
print(user_num + (user_num * 10 + user_num) + (user_num * 100 + user_num * 10 + user_num))
