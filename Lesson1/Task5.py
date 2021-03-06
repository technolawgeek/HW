"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность
сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

"""

while True:
    income = input("Введите размер вашей выручки:\n")
    if income.isdigit():
        income = int(income)
        break
    else:
        print("Введите цифры, вы ввели что-то другое")

while True:
    outcome = input("Введите размер ваших исдержкек:\n")
    if outcome.isdigit():
        outcome = int(outcome)
        break
    else:
        print("Введите цифры, вы ввели что-то другое")


if income >= outcome:
    print("Ваш бизнес приносит прибыль")
    num_of_workers = input("Сколько у вас сотрдников:\n")
    while True:
        if num_of_workers.isdigit():
            num_of_workers = int(num_of_workers)
            break
        else:
            print("Введите цифры, вы ввели что-то другое")
    print("Рентабельность вашей выручки составляет: ", (income - outcome) / income * 100)
    print("Прибыль на каждого сотрудника составит (пр/1 чел):", (income - outcome) / num_of_workers)
else:
    print("Вы работаете с убытком")
