import random
import sys
from functools import lru_cache

# sys.getrecurionlimit() параметр ограничения кол-ва рекурсий

def edit_distance(s1, s2):
    @lru_cache(maxsize=None)  # мемоизация функции декоратором неогр. размера

    def d(i, j):  # длины двух строк для ктр мы считаем ред. расстояние
        if i == 0 or j == 0:  # случай пустых строк
            return max(i, j)  # тогда ред. расстояние = длине не пустой строки

        else:  # если строки не пусты
            return min(d(i, j - 1) + 1,  # вставка
                       d(i - 1, j) + 1,  # удаление
                       d(i - 1, j - 1) + (s1[i - 1] != s2[j - 1]))  # соотв./не соотв.

    return d(len(s1), len(s2))


def main():
    s1 = input()
    s2 = input()
    print(edit_distance(s1, s2))


def test(n_iter=100):
    for i in range(n_iter):
        length = random.randint(0, 1000)
        s = "".join(random.choice("01") for _ in range(length))

        assert edit_distance(s, "") == edit_distance("", s) == len(s)
        assert edit_distance(s, s) == 0

    assert edit_distance("ab", "ab") == 0
    assert edit_distance("short", "ports") == 3


if __name__ == "__main__":
    sys.setrecursionlimit(10000)  # устанавливаем свой лимит рекурсий
    test()
