"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

from time import time
from functools import wraps


def time_decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        res_func = func(*args, **kwargs)
        end = time()
        result_time = end - start
        print(f'Время исполнения: {result_time}')
        return res_func

    return wrapper


@time_decor
def completion_list(n):
    lst_obj = [x for x in range(n)]
    return lst_obj


@time_decor
def completion_dict(n):
    dct_obj = {}
    for i in range(n):
        dct_obj[i] = i
    return dct_obj


@time_decor
def action_with_list(lst_obj):
    lst_obj_2 = []
    for i in range(len(lst_obj)):
        lst_obj_2.append(lst_obj[i])
    return lst_obj_2


@time_decor
def action_with_dict(dct_obj):
    lst_obj_2 = []
    for i in dct_obj:
        lst_obj_2.append(dct_obj[i])
    return lst_obj_2


@time_decor
def search_with_list(lst_obj):
    for i in range(len(lst_obj)):
        if lst_obj[i] in lst_obj:
            lst_obj[i] = i + 1
    return lst_obj


@time_decor
def search_with_dict(dct_obj):
    for i in dct_obj:
        if i in dct_obj:
            dct_obj[i] = i + 1
    return dct_obj


lst_obj = completion_list(100000)  # 0,003секунды

dct_obj = completion_dict(100000)  # 0,008 секунд

action_with_list(lst_obj)  # 0,008 секунд

action_with_dict(dct_obj)  # 0,006 секунд

# search_with_list(lst_obj)  # 53 секунды, лучше не пробовать

search_with_dict(dct_obj)  # 0,007 секунд

# В первом задании список заполняется быстрее, потому что для словаря python'у еще необходимо посчитать хеш каждого
# ключа.
# Замена в словаре и списке происходит одинаково
# Поиск в словаре происходит намного быстрее, так как пайтон уже знает по индексу где лежит значение
