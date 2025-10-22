"""
Задача: Автоматический анализ программ.
При автоматическом анализе программ возникает такая задача.
Система равенств и неравенств.
Проверить, можно ли присвоить переменным целые значения, чтобы выполнить заданные
равенства вида xi = xj и неравенства вида xp != xq.

Формат входа.
Первая строка содержит числа n, e, d. Каждая из следующих e строк содержит два числа
i и j и задаёт равенство xi = xj.
Каждая из следующих d строк содержит два числа i и j и задаёт неравенство xi != xj.
Переменные индексируются с 1: x1, ..., xn.

Формат выхода.
Выведите 1, если переменным x1, ..., xn можно присвоить целые значения, чтобы все
равенства и неравенства выполнились. В противном случае выведите 0.

Ограничения.
1 ≤ n ≤ 10^5;
0 ≤ e, d;
e + d ≤ 2 * 10^5;
1 ≤ i, j ≤ n.

Sample Input 1:
4 6 0
1 2
1 3
1 4
2 3
2 4
3 4
Sample Output 1:
1

Sample Input 2:
4 6 1
1 2
1 3
1 4
2 3
2 4
3 4
1 2
Sample Output 2:
0

Sample Input 3:
4 0 6
1 2
1 3
1 4
2 3
2 4
3 4
Sample Output 3:
1
"""

from sys import setrecursionlimit

setrecursionlimit(10000)

def find(i):
    if i != parent[i]:
        parent[i] = find(parent[i])
    return parent[i]


def union(i, j):
    i_id, j_id = find(i), find(j)
    parent[j_id] = i_id


n, e, d = map(int, input().split())
parent = [i for i in range(n)]
answer = 1

for equal in range(e):
    i, j = map(int, input().split())
    union(i - 1, j - 1)

for non_equal in range(d):
    i, j = map(int, input().split())
    if find(i - 1) == find(j - 1):
        answer = 0
        break

print(answer)