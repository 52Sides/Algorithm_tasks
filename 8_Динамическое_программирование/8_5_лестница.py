"""
Задача: Лестница

Даны число 1 ≤ n ≤ 10^2 ступенек лестницы и целые числа −10^4 ≤ a1, …, an ≤ 10^4,
которыми помечены ступеньки. Найдите максимальную сумму, которую можно получить,
идя по лестнице снизу вверх (от нулевой до n-й ступеньки), каждый раз поднимаясь на
одну или две ступеньки.

Sample Input 1:
2
1 2
Sample Output 1:
3

Sample Input 2:
2
2 -1
Sample Output 2:
1

Sample Input 3:
3
-1 2 1
Sample Output 3:
3
"""

import sys

reader = list(map(int, sys.stdin.read().split()))
n, a = reader[0], reader[1:]

dp = [0] * (n + 1)
dp[1] = a[0]

for i in range(2, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2]) + a[i - 1]

print(dp[n])










