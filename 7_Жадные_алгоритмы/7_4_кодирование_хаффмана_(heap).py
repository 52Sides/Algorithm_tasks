"""Реализация через heap"""

import heapq
from collections import Counter, namedtuple


# создаем упрощенные классы namedtuple(имя, атрибуты) для узла и листков дерева
class Node(namedtuple("Node", ["left", "right"])):

    def walk(self, code, acc): # метод для класса
        self.left.walk(code, acc + "0") # сначала в левого потомка
        self.right.walk(code, acc + "1") # потом в правого


class Leaf(namedtuple("Leaf", ["char"])):

    def walk(self, code, acc):
        code[self.char] = acc or "0" # записывает в code код символа


def huffman_encode(s):
    h = []

    for ch, freq in Counter(s).items(): # Создаем массив через генератор с 3мя переменными:
        h.append((freq, len(h), Leaf(ch))) # частота, позиция, код

    heapq.heapify(h) # Формируем из массива очередь с приоритетами (кучу - Heap)

    count = len(h)

    while len(h) > 1: # Пока в очереди есть 2 и более элементов
        freq1, _count1, left = heapq.heappop(h) # Достаем элемент с мин частотой
        freq2, _count2, right = heapq.heappop(h) # Достаем элемент с мин частотой

        new_item = (freq1 + freq2, count, Node(left, right))
        heapq.heappush(h, new_item) # Добавляем новый элемент с суммой частот
        count += 1

    code = {}
    if h:
        [(freq, _count, root)] = h
        root.walk(code, "")

    return code


def huffman_decode(encoded, code):
    if not code:
        return ""  # защита от пустой строки

    decode_map = {v: k for k, v in code.items()}
    s = ""
    buffer = ""

    for bit in encoded:
        buffer += bit
        if buffer in decode_map:
            s += decode_map[buffer]
            buffer = ""
    return s



def main():
    s = input()
    code = huffman_encode(s)

    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))

    for ch in code:
        print("{}: {}".format(ch, code[ch]))

    print(encoded)


if __name__ == "__main__":
    main()


def test(n_iter=100):
    import random
    import string

    for i in range(n_iter):
        length = random.randint(0, 32)
        s = "".join(random.choice(string.ascii_letters) for _ in range(length))
        if not s:
            continue  # пропускаем пустые строки

        code = huffman_encode(s)
        encoded = "".join(code[ch] for ch in s)
        decoded = huffman_decode(encoded, code)

        assert decoded == s, f"Ошибка на строке: {s}, decoded={decoded}, code={code}"
