"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
from timeit import timeit

dct_obj = {'a': 1, 'b': 2, 'c': 3}
order_dct_obj = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print('Взятие значения из обычного словаря',
      timeit('dct_obj["a"]', globals=globals()))

print('Взятие значения из OrderedDict словаря',
      timeit('order_dct_obj["a"]', globals=globals()))


# Время одинаковое

def change(obj):
    for i in obj:
        obj[i] = obj[i] + obj[i]


# print('Изменение значения в обычном словаре',
#       timeit('change(dct_obj)', globals=globals(), number=1000000)) # 32 секунды
#
# print('Изменение значения в OrderedDict словаре',
#       timeit('change(order_dct_obj)', globals=globals(), number=1000000)) # 32 секунды


# Время одинаковое

dct_obj_1 = {'1': 1, '2': 2, '3': 3}
order_dct_obj_1 = collections.OrderedDict([('1', 1), ('2', 2), ('3', 3)])
lst_obj = [1, 2, 3]


def search_in_dct(obj):
    for i in lst_obj:
        if i in obj.values() and str(i) in obj:
            dct_obj[i] = str(i)


print('Поиск в обычном словаре',
      timeit('search_in_dct(dct_obj_1)', globals=globals()))

print('Поиск в OrderedDict словаре',
      timeit('search_in_dct(order_dct_obj_1)', globals=globals()))


# Как написано в документации время работы всех методов такое же, как и у обычных словарей.
# Замерим время работы особокго метода


def move_to_end_dct(key):
    val = dct_obj_1[key]
    dct_obj_1.pop(key)
    dct_obj_1[key] = val


print('move_to_end в обычном словаре',
      timeit('move_to_end_dct("1")', globals=globals(), number=10000000))

print('move_to_end в OrderedDict словаре',
      timeit('order_dct_obj_1.move_to_end("1")', globals=globals(), number=10000000))

# особый метод в OrderedDict намного быстрее
# OrderedDict есть смысл использовать только если вам нужен функционал его специального метода
