"""
Задача: наибольшая невозрастающая подпоследовательность

Дано целое число 1 ≤ n ≤ 10^5 и массив A[1…n], содержащий неотрицательные целые числа,
не превосходящие 10^9. Найдите наибольшую невозрастающую подпоследовательность в A.
В первой строке выведите её длину k, во второй — её индексы
1 ≤ i1 < i2 < … < ik ≤ n (таким образом, A[i1] ≥ A[i2] ≥ … ≥ A[in]).

Sample Input:
5
5 3 4 4 2
Sample Output:
4
1 3 4 5
"""

def LISbottomup(A):
    a = len(A)
    D, prev = [1] * a, [-1] * a

    for i in range(a):
        for j in range(i):
            if A[j] >= A[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
                prev[i] = j + 1

    # Восстановление ответа
    lst = []
    lst.append(D.index(max(D)) + 1)
    i = prev[lst[-1] - 1]

    while i >= 0:
        lst.append(i)
        i = prev[lst[-1] - 1]

    return lst[::-1]


import sys

a, *A = map(int, sys.stdin.read().split())

lst = LISbottomup(A)

print(len(lst))
print(*lst)


