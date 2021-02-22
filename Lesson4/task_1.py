"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


nums = list(range(1000))
print(timeit("func_1(nums)", "from __main__ import func_1,nums", number=10000))

#Чтобы не тратить время на поиск элемента по индексу, мы просто вытаскиваем элементы по очереди, получается быстрее
def func_1(nums):
    new_arr = []
    for i in nums:
        if i % 2 == 0:
            new_arr.append(i)
    return new_arr


nums = list(range(1000))
print(timeit("func_1(nums)", "from __main__ import func_1,nums", number=10000))