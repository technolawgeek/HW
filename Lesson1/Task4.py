"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.

"""
while True:
    user_num = input('Введите целое число:\n')
    if user_num.isdigit():
        user_num = int(user_num)
        break
    else:
        print("Вы ввели не число, попробуйте ещё...")

result = 0
while user_num:
    tnp = user_num % 10
    if tnp > result:
        result = tnp
    if result ==  9:
        break
    user_num //= 10

print(result)
