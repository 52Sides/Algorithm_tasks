"""
Задача: функция проверки алгоритма на НОД двух чисел
"""

import random

def test(gcd, n_iter=100):  # Greatest Common Divisor
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0,128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0

"""наивный алгоритм для нахождения НОД. минусы: скорость алгоритма"""

def gcd1(a, b):
    assert a >= 0 and b >= 0

    for d in reversed(range(max(a, b) + 1)):  # перебор в обратном порядке
        if d == 0 or a % d == b % d == 0:
            return d

print(gcd1(8, 4))

"""Алгоритм Евклида для НОД"""

def gcd2(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)

"""Рекурсивная версия"""

def gcd3(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)

"""рекурсия версия нативного алгоритма"""

def gcd4(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    return gcd4(b % a, a)