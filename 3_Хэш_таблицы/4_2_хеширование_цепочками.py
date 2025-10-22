"""
Задача: Хеширование цепочками.
Хеширование цепочками — один из наиболее популярных методов реализации хеш-таблиц на
практике. Ваша цель в данной задаче — реализовать такую схему, используя таблицу с m
ячейками и полиномиальной хеш-функцией на строках.
h(S) = (sum i from 0 to |S| - 1(S|i|*x^2 mod p) mod m, где
S[i] — ASCII-код i-го символа строки S,
p = 1 000 000 007 — простое число,
x = 263.

Ваша программа должна поддерживать следующие типы запросов:
• add string: добавить строку string в таблицу.
              Если такая строка уже есть, проигнорировать запрос;
• del string: удалить строку string из таблицы.
              Если такой строки нет, проигнорировать запрос;
• find string: вывести «yes» или «no» в зависимости от того,
               есть в таблице строка string или нет;
• check i: вывести i-й список (используя пробел в качестве разделителя);
           если i-й список пуст, вывести пустую строку.
При добавлении строки в цепочку, строка должна добавляться в начало цепочки.

Формат входа.
Первая строка размер хеш-таблицы m. Следующая строка содержит количество запросов n.
Каждая из последующих n строк содержит запрос одного из перечисленных выше четырёх типов.

Формат выхода.
Для каждого из запросов типа find и check выведите результат в отдельной строке.

Ограничения.
1 ≤ n ≤ 10^5;
n/5 ≤ m ≤ n.
Все строки имеют длину от одного до пятнадцати и содержат только буквы латинского
алфавита.

Sample Input 1:
5
12
add world
add HellO
check 4
find World
find world
del world
check 4
del HellO
add luck
add GooD
check 2
del good
Sample Output 1:
HellO world
no
yes
HellO
GooD luck

Sample Input 2:
4
8
add test
add test
find test
del test
find test
find Test
add Test
find Test
Sample Output 2:
yes
no
no
yes

ord()
"""

def hsh(stroke):
    p, x, h = 1000000007, 263, 0

    for i, v in enumerate(stroke):
        h = h + ((ord(v) * (x ** i)) % p)

    h = (h % p) % m

    if stroke not in d.keys():
        d[stroke] = h

    return h


def command(task, stroke, lst):
    if task == "add":
        h = d[stroke] if stroke in d else hsh(stroke)
        if stroke not in lst[h]:
            lst[h] = [stroke] + lst[h]

    elif task == "del":
        if stroke in d.keys():
            lst[d[stroke]].remove(stroke)
            del d[stroke]

    elif task == "find":
        print(["no", "yes"][stroke in d])

    elif task == "check":
        print(*lst[int(stroke)])


m, n = int(input()), int(input())
lst, d = [[] for i in range(m)], {}

for i in range(n):
    task, stroke = input().split()
    command(task, stroke, lst)

