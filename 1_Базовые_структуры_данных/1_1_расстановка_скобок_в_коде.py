"""
Задача: Расстановка скобок в коде
Проверить, правильно ли расставлены скобки в данном коде.

Формат входа.
Строка s[1...n], состоящая из заглавных и прописных букв латинского алфавита, цифр,
знаков препинания и скобок из множества []{}().

Формат выхода.
Если скобки в s расставлены правильно, выведите строку “Success".
В противном случае выведите индекс (используя индексацию с единицы) первой закрывающей
скобки, для которой нет соответствующей открывающей.
Если такой нет, выведите индекс первой открывающей скобки, для которой нет
соответствующей закрывающей.

Sample Input 1:
([](){([])})
Sample Output 1:
Success

Sample Input 2:
()[]}
Sample Output 2:
5

Sample Input 3:
{{[()]]
Sample Output 3:
7
"""
from collections import deque

def is_balance(s):
    i, k, st = 0, [], deque()

    while i <= len(s) - 1:
        # Debug: print("s[i] = " + str(s[i]) + " st = " + str(st))
        if s[i] in {"(", "[", "{", ")", "]", "}"}:
            if s[i] in {"(", "[", "{"}:
                st.append(s[i])
                k.append(i)

            else:
                if len(st) == 0:
                    return print(i + 1) if k == [] else print(k[-1] + 1)

                if s[i] == ")" and st[-1] != "(":
                    if s[i] == "]" and st[-1] != "[":
                        return print(i + 1)

                    elif s[i] == "}" and st[-1] != "{":
                        return print(i + 1)

                st.pop()
                k.pop()

        i += 1

    return print("Success" if len(st) == 0 else str(k[-1] + 1))


s = str(input())

is_balance(s)
