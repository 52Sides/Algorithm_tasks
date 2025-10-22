"""
Задача: Обход двоичного дерева.
Построить in-order, pre-order и post-order обходы данного двоичного дерева

In-order(v) обход: произвести рекурсивный вызов для v.left, напечатать v.key,
произвести рекурсивный вызов для v.right.
Pre-order(v) обход: напечатать v.key, произвести рекурсивный вызов для v.left,
произвести рекурсивный вызов для v.right.
Post-order(v): произвести рекурсивный вызов для v.left, произвести рекурсивный вызов
для v.right, напечатать v.key.

Формат входа.
Первая строка содержит число вершин n.
Вершины дерева пронумерованы числами от 0 до n−1.
Вершина 0 является корнем.
Каждая из следующих n строк содержит информацию о вершинах 0, 1, ..., n−1: i-я строка
задаёт числа keyi, lefti и righti, где:
keyi — ключ вершины i,
lefti — индекс левого сына вершины i, а
righti — индекс правого сына вершины i.
Если у вершины i нет одного или обоих сыновей, соответствующее значение равно −1.

Формат выхода.
Три строки: in-order, pre-order и post-order обходы.

Ограничения. 1 ≤ n ≤ 10^5; 0 ≤ keyi ≤ 10^9; −1 ≤ lefti, righti ≤ n − 1.
Гарантируется, что вход задаёт корректное двоичное дерево:
в частности, если lefti 6= −1 и righti 6= −1, то lefti 6= righti;
никакая вершина не является сыном двух вершин; каждая вершина является потомком корня.

Sample Input:
10
0 7 2
10 -1 -1
20 -1 6
30 8 9
40 3 -1
50 -1 -1
60 1 -1
70 5 4
80 -1 -1
90 -1 -1
Sample Output:
50 70 80 30 90 40 0 20 10 60
0 70 50 40 30 80 90 20 60 10
50 80 90 30 40 70 10 60 20 0

Sample Input:
5
4 1 2
2 3 4
5 -1 -1
1 -1 -1
3 -1 -1
Sample Output:
1 2 3 4 5
4 2 1 3 5
1 3 2 5 4
"""

def in_order(i, tree):
    """
    произвести рекурсивный вызов для v.left, напечатать v.key,
    произвести рекурсивный вызов для v.right.
    """
    key, left, right = tree[i]
    if left != -1:
        in_order(left, tree)
    print(key, end=' ')
    if right != -1:
        in_order(right, tree)

def pre_order(i, tree):
    """
    напечатать v.key, произвести рекурсивный вызов для v.left,
    произвести рекурсивный вызов для v.right.
    """
    key, left, right = tree[i]
    print(key, end=' ')
    if left != -1:
        pre_order(left, tree)
    if right != -1:
        pre_order(right, tree)

def post_order(i, tree):
    """
    произвести рекурсивный вызов для v.left,
    произвести рекурсивный вызов для v.right, напечатать v.key.
    """
    key, left, right = tree[i]
    if left != -1:
        post_order(left, tree)
    if right != -1:
        post_order(right, tree)
    print(key, end=' ')

tree = []

for i in range(int(input())):
    tree += [list(map(int, input().split()))]

in_order(0, tree)
print()
pre_order(0, tree)
print()
post_order(0, tree)



