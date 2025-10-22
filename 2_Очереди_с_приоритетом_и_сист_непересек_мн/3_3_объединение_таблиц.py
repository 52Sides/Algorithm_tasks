"""
Задача: Объединение таблиц
Ваша цель в данной задаче — реализовать симуляцию объединения таблиц в базе данных.
В базе данных есть n таблиц, пронумерованных от 1 до n, над одним и тем же множеством
столбцов (атрибутов). Каждая таблица содержит либо реальные записи в таблице, либо
символьную ссылку на другую таблицу. Изначально все таблицы содержат реальные записи,
и i-я таблица содержит ri записей. Ваша цель — обработать m запросов типа
(destinationi, sourcei):

Формат входа.
Первая строка содержит числа n и m — число таблиц и число запросов, соответственно.
Вторая строка содержит n целых чисел r1, ..., rn — размеры таблиц.
Каждая из последующих m строк содержит два номера таблиц destinationi и sourcei,
которые необходимо объединить.

Формат выхода.
Для каждого из m запросов выведите максимальный размер таблицы после соответствующего
объединения.

Ограничения.
1 ≤ n, m ≤ 100 000;
0 ≤ ri ≤ 10 000;
1 ≤ destinationi, sourcei ≤ n.

Sample Input:
5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3
Sample Output:
2
2
3
5
5
"""

def find(i):
    if i != parent[i]:
        parent[i] = find(parent[i])
    return parent[i]


def union(dest, source):
    global max_size

    dest_id = find(dest)
    source_id = find(source)

    if dest_id != source_id:
        size[dest_id] += size[source_id]

        if size[dest_id] > max_size:
            max_size = size[dest_id]

        parent[source_id] = parent[dest_id]

    print(max_size)


n, m = map(int, input().split())
size = [int(i) for i in input().split()]
parent = [i for i in range(len(size))]
max_size = max(size)

for i in range(m):
    dest, source = map(int, input().split())
    union(dest - 1, source - 1)

    print(size)
    print(parent)












