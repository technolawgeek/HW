"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

"""

while True:
    user_time = input("Введите количество секунд:\n")
    if user_time.isdigit():
        user_time = int(user_time)
        break
    else:
        print("Введите цифры, вы ввели что-то другое")


hh = user_time // 3600
mm = (user_time & 3600) // 60
ss = (user_time & 3600) % 60

print (f'{hh:>02}:{mm:>02}:{ss:>02}')