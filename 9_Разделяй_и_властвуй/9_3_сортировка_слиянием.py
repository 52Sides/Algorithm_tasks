"""
Задача: Число инверсий

Первая строка содержит число 1 ≤ n ≤ 10^5, вторая — массив A[1…n], содержащий
натуральные числа, не превосходящие 10^9. Необходимо посчитать число пар индексов
1 ≤ i < j ≤ n, для которых A[i] > A[j]. (Такая пара элементов называется инверсией
массива. Количество инверсий в массиве является в некотором смысле его мерой
неупорядоченности: например, в упорядоченном по неубыванию массиве инверсий нет вообще,
а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)

Sample Input:
5
2 3 9 2 9
Sample Output:
2
"""

import sys

def merge(A):
    global count

    if len(A) <= 1:
        return A

    L = merge(A[:len(A) // 2])
    R = merge(A[len(A) // 2:])
    n = m = k = 0
    C = [0] * len(A)

    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            count += len(L) - n
            C[k] = R[m]
            m += 1

        k += 1

    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1

    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1

    for i in range(len(A)):
        A[i] = C[i]

    return A


a, *A = (int(i) for i in sys.stdin.read().split())
count = 0

merge(A)
print(count)
