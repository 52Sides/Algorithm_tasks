"""
Задача: Высота дерева
Вычислить высоту данного дерева.

Формат входа.
Первая строка содержит натуральное число n.
Вторая строка содержит n целых чисел parent0, ..., parent_n−1.
Для каждого 0 ≤ i ≤ n−1, parent_i — родитель вершины i; если parent_i = −1, то i
является корнем.

Гарантируется, что корень ровно один. Гарантируется, что данная последовательность
задаёт дерево.

Формат выхода.
Высота дерева. (Ограничения. 1 ≤ n ≤ 10^5)

Вход:
5
4 -1 4 1 1
Выход:
3

Вход:
5
 0 1 2 3 4
-1 0 4 0 3
Выход:
4
"""

import sys

def height(root):
    h = 1
    for i in root:
        if i in d.keys():
            h = max(h, 1 + height(d[i]))

    return h


sys.setrecursionlimit(20000)

n, lst, d = int(input()), list(map(int, input().split())), dict()

for i in range(n):
    if lst[i] in d.keys():
        d[lst[i]].append(i)
    else:
        d[lst[i]] = [i]

print(height(d[-1]))