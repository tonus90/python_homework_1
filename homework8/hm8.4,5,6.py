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
from random import choice, random

class OrgWarehouse():
    pass

class OrgTechnic(ABC):
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    @abstractmethod
    def print(self, cnt_paper, time_print):
        pass

    @abstractmethod
    def scan(self,  cnt_paper, time_scan):
        pass


class Printer(OrgTechnic):
    def __init__(self, name, price, color, colorful, ink_system, ink_capacity):
        super().__init__(name, price, color)

        self.colorful = colorful.lower()
        self.ink_system = ink_system
        self.ink_capacity = ink_capacity

    def print(self, cnt_paper, time_print):
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

    def scan(self,  cnt_paper, time_scan):
        pass

    def print_logic(self, lists):
        my_dict1 = {
            'цветной': 1.2,
            'чб': 0.6,
        }
        my_dict2 = {
            'лазер': 0.5,
            'струйный': 1
        }

        time_c = my_dict1.get(self.colorful)
        time_i = my_dict2.get(self.ink_system)
        summ_time = time_c+time_i
        return self.print(lists, summ_time)

    def __str__(self):
        return f'Параметры принтера. Фирма: {self.name}, Стоимость: {self.price}р., Цвет: {self.color},\n Чернила: {self.ink_system} Запас чернил: {self.ink_capacity}, Цвет/ЧБ: {self.colorful}'


# def generate_objects(cnt_objects):
name = ['Sony', 'Epson', 'Cannon', 'HP', 'Kyocera', 'Xerox']
price = int(random()*10)*1000
color = ['white', 'black', 'blue', 'gray']
colorful = ['цветной', 'чб']
ink_system = ['лазер', 'струйный']
ink_capacity = [100, 150, 200]
scan_mode = ['цветной', 'чб']
print_params = [name, price, color, colorful, ink_system, ink_capacity]
name_list = ['name', 'price', 'color', 'colorful', 'ink_system', 'ink_capacity']
printers_list = []
p_dict = {}
for j in range(10):
    for i in range(len(name_list)):
        p_dict[name_list[i]] = choice(print_params[i])
print(p_dict)

printer_params = {
    'name': 'Epson',
    'price': 5000,
    'color': 'white',
    'colorful': 'цветной',
    'ink_system': 'струйный',
    'ink_capacity': 100
}

# printer1 = Printer(**printer_params)
# printer1.print_logic(5)
# print(printer1)
price = int(random()*10)*1000
print(price)


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