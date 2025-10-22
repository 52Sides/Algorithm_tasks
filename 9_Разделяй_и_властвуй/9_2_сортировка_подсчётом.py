"""
Задача: Сортировка подсчётом.

Первая строка содержит число 1 ≤ n ≤ 10^4,
вторая — n натуральных чисел, не превышающих 10.
Выведите упорядоченную по неубыванию последовательность этих чисел.

Sample Input:
5
2 3 9 2 9
Sample Output:
2 2 3 9 9
"""

def countsort(A):
    B = [0] * 11
    C = [0] * a

    for j in range(a):
        B[A[j]] += 1

    for i in range(1, 11):
        B[i] += B[i - 1]

    for j in range(a - 1, -1, -1):
        C[B[A[j]] - 1] = A[j]
        B[A[j]] -= 1

    return C


import sys

a, *A = map(int, sys.stdin.read().split())

print(*countsort(A))