"""
Задача: Симуляция обработки сетевых пакетов

Вход.
Размер буфера size и число пакетов n, а также две последовательности
arrival1, ..., arrivaln и duration1, ..., durationn, обозначающих время поступления и
длительность обработки n пакетов.

Выход.
Для каждого из данных n пакетов необходимо вывести время начала его обработки или −1,
если пакет не был обработан (это происходит в случае, когда пакет поступает в момент,
когда в буфере компьютера уже находится size пакетов).

Sample Input 1:
1 0
Sample Output 1:


Sample Input 2:
1 1
0 0
Sample Output 2:
0

Sample Input 3:
1 1
0 1
Sample Output 3:
0
"""

# У нас есть время работы процессора = 0, ктр растет с каждым обработанным пакетом
# Логика: приходит пакет, мы считываем его и добавляем в буфер,
# c временем начала его обработки
# Параллельно есть процессор, который берет себе пакет и обрабатывает его,
# потом берет следующий и т.д.

from collections import deque

size, n = map(int, input().split())
buffer = deque([-1] * size)

for arrival, duration in (map(int, input().split()) for _ in range(n)):
    if arrival < buffer[0]:
        print(-1)
    else:
        print(max(buffer[-1], arrival))
        buffer.append(max(buffer[-1], arrival) + duration)
        buffer.popleft()


# Первая версия
size, n = map(int, input().split())
buffer = deque([-1] * size)

for i in range(n):
    arrival, duration = map(int, input().split())
    if arrival < buffer[0]:
        print(-1)
    else:
        if arrival > buffer[-1]:
            print(arrival)
            buffer.append(arrival + duration)
        else:
            print(buffer[-1])
            buffer.append(buffer[-1] + duration)
        buffer.popleft()











