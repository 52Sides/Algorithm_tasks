"""
Задача: Максимум в скользящем окне.
Найти максимум в каждом окне размера m данного массива чисел A[1 ... n].

Формат входа.
Первая строка входа содержит число n, вторая — массив A[1 ... n], третья — число m.

Формат выхода.
n − m + 1 максимумов, разделённых пробелами.

Ограничения. 1 ≤ n ≤ 10^5, 1 ≤ m ≤ n, 0 ≤ A[i] ≤ 10^5 для всех 1 ≤ i ≤ n.

Наивный способ решить данную задачу — честно просканировать каждое окно и найти в нём
максимум. Время работы такого алгоритма — O(nm). Ваша задача — реализовать алгоритм со
временем работы O(n).

Sample Input 1:
3
2 1 5
1
Sample Output 1:
2 1 5

Sample Input 2:
8
2 7 3 1 5 2 6 2
4
Sample Output 2:
7 7 5 6 6
"""

import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
a, m = data[1:data[0] + 1], data[-1]
stack_in, stack_out = deque(), deque()

for i in a:
    stack_in.append([i, max(i, 0 if len(stack_in) == 0 else stack_in[-1][1])])

    if len(stack_in) + len(stack_out) == m:
        if len(stack_out) == 0:
            while stack_in:
                x = stack_in.pop()
                stack_out.append(
                    [x[0], max(x[0], 0 if len(stack_out) == 0 else stack_out[-1][1])]
                )

        print(
            max(stack_out[-1][1], 0 if len(stack_in) == 0 else stack_in[-1][1]),
            end=' '
        )
        stack_out.pop()






