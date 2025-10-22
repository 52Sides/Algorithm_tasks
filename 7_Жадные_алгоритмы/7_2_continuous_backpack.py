"""
Задача: Непрерывный рюкзак

Первая строка содержит количество предметов 1 ≤ n ≤ 10^3 и
вместимость рюкзака 0 ≤ W ≤ 2 * 10^6.
Каждая из следующих n строк задаёт:
стоимость 0 ≤ ci ≤ 2 * 10^6
объём 0 < w i ≤ 2 * 10^6 предмет (n, W, ci, wi — целые числа).

Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить
любую часть, стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30
Sample Output:
180.000
"""

import sys

amount, b_size = map(int, sys.stdin.readline().split())
backpack = [0 for i in range(b_size)]

for _ in range(amount):
    value, size = map(int, sys.stdin.readline().split())
    backpack += (float(value / size) for i in range(size))

backpack = sum(sorted(backpack, reverse=True)[:b_size])
print(f"{backpack:.3f}")