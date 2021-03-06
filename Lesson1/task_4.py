"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

users = {'user1': '1234', 'user2': '1234', 'user3': '1234', 'user4': '1234', 'user5': '1234'}
activ_users = {'user1': 'activated', 'user2': 'non_activated', 'user3': 'activated', 'user4': 'non_activated',
               'user5': 'activated'}


def log_in(user, passw):
    if user in users:  # O(n)
        if users[user] == passw:  # O(1)
            if activ_users[user] == 'activated':  # O(1)
                return 'Вы вошли в систему'  # O(1)
            else:
                return 'Вход в систему запрещен, пройдите процедуру активации'  # O(1)
        else:
            return 'Неверный пароль'  # O(1)

    else:
        return 'Логин/пароль введены неправильно либо вы не зарегистрированны'  # O(1)


# Общая сложность o(n), несмотря на то что 2 входящий аргумента, второй аргумент никак не влияет на сложность функции


db_users = [['user1', '1234', 'activated'], ['user2', '1234', 'non_activated'], ['user3', '1234', 'activated'],
            ['user4', '1234', 'non_activated'], ['user5', '1234', 'activated'], ['user6', '1234', 'non_activated']]


def log_in2(user, passw):
    for i in db_users:  # O(n)
        us = False  # O(1)
        psw = False  # O(1)
        act = False  # O(1)
        for k in i:  # по идее если у нас есть какие то
            # правила по заболнению db_users
            # то K - будет константной o(1), но мы исходим
            # из того что нет определенный правил, так что
            # О(n)
            if user == k:  # O(1)
                us = True  # O(1)
            if passw == k:  # O(1)
                psw = True  # O(1)
            if k == 'activated':  # O(1)
                act = True  # O(1)
        if not us:
            return 'Логин/пароль введены неправильно либо вы не зарегистрированны'  # O(1)
        elif us and not psw:
            return 'Неверный пароль'  # O(1)
        elif us and psw and not act:
            return 'Вход в систему запрещен, пройдите процедуру активации'  # O(1)
        elif us and psw and act:
            return 'Вы вошли в систему'  # O(1)

        # Общая сложность O(log n) так как могут изменяться архитектура db_users, но если считать что db_users
        # подчиняется каким то правилам при формировании будет O(n)


# Сложности одинаковые, первый вариант более компактный


# print(log_in('anton', '1234'))
# print(log_in('user1', '12345'))
# print(log_in('user2', '1234'))
# print(log_in('user1', '1234'))
# print(log_in2('anton', '1234'))
# print(log_in2('user1', '12345'))
# print(log_in2('user2', '1234'))
# print(log_in2('user1', '1234'))
