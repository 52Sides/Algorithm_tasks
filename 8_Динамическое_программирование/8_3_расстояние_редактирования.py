"""
Задача: Расстояние редактирования

Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2,
содержащих строчные буквы латинского алфавита.

Sample Input 1:
ab
ab
Sample Output 1:
0

Sample Input 2:
short
ports
Sample Output 2:
3
"""


def EditDistBU(a, b):
    n, m = len(a), len(b)
    d = [[int(0) for _ in range(m + 1)] for j in range(n + 1)]

    for i in range(m + 1):
        d[0][i] = i

    for j in range(n + 1):
        d[j][0] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = 0 if a[i - 1] == b[j - 1] else 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + c)

    return d


import sys

reader = map(str, sys.stdin.read().split())
a, b = next(reader), next(reader)

print(EditDistBU(a, b)[-1][-1])

"""
        a  b
    [0, 1, 2]
a   [1, 0, 0]
b   [2, 0, 0]
c   [3, 0, 0]
"""