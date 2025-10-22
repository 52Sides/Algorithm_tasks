"""
Реализация за O(nlogn)
"""

def LISbottomup(A):
    a = len(A)
    tails, pos, prev = [], [], [-1] * a

    for i in range(a):
        #  upper_bound: Ищем наименьший индекс i такой,
        #  что tails[i] < x (потому что массив невозрастающий)
        l, r = 0, len(tails)

        while l < r:
            m = (l + r) // 2

            if tails[m] < A[i]:
                r = m
            else:
                l = m + 1

        j = l

        # обновляем Tails если нашли лучшее значение или добавляем новое
        if j == len(tails):
            tails.append(A[i])
            pos.append(i)
        else:
            tails[j] = A[i]
            pos[j] = i

        if j > 0:
            prev[i] = pos[j - 1]

    # Восстановление ответа
    lst = []
    k = pos[-1]

    while k != -1:
        lst.append(k + 1)  # +1 для индексации с 1
        k = prev[k]

    return lst[::-1]


import sys

n, *A = map(int, sys.stdin.read().split())

lst = LISbottomup(A)

print(len(lst))
print(*lst)