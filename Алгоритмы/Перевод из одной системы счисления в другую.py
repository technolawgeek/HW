base = int(input("Введите максимальное число в выбраной вами системе счисления: "))
number = int(input("Введите число которое вы хотите перевести в выбраную систему счисления: "))

while number > 0:
    digit = number % base
    print(digit, end='')
    number //= base

# необходимо развернуть цифры на выходе!!! допиши как нибудь


