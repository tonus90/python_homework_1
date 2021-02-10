# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
# speed_print, speed_scan, colorful, type_of_print

from abc import ABC, abstractmethod
from time import sleep, time

class OrgWarehouse():


class OrgTechnic(ABC):
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    @abstractmethod
    def __print(self, cnt_paper, time_print):
        pass

    @abstractmethod
    def __scan(self,  cnt_paper, time_scan):
        pass


class Printer(OrgTechnic):
    def __init__(self, name, price, color, colorful, ink_system, ink_capacity):
        super().__init__(name, price, color)

        self.colorful = colorful.lower()
        self.ink_system = ink_system
        self.ink_capacity = ink_capacity

    def __print(self, cnt_paper, time_print):
        my_list = [el for el in range(1, cnt_paper, 1)]
        time_cnter = 0
        printed_list = []
        for i in my_list:
            print(f'Печатаю лист {i}')
            a = time()
            sleep(time_print)
            time_cnter += time_print
            b = time()
            if b-a > b+2:
                try:
                    raise RuntimeError('Произошло Замятие бумаги, вытащите бумагу и перезапустите')
                except RuntimeError as err:
                    print(err)
            printed_list.append(i)
            print(f'Напечатал лист {i}')
            self.ink_capacity -= 2
        return print(f'Напечатал {len(printed_list)} листов за {time_cnter} секунд')

    def print_logic(self, lists):
        if self.colorful == 'цветной':
            time_c = 1.2
        elif self.colorful == 'чб':
            time_c = 0.5
        if self.ink_system == 'лазер':
            time_i = 0.2
        elif self.ink_system == 'струйный':
            time_i = 0.6
        summ_time = time_c+time_i
        return self.__print(lists, summ_time)

printer1 = Printer('Epson', 'white', 'Цветной',  )



# class Scaner(OrgTechnic):
#     def __init__(self, name, price, color, scan_mode):
#         super().__init__(name, price, color)
#
#         self.scan_mode = scan_mode

#     def __scan(self, cnt_paper, time_scan):
#         my_list = [el for el in range(1, cnt_paper, 1)]
#         time_cnter = 0
#         scan_list = []
#         for i in my_list:
#             print(f'Сканирую лист {i}')
#             a = time()
#             sleep(time_scan)
#             time_cnter += time_scan
#             b = time()
#             if b-a > b+2:
#                 try:
#                     raise RuntimeError('Произошло Замятие бумаги, вытащите бумагу и перезапустите')
#                 except RuntimeError as err:
#                     print(err)
#             scan_list.append(i)
#             print(f'Отсканирован лист {i} и добавлен в память')
#         return print(f'Отсканировано {len(printed_list)} листов за {time_cnter} секунд и добавлено в память')
#
# class Xerox(OrgTechnic):
#     def __init__(self, name, price, color, speed_print, speed_scan, colorful, ink_system, ink_capacity, scan_mode):
#         super().__init__(name, price, color, speed_print, speed_scan)
#         self.speed_print = speed_print
#         self.colorful = colorful
#         self.ink_system = ink_system
#         self.ink_capacity = ink_capacity
#         self.scan_mode = scan_mode