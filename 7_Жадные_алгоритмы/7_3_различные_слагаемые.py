"""
Задача: Различные слагаемые.

По данному числу 1 ≤ n ≤ 10^9 найдите максимальное число k, для которого n можно
представить как сумму k различных натуральных слагаемых. Выведите в первой строке
число k, во второй — k слагаемых.

Sample Input 1:
4
Sample Output 1:
2
1 3

Sample Input 2:
6
Sample Output 2:
3
1 2 3
"""

import sys

n = int(sys.stdin.readline())
k, s = [], int()

while n > 0:
    s += 1
    if n - s - (s + 1) >= 0:
        k.append(s)
        n -= s
    else:
        k.append(n)
        break

print(str(len(k)) + '\n' + ' '.join(map(str,k)))