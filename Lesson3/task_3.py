"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
a
"""


# hash?

def func(str_obj):
    substrings = []
    for i in range(len(str_obj) - 1):
        substrings.append(str_obj[0:i + 1])
        substrings.append(str_obj[i + 1:])
    print(substrings)
    substrings = set(substrings)
    print(f'Колличество подстрок {len(substrings)}')
    for i in substrings:
        print(hash(i))


func('привет')
