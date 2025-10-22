"""
Задача: структура данных Rope
Ваша цель в данной задаче — реализовать структуру данных Rope.
Данная структура данных хранит строку и позволяет эффективно вырезать кусок строки и
переставить его в другое место.

Формат входа.
Первая строка содержит исходную строку S, вторая — число запросов q.
Каждая из последующих q строк задаёт запрос тройкой чисел i, j, k и означает следующее:
вырезать подстроку S[i..j] (где i и j индексируются с нуля) и вставить её после k-го
символа оставшейся строки (где k индексируется с единицы), при этом если k = 0, то
вставить вырезанный кусок надо в начало.

Формат выхода.
Выведите полученную (после всех q запросов) строку.

Ограничения.
S содержит только буквы латинского алфавита.
1 ≤ |S| ≤ 300 000;
1 ≤ q ≤ 100 000;
0 ≤ i ≤ j ≤ n−1;
0 ≤ k ≤ n − (j − i + 1).

Вход:
hlelowrold
2
1 1 2
6 6 7
Выход:
helloworld
hlelowrold → hellowrold → helloworld

Вход:
abcdef
2
0 1 1
4 5 0
Выход:
efcabd
abcdef → cabdef → efcabd
"""

class Node:

    def __init__(self, s, left=None, right=None, parent=None):
        self.s = s
        self.left = None
        self.right = None
        self.parent = None
        self.size = len(s)
        self.update()


    def update(self):
        self.size = len(self.s)

        if self.left:
            self.left.parent = self
            self.size += self.left.size

        if self.right:
            self.right.parent = self
            self.size += self.right.size


def get_size(v):
    return v.size if v else 0


def split(node, index):
    if not node:
        return None, None

    if index <= get_size(node.left):
        left, right = split(node.left, index)
        node.left = right
        node.update()
        return left, node

    elif index > get_size(node.left) + len(node.s):
        left, right = split(node.right, index - get_size(node.left) - len(node.s))
        node.right = left
        node.update()
        return node, right

    else:
        # Делим строку внутри узла
        cut_point = index - get_size(node.left)
        left_node = Node(node.s[:cut_point], node.left, None)
        right_node = Node(node.s[cut_point:], None, node.right)
        left_node.update()
        right_node.update()
        return left_node, right_node


def merge(left, right):
    if not left or not right:
        return left or right

    # Найдём самый правый в левом
    node = left

    while node.right:
        node = node.right

    splay(node)
    node.right = right
    node.update()
    return node


def splay(node):
    while node.parent:
        p = node.parent
        gp = p.parent

        if gp:
            zigzig(node) if (gp.left == p) == (p.left == node) else zigzag(node)
        else:
            zig(node)


def zig(node):
    p = node.parent

    if p.left == node:
        rotate_right(p)
    else:
        rotate_left(p)


def zigzig(node):
    p = node.parent
    gp = p.parent
    zig(p)
    zig(node)


def zigzag(node):
    zig(node)
    zig(node)


def rotate_left(p):
    q = p.right
    if not q:
        return

    p.right = q.left

    if q.left:
        q.left.parent = p

    q.left = p
    q.parent = p.parent

    if p.parent:
        if p.parent.left == p:
            p.parent.left = q
        else:
            p.parent.right = q

    p.parent = q
    p.update()
    q.update()


def rotate_right(p):
    q = p.left
    if not q:
        return

    p.left = q.right

    if q.right:
        q.right.parent = p

    q.right = p
    q.parent = p.parent

    if p.parent:
        if p.parent.left == p:
            p.parent.left = q
        else:
            p.parent.right = q

    p.parent = q
    p.update()
    q.update()


def inorder(node):
    if not node:
        return ''

    return inorder(node.left) + node.s + inorder(node.right)


def process_rope(s, queries):
    root = Node(s)

    for i, j, k in queries:
        # для i
        left, mid_right = split(root, i)
        mid, right = split(mid_right, j - i + 1)
        root = merge(left, right)

        # для k
        left, right = split(root, k)
        root = merge(merge(left, mid), right)

    return inorder(root)


s = input().strip()
q = int(input())
print(process_rope(s, [tuple(map(int, input().split())) for _ in range(q)]))


"""
import sys

# Чтение входных данных
input = sys.stdin.read
data = input().split()
s = data[0]
q = int(data[1])
idx = 2

for _ in range(q):
    i, j, k = map(int, data[idx:idx+3])
    idx += 3

    cut = s[i:j+1]           # Вырезаем подстроку
    rest = s[:i] + s[j+1:]   # Остаток строки без вырезанного

    # Вставляем после k-го символа (k индексируется с 1, значит вставка после позиции k-1)
    s = rest[:k] + cut + rest[k:]

# Вывод результата
print(s)
"""