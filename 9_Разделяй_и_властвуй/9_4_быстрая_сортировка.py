"""
Задача: Точки и отрезки

В первой строке задано два целых числа 1 ≤ n ≤ 50000 и 1 ≤ m ≤ 50000 — количество
отрезков и точек на прямой, соответственно. Следующие n строк содержат по два целых
числа ai и bi (ai ≤ bi) — координаты концов отрезков.
Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают
10^8 по модулю. Точка считается принадлежащей отрезку, если она находится внутри него
или на границе. Для каждой точки в порядке появления во вводе выведите, скольким
отрезкам она принадлежит.

Sample Input:
2 3
0 5
7 10
1 6 11
Sample Output:
1 0 0
"""

def quicksort(a):
    """функция быстрой сортировки с 3мя диапазонами"""
    if len(a) <= 1:
        return a

    import random

    pivot = a[random.randrange(0, len(a))]  # берём cлучайный элемент как опорный

    left_arr = [x for x in a if x < pivot]
    center = [x for x in a if x == pivot]
    right_arr = [x for x in a if x > pivot]

    return quicksort(left_arr) + center + quicksort(right_arr)


def binarysearch(left, right, a, i):
    """
    функция бинарного поиска кол-ва значений в списке
    проверяем вхождения <= для левой части
    """
    c_left, l, r = 0, 0, a - 1

    while l <= r:
        m = int((l + r) / 2)

        if left[m] <= i:
            c_left = m + 1
            l = m + 1
        elif left[m] > i:
            r = m - 1

    #  проверяем вхождения < для правой части
    c_right, l, r = 0, 0, a - 1

    while l <= r:
        m = int((l + r) / 2)

        if right[m] < i:
            c_right = m + 1
            l = m + 1
        elif right[m] >= i:
            r = m - 1

    return c_left - c_right


import sys

#  ввод данных
a, b = map(int, sys.stdin.readline().split())
lines = [list(map(int, sys.stdin.readline().split())) for i in range(a)]
points = list(map(int, sys.stdin.readline().split()))

#  сортируем левые и правые концы отрезков
left = quicksort([i[0] for i in lines])
right = quicksort([i[1] for i in lines])

#  вывод значений
for i in points:
    print(binarysearch(left, right, a, i), end=' ')





