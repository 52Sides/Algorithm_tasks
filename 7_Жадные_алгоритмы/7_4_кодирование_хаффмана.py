"""
Задача: Кодирование Хаффмана.

По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского
алфавита, постройте оптимальный беспрефиксный код.
В первой строке выведите количество различных букв k, встречающихся в строке,
и размер получившейся закодированной строки. В следующих k строках запишите коды букв в
формате "letter: code".
В последней строке выведите закодированную строку.

Sample Input 1:
a
Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad
Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
"""

s = input()
lst = [[s.count(i), i] for i in set(s)]

while len(lst) > 1:
    lst = sorted(lst, key=lambda x: x[0])
    left = lst.pop(0)
    right = lst.pop(0)
    lst.append([left[0] + right[0], [left, right]])

if len(set(s)) == 1:
    codes = {s[0]: '0'}
else:
    def f_code(tree, prefix='', codebook=None):
        if codebook is None:
            codebook = {}

        if isinstance(tree[1], str):  # если это лист, например ['a', 1]
            codebook[tree[1]] = prefix
        else:
            f_code(tree[1][0], prefix + '0', codebook)
            f_code(tree[1][1], prefix + '1', codebook)

        return codebook

    codes = f_code(lst[0])

encoded = ''.join(codes[i] for i in s)

print(str(len(set(s))) + ' ' + str(len(encoded)))

for key, value in codes.items():
    print(str(key) + ': ' + str(value))

print(encoded)