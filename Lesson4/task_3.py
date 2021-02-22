"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from cProfile import run
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# делайте профилировка через cProfile
def main():
    revers_1(123456789)
    revers_2(123456789)
    revers_3(123456789)


run('main()')

# делайте профилировка через timeit
print(timeit("revers_1(123456789)", "from __main__ import revers_1", number=10000))  # 0.018
print(timeit("revers_2(123456789)", "from __main__ import revers_2", number=10000))  # 0.011
print(timeit("revers_3(123456789)", "from __main__ import revers_3", number=10000))  # 0.002

# Cамая быстрая функция revers_3, так как она использует функционал срезов, тоесть просто взятие элементов по индексу
# это происходит быстрее чем цикл в revers_2, в котором на добавление одного символа уходит целых 3 строки кода,
# и намного быстрее, чем  revers_1, где для определения 1 элемента происходит целый новый вызов функции
