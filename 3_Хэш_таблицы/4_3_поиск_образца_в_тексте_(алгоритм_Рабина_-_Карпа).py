"""
Задача: Поиск образца в тексте.
Найти все вхождения строки Pattern в строку Text. Реализуйте алгоритм Карпа–Рабина.

Формат входа.
Образец Pattern и текст Text.

Формат выхода.
Индексы вхождений строки Pattern в строку Text в возрастающем порядке, используя
индексацию с нуля.

Ограничения.
1 ≤ |Pattern| ≤ |Text| ≤ 5 * 10^5.
Суммарная длина всех вхождений образца в текста не превосходит 10^8.
Обе строки содержат буквы латинского алфавита.

Sample Input 1:
aba
abacaba
Sample Output 1:
0 4

Sample Input 2:
Test
testTesttesT
Sample Output 2:
4

Sample Input 3:
aaaaa
baaaaaaa
Sample Output 3:
1 2 3
"""

def RabinKarpHash(pattern, text):

    def hsh(lst, p, x):
        h = 0
        for value in lst:
            h = (h * x + ord(value)) % p
        return h

    p, x = 100000007, 263
    l, i = len(pattern), 0
    res = []

    pattern_hash = hsh(pattern, p, x)
    text_hash = hsh(text[0:l], p, x)

    while i + l - 1 < len(text):
        if text_hash == pattern_hash:
            if text[i:i + l] == pattern:  # на случай коллизии
                res.append(i)

        if i + l < len(text):
            text_hash = ((text_hash - ord(text[i]) * pow(x, l - 1, p)) * x + ord(text[i + l])) % p

        i += 1

    print(*res)


RabinKarpHash(input(), input())