"""
Задача: Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи
(напомним, что F0 = 0 F1 = 0, и Fn = Fn−1 + Fn−2 при n ≥ 2).

Sample Input:
3
Sample Output:
2
"""

def fib(n):
    fib_lst = [1, 1]

    if n <= 2:
        return fib_lst[n-1]

    else: 
        for i in range(2, n+1):
            fib_lst.append(fib_lst[i-1] + fib_lst[i-2])
        return fib_lst[n-1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()