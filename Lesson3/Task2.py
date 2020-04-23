"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
"""

def greeting():
    print ("Hi, please enter the following data")
    name = input("Your name?\n")
    surname = input("Your surname?\n")
    date_of_birth = input("Your date of birth?\n")
    city = input("Your hometown?\n")
    email = input("Your email?\n")
    phone = input("Your phone number?\n")

    return print(f'Ok now please check the data\n'
                 f'Name: {name}\n'
                 f'Surname: {surname}\n'
                 f'Date of birth: {date_of_birth}\n'
                 f'Hometown: {city}\n'
                 f'E-mail: {email}\n'
                 f'Phone number: {phone}\n')
greeting()