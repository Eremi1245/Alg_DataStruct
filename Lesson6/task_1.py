"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import memory_usage
from time import time as t
from random import randint
from pympler import asizeof


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        t1 = t()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        t2 = t()
        mem_diff = m2[0] - m1[0]
        time_diff = t2 - t1
        print(f'Выполнение заняло {mem_diff} памяти и {time_diff} секунд')
        return res

    return wrapper


@decor
def func_1():
    '''
    Функция имитирует вывод рандомного числа, в зависимости от запроса пользователя. Если пользователю нужно число,
    то есть он вводит "True" функция отдает ему рандомное число, если нет, не отдает ничего
    :users_solutions: решения пользователя
    '''
    users_solutions = [True, True, False, True, True, False, True, True, False, True, True, False, True, True, False,
                       True, True,
                       False, True, True, False, True, True, False, True, True, False, True, True, False, True, True,
                       False, True, True, ]
    list_obj = [randint(-100, 100) for _ in range(1000000)]
    for i in range(len(users_solutions)):
        if users_solutions[i] == True:
            list_obj[i]


# Выполнение заняло 0.984375 памяти и 0.730161190032959 секунд

@decor
def func_1_improved_1():
    users_solutions = [True, True, False, True, True, False, True, True, False, True, True, False, True, True, False,
                       True, True,
                       False, True, True, False, True, True, False, True, True, False, True, True, False, True, True,
                       False, True, True, ]
    list_obj = (randint(-100, 100) for _ in range(10000000))  # заменим список на генератор
    for i in range(len(users_solutions)):
        if users_solutions[i] == True:
            next(list_obj)


# Выполнение заняло 0.0 памяти и 0.1094357967376709 секунд
# func_1()
# func_1_improved_1()
# Генератор в данном случае сводит использование памяти к нулю, потому что интерпретатор не выделяет изначально под
# 10000000 элементов память, как в первом примере

class FIO:
    '''
    Класс имитирует ФИО русского человека, в котором всегда содержаться 3 атрибута имя фамилия, отчетсво
    '''

    def __init__(self, name, second_name, patronymic):
        self.name = name
        self.second_name = second_name
        self.patronymic = patronymic

    def show(self):
        return f'Мое ФИО: {self.second_name} {self.name} {self.patronymic}'


sasha = FIO('Александр', 'Иванов', 'Евгеньевич')
#print(sasha.__dict__)
#print(asizeof.asizeof(sasha))  # 616


class FIO_2:
    __slots__ = ('name', 'second_name', 'patronymic')

    def __init__(self, name, second_name, patronymic):
        self.name = name
        self.second_name = second_name
        self.patronymic = patronymic

    def show(self):
        return f'Мое ФИО: {self.second_name} {self.name} {self.patronymic}'


sasha = FIO_2('Александр', 'Иванов', 'Евгеньевич')
#print(sasha.__slots__)
#print(asizeof.asizeof(sasha))  # 336


# В данном примере применение слотов оправдано. Слоты занимают меньше памяти, так как используют для хранения
# атрибутов списки или кортежи, вместо словарей

def search_div(num):
    '''
    Функция выводит все делители числа
    '''
    divs = [1]
    for i in range(num + 1, 1, -1):
        if num % i == 0:
            divs.append(i)

    return num, divs


@decor
def without_map():
    lst_obj = [i for i in range(10000)]
    result = [search_div(i) for i in lst_obj]


#

@decor
def with_map():
    lst_obj = [i for i in range(10000)]
    result = map(search_div, lst_obj)
    return result


#

#without_map()  # Выполнение заняло 1.5234375 памяти и 2.3441355228424072 секунд
#with_map()  # Выполнение заняло 0.0 памяти и 0.1225271224975586 секунд

#print(asizeof.asizeof(with_map()))  # 48

#print(asizeof.asizeof(list(with_map())))  # 3498120

# Класс map использует память намного экономнее, я не уверен, но мне кажется, что дело в том, что работа map
# схожа с классом генератора, тоесть пока не передашь класс map в другой, например =list(map), map будет
# отображаться как map_object, за счет этого и происходит экономия памяти
