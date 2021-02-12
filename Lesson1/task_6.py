"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class QueueClass:
    def __init__(self):
        self.elems = []
        self.name='Базовая очередь'

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)
    
    def __str__(self):
    	return f'Это {self.name}, в ней содержаться такие элементы {self.elems}'

class Decided_Queue_Class(QueueClass):
	def __init__(self):
		super(Decided_Queue_Class, self).__init__()
		self.name='Очередь решенных задач'


class Fix_Queue_Class(QueueClass):
	def __init__(self):
		super(Fix_Queue_Class, self).__init__()
		self.name='Очередь задач для доработки'



task_board=[]

queue=QueueClass()
decided_queue=Decided_Queue_Class()
fix_queue=Fix_Queue_Class()
task_board.append(queue)
task_board.append(decided_queue)
task_board.append(fix_queue)


queue.to_queue('Первая задача')
queue.to_queue('Вторая задача')
queue.to_queue('Третья задача')
queue.to_queue('Четвертая задача')
queue.to_queue('Пятая задача')
queue.to_queue('Шестая задача')
queue.to_queue('Седьмая задача')
queue.to_queue('Восьмая задача')
queue.to_queue('Девятая задача')
queue.to_queue('Десятая задача')
queue.to_queue('Одиннадцатая задача')
queue.to_queue('Двенадцатая задача')

decided_queue.to_queue(queue.from_queue())
decided_queue.to_queue(queue.from_queue())
decided_queue.to_queue(queue.from_queue())

fix_queue.to_queue(queue.from_queue())
fix_queue.to_queue(queue.from_queue())
fix_queue.to_queue(queue.from_queue())


for i in task_board:
	print(i)