"""
Задача: Множество с запросами суммы на отрезке

Реализуйте структуру данных для хранения множества целых чисел, поддерживающую запросы
добавления, удаления, поиска, а также суммы на отрезке.

На вход в данной задаче будет дана последовательность таких запросов.
Чтобы гарантировать, что ваша программа обрабатывает каждый запрос по мере поступления
(то есть онлайн), каждый запрос будет зависеть от результата выполнения одного из
предыдущих запросов. Если бы такой зависимости не было, задачу можно было бы решить
оффлайн: сначала прочитать весь вход и сохранить все запросы в каком-нибудь виде,
а потом прочитать вход ещё раз, параллельно отвечая на запросы.

Формат входа.
Изначально множество пусто. Первая строка содержит число запросов n.
Каждая из n следующих строк содержит запрос в одном из следующих четырёх форматов:
• + i: добавить число f(i) в множество (если оно уже есть, проигнорировать запрос);
• - i: удалить число f(i) из множества (если его нет, проигнорировать запрос);
• ? i: проверить принадлежность числа f(i) множеству;
• s l r: посчитать сумму всех элементов множества, попадающих в отрезок [f(l), f(r)].
Функция f определяется следующим образом.
Пусть s — результат последнего запроса суммы на отрезке
(если таких запросов ещё не было, то s = 0).
Тогда f(x) = (x + s) mod 1 000 000 001.

Формат выхода.
Для каждого запроса типа ? i выведите «Found» или «Not found».
Для каждого запроса суммы выведите сумму всех элементов множества, попадающих
в отрезок [f(l), f(r)].
Гарантируется, что во всех тестах f(l) ≤ f(r).
Ограничения. 1 ≤ n ≤ 10^5; 0 ≤ i ≤ 10^9.

Sample Input:
15
? 1
+ 1
? 1
+ 2
s 1 2
+ 1000000000
? 1000000000
- 1000000000
? 1000000000
s 999999999 1000000000
- 2
? 2
- 0
+ 9
s 0 9
Sample Output:
Not found
Found
3
Found
Not found
1
Not found
10

Sample Input:
5
? 0
+ 0
? 0
- 0
? 0
Sample Output:
Not found
Found
Not found

Sample Input:
5
+ 491572259
? 491572259
? 899375874
s 310971296 877523306
+ 352411209
Sample Output:
Found
Not found
491572259
"""

MOD = 10**9 + 1  # как обычно в задачах

# контейнер данных для каждого узла дерева
class AVLNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # новый узел — лист
        self.size = 1 # размер поддерева
        self.sumv = key # сумма в поддереве


def height(node):
    return node.height if node else 0


def size(node):
    return node.size if node else 0


def sumv(node):
    return node.sumv if node else 0


def update(node):
    if not node:
        return

    node.height = 1 + max(height(node.left), height(node.right))
    node.size = 1 + size(node.left) + size(node.right)
    node.sumv = node.key + sumv(node.left) + sumv(node.right)


def balance_factor(node):
    return height(node.right) - height(node.left)


def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    update(x)
    update(y)
    return y


def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    update(y)
    update(x)
    return x


def balance(node):
    update(node)
    bf = balance_factor(node)

    if bf == 2:
        if balance_factor(node.right) < 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)

    if bf == -2:
        if balance_factor(node.left) > 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)

    return node


# Вставка (add), удаление (remove), поиск (exists):
def insert(node, key):
    if not node:
        return AVLNode(key)

    if key == node.key:
        return node

    elif key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return balance(node)


def find(node, key):
    if not node:
        return False

    if key == node.key:
        return True

    elif key < node.key:
        return find(node.left, key)

    else:
        return find(node.right, key)


def find_min(node):
    while node.left:
        node = node.left
    return node


def remove(node, key):
    if not node:
        return None

    if key < node.key:
        node.left = remove(node.left, key)
    elif key > node.key:
        node.right = remove(node.right, key)
    else:
        # key == node.key
        if not node.left:
            return node.right

        if not node.right:
            return node.left

        min_larger = find_min(node.right)
        node.key = min_larger.key
        node.right = remove(node.right, min_larger.key)

    return balance(node)


# Сумма на отрезке [l, r]
def range_sum(node, l, r):
    if not node:
        return 0

    if node.key < l:
        return range_sum(node.right, l, r)

    if node.key > r:
        return range_sum(node.left, l, r)

    return (node.key + range_sum(node.left, l, r) + range_sum(node.right, l, r))


# Обёртка-класс:
class AVLTree:

    def __init__(self):
        self.root = None


    def add(self, key):
        if not self.exists(key):
            self.root = insert(self.root, key)


    def remove(self, key):
        if self.exists(key):
            self.root = remove(self.root, key)


    def exists(self, key):
        return find(self.root, key)


    def range_sum(self, l, r):
        return range_sum(self.root, l, r)


# Поддержка функции f(i) в основной логике запроса:
tree = AVLTree()
s = 0

for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == '+':
        x = (int(cmd[1]) + s) % MOD
        tree.add(x)
    elif cmd[0] == '-':
        x = (int(cmd[1]) + s) % MOD
        tree.remove(x)
    elif cmd[0] == '?':
        x = (int(cmd[1]) + s) % MOD
        print("Found" if tree.exists(x) else "Not found")
    elif cmd[0] == 's':
        x1 = (int(cmd[1]) + s) % MOD
        x2 = (int(cmd[2]) + s) % MOD
        s_new = tree.range_sum(x1, x2)
        print(s)
        s = s_new % MOD
