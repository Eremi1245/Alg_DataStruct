"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""

import timeit
import random
from statistics import median

# print(
#     timeit.timeit(
#         "merge_sort(orig_list[:])",
#         globals=globals(),
#         number=1000))

m = random.randint(1, 100)


# orig_list = [random.randint(-100, 100) for _ in range(2*m+1)]

def func_1(lst_obj):
    left = []
    right = []
    middle = -1  # переменная для подсчета равных по значению элементов, -1 - потому что в любом случае будет
    # совпадение с
    # c самим собой
    for i in lst_obj:
        for j in lst_obj:
            if i > j:
                left.append(j)
            elif i < j:
                right.append(j)
            else:
                middle += 1
        if len(left) + middle == len(right) or len(left) == len(right) + middle:
            return i
        left.clear()
        right.clear()
        middle = -1


# if median(orig_list)==func_1(orig_list):
#     print(f'm={m}, Медиана : {func_1(orig_list)}')
# else:
#     print('Неправильно')

# orig_list_2 = [random.randint(-100, 100) for _ in range(2*m+1)]


def func_2(lst_obj):
    for i in range(len(lst_obj) // 2):
        del lst_obj[lst_obj.index(max(lst_obj))]
    return max(lst_obj)


# if median(orig_list_2)==func_2(orig_list_2[:]):
#     print(f'm={m}, Медиана : {func_2(orig_list_2[:])}')
# else:
#     print('Неправильно')

# замеры 10 элементов - 0.0070 сек, 100 элементов - 0.1568 секунд, 1000 элементов - 68.12
# m=5
orig_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]

print(
    timeit.timeit(
        "func_1(orig_list)",
        globals=globals(),
        number=1000))
# замеры 10 элементов - 0.0021 сек, 100 элементов - 0.0778 секунд, 1000 элементов - 6.56
print(
    timeit.timeit(
        "func_2(orig_list[:])",
        globals=globals(),
        number=1000))
# замеры 10 элементов - 0.0004 сек, 100 элементов - 0.0028 секунд, 1000 элементов - 0.0804
print(
    timeit.timeit(
        "median(orig_list)",
        globals=globals(),
        number=1000))

# Второй вариант нахождения медианы(удалением наибольших чисел) быстрее чем первый. встроеная фукция median ожидаемо
# лучше остальных
