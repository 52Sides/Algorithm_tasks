"""
Задача: Огромное число Фибоначчи по модулю
Даны целые числа 1 ≤ n ≤ 10^18 и 2 ≤ m ≤ 10^5, необходимо найти остаток от деления n-го
числа Фибоначчи на m.

Sample Input:
10 2
Sample Output:
1
"""

# период остатков от деления Fib на m фиксирован
# n % m = период_остатка[n % len(период_остатка)]

def fib_mod(n, m):
    fib, modm, k = [0, 1], [0, 1], 1

    for i in range(2, n + 1):
        fib.append(fib[i - k] + fib[i - k - 1])
        modm.append(fib[i - k + 1] % m)

        del fib[0]
        k += 1

        if i > 2 and modm[i] == 1 and modm[i - 1] == 0:
            return modm[n % (len(modm) - 2)]

    return modm[-1]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()


# или так
def fib_mod(n, m):
    a, b, modm = 0, 1, []

    for i in range(n + 1):
        modm.append(a)
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            break

    return modm[n % len(modm)]

