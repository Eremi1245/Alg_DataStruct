"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import hashlib
from uuid import uuid4


class HashTable:
    def __init__(self):
        self.hsh_table = {}
        self.salt = uuid4().hex

    def add(self, url):
        hash_obj = hashlib.sha256(self.salt.encode() + url.encode())
        hex_dig_res = hash_obj.hexdigest()
        if hex_dig_res not in self.hsh_table.values():
            self.hsh_table[len(self.hsh_table)] = hex_dig_res
            print(f'ulr {url} добавлен')
        else:
            print('Такая страница уже есть в кэше')

    def view_ulr(self):
        print(self.hsh_table)


kash = HashTable()
kash.add('https://ru.wikipedia.org/')
kash.add('https://www.youtube.com/')
kash.add('https://www.codewars.com/')
kash.add('https://docs.python.org/')
kash.add('https://yandex.ru/')
kash.add('https://www.youtube.com/')
kash.view_ulr()
