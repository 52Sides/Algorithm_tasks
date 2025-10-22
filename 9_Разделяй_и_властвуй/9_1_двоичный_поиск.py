"""
Задача: Двоичный поиск

В первой строке даны целое число 1 ≤ n ≤ 10^5 и массив A[1…n] из n различных
натуральных чисел, не превышающих 10^9, в порядке возрастания, во второй — целое число
1 ≤ k ≤ 10^5 и k натуральных чисел b1, …, bk, не превышающих 10^9.

Для каждого i от 1 до k необходимо вывести индекс 1 ≤ j ≤ n, для которого A[j]=bi,
или −1, если такого j нет.

Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1
"""

import sys

n, *A = map(int, sys.stdin.readline().split())
k, *K = map(int, sys.stdin.readline().split())

for k in K:
    l, r = 0, n - 1

    while l <= r:
        m = int((l + r) / 2)
        if A[m] == k:
            print(m + 1, end=' ')
            break

        elif A[m] > k:
            r = m - 1
        else:
            l = m + 1
    else:
        print(str(-1), end=' ')



