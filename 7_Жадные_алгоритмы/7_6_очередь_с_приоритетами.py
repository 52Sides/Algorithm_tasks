"""
Задача: очередь с приоритетами

Первая строка входа содержит число операций 1 ≤ n ≤ 10^5.
Каждая из последующих n строк задают операцию одного из следующих двух типов:
Insert x, где 0 ≤ x ≤ 10^9 — целое число;
ExtractMax.

Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает
максимальное число и выводит его.

Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax
Sample Output:
200
500
"""

import sys

def sift_UP(heap):
    i = len(heap) - 1

    while heap[int((i - 1) / 2)] < heap[i]:
        heap[int((i -1) / 2)], heap[i] = heap[i], heap[int((i -1) / 2)]
        i = int((i -1) / 2)


def sift_DOWN(heap):
    i = 0

    while i * 2 + 1 < len(heap):
        left = 2 * i + 1
        right = 2 * i + 2

        if right < len(heap) and heap[right] > heap[left]:
            j = right
        else:
            j = left

        if heap[i] >= heap[j]:
            break

        heap[i], heap[j] = heap[j], heap[i]
        i = j


heap = []

for i in range(int(sys.stdin.readline())):
    command = str(sys.stdin.readline())

    if command[0] == 'I':
        heap.append(int(command.strip().split(' ')[1]))

        if len(heap) > 1:
            sift_UP(heap)

    elif command[0] == 'E':
        print(heap[0])

        if len(heap) >= 2:
            heap[0] = heap.pop(len(heap) - 1)
            sift_DOWN(heap)
        else:
            heap = []