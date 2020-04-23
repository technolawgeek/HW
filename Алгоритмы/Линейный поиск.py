def array_search(a: list, n: int, x: int):
    """
    Осуществляет поиск числа x в Массиве A
    от 0 до N-1 индекса влючительно.
    Возвращает индекс элемента x в массиве A.
    Или -1 если такого нет.
    Если в массиве

    :param a: массив
    :param n: Длинна
    :param x: искомое число
    :return: Индекс искомого элемента
    """
    for k in range(n):
        if a[k] == x:
            return k
    return -1

a1 = [1, 2, 3, 4, 5]
m = array_search(a1,5,8)
if m == -1:
    print("#test1 - ok")
else:
    print("#test1 - fail")

a2 = [-1, -2, -3, -4, -5]
m = array_search(a2, 5, -3)
if m == 2:
    print("#test2 - ok")
else:
    print("#test2 - fail")

a3 = [10, 20, 30, 10, 10]
m = array_search(a3, 5, 10)
if m == 0:
    print("#test3 - ok")
else:
    print("#test3 - fail")