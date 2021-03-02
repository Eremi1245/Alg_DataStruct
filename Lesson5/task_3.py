"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""
from timeit import timeit
from collections import deque

simple_lst = ['a', 'b', 'c', 'd']
deq_obj = deque(simple_lst)
second_list = ['a', 'b', 'c', 'd']

print('Скорость добавление элемента в начало список',
      timeit('simple_lst.insert(0, "j")', globals=globals(), number=100000))

print('Скорость добавление элемента в начало дека',
      timeit('deq_obj.appendleft("j")', globals=globals(), number=100000))

# Дек быстрее

print('Скорость удаления элемента из начала списка',
      timeit('simple_lst.pop(0)', globals=globals(), number=100000))

print('Скорость удаления элемента из начала дека',
      timeit('deq_obj.popleft()', globals=globals(), number=100000))


# Дек быстрее

def rotat(n):
    for i in range(n):
        s = simple_lst.pop(-1)
        simple_lst.insert(0, s)


rotat(2)

print('Скорость ротации элементов в списке',
      timeit('rotat(2)', globals=globals(), number=10000000))

print('Скорость ротации элементов в деке',
      timeit('deq_obj.rotate(2)', globals=globals(), number=10000000))


# Дек быстрее

def choice(obj):
    for i in range(len(obj)):
        m = obj[i]


print('Скорость выборки элемента из списка',
      timeit('choice(simple_lst)', globals=globals(), number=100000000))  # 33.080153100000004

print('Скорость выборки элемента из дека',
      timeit('choice(deq_obj)', globals=globals(), number=100000000))  # 36.70630270000001

# разница не значительна, скорость равна

# В соответсвии с замерами документация верна, за исключением утвреждения,
# что случайный доступ к элементу быстрее в списке
