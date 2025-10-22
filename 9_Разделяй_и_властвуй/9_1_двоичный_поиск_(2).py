"""
Задача: двоичный поиск

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

def find_pos(xs, query):
    # Invariant: lo <= pos <= hi
    lo, hi = 0, len(xs) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if query < xs[mid]:
            hi = mid - 1  # [lo, mid - 1]
        elif query > xs[mid]:
            lo = mid + 1  # [mid + 1, hi]
        else:
            return mid + 1  # 1-based

    return -1


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)

    for query in queries:
        print(find_pos(xs, query), end=' ')


def test():
    assert find_pos([], 42) == -1
    assert find_pos([42], 42) == 1
    assert find_pos([42], 24) == -1


if __name__ == "__main__":
    main()