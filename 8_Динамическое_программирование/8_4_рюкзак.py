"""
Задача: рюкзак

Первая строка входа содержит целые числа 1 ≤ W ≤ 10^4 и 1 ≤ n ≤ 300 — вместимость
рюкзака и число золотых слитков. Следующая строка содержит n целых чисел
0 ≤ w1, …, wn ≤ 10^5, задающих веса слитков. Найдите максимальный вес золота,
который можно унести в рюкзаке.

Sample Input:
10 3
1 4 8
Sample Output:
9
"""

def KnapsackWithoutRepsBU(W, a, c):
    d = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            d[i][w] = d[i-1][w]

            if a[i-1] <= w:
                d[i][w] = max(d[i-1][w], d[i-1][w - a[i-1]] + c[i-1])
    return d


import sys

reader = list(map(int, sys.stdin.read().split()))
W, n, a = reader[0], reader[1], reader[2:]

print(KnapsackWithoutRepsBU(W, a, a)[-1][-1])