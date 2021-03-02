"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple


def creat_firm(name, quarter_1, quarter_2, quarter_3, quarter_4):
    template = namedtuple('Шаблон_Фирмы', 'firm_name quar_1 quar_2 quar_3 quar_4 avg_res')
    firm = template(firm_name=name, quar_1=int(quarter_1), quar_2=int(quarter_2), quar_3=int(quarter_3),
                    quar_4=int(quarter_4),
                    avg_res=(int(quarter_1) + int(quarter_2) + int(quarter_3) + int(quarter_4)) / 4)
    return firm


def function():
    firms = []
    avg_all_firm = []
    num_of_firms = int(input('Введите количество предприятий для расчета прибыли: '))
    for firm in range(num_of_firms):
        firm_name = input('Введите название предприятия: ')
        profit = (input('через пробел введите прибыль данного предприятия'
                        'за каждый квартал(Всего 4 квартала): ')).split(' ')
        firm = creat_firm(firm_name, *profit)
        firms.append(firm)
        avg_all_firm.append(firm.avg_res)
    print(f'Средняя годовая прибыль всех предприятий: {sum(avg_all_firm) / num_of_firms}')
    print(
        f'Предприятия, с прибылью выше среднего значения: '
        f'{",".join([i.firm_name for i in firms if i.avg_res > sum(avg_all_firm) / num_of_firms])}')
    print(
        f'Предприятия, с прибылью ниже среднего значения: '
        f'{",".join([i.firm_name for i in firms if i.avg_res < sum(avg_all_firm) / num_of_firms])}')


function()
