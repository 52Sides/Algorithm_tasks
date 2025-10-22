"""
Задача: Стек с поддержкой максимума
Реализовать стек с поддержкой операций push, pop и max.

Формат входа.
Первая строка содержит число запросов q. Каждая из последующих q строк задаёт запрос
в одном из следующих форматов: push v, pop, or max.

Формат выхода.
Для каждого запроса max выведите (в отдельной строке) текущий максимум на стеке.

Ограничения. 1 ≤ q ≤ 400 000, 0 ≤ v ≤ 100 000.

Стек — абстрактная структура данных, поддерживающая операции push и pop. Несложно
реализовать стек так, чтобы обе эти операции работали за константное время.
В данной задаче ваша цель — расширить интерфейс стека так, чтобы он дополнительно
поддерживал операцию max и при этом чтобы время работы всех операций по-прежнему было
константным.

Sample Input 1:
5
push 2
push 1
max
pop
max
Sample Output 1:
2
2

Sample Input 2:
5
push 1
push 2
max
pop
max
Sample Output 2:
2
1

Sample Input 3:
10
push 2
push 3
push 9
push 7
push 2
max
max
max
pop
max
Sample Output 3:
9
9
9
9
"""

import sys

stack_max = [0]

for i in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack_max.append(max(stack_max[-1], int(command[1])))

    elif command[0] == 'pop':
        stack_max.pop()

    elif command[0] == 'max':
        print(stack_max[-1])
