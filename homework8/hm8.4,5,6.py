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


from abc import ABC, abstractmethod
from time import sleep, time
from random import choice, random

class OrgWarehouse():
    def __init__(self, capacity, department, type_org):
        self.capacity = capacity
        self.department = department
        self.type_org = type_org
    def get_in(self, cnt_org):
        my_dict = {}
        cnt_org

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
    type_org = 'Printer'
    def __init__(self, name, price, color, colorful, ink_system, ink_capacity):
        super().__init__(name, price, color)

        self.colorful = colorful
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
        return print(f'Напечатал {len(printed_list)+1} листов за {int(time_cnter)} секунд')

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
        return f'Параметры принтера. Фирма: {self.name}, Стоимость: {self.price}р., Цвет: {self.color}, Чернила: {self.ink_system} Запас чернил: {self.ink_capacity}, Цвет/ЧБ: {self.colorful}'

class Scaner(OrgTechnic):
    type_org = 'Scaner'
    def __init__(self, name, price, color, scan_mode):
        super().__init__(name, price, color)

        self.scan_mode = scan_mode


    def scan(self, cnt_paper, time_scan):
        my_list = [el for el in range(1, cnt_paper, 1)]
        time_cnter = 0
        scan_list = []
        for i in my_list:
            print(f'Сканирую лист {i}')
            sleep(time_scan)
            time_cnter += time_scan
            scan_list.append(i)
            print(f'Отсканировал лист {i}')
        return print(f'Отсканировано {len(scan_list)} листов за {int(time_cnter)} секунд. Листы записаны в память.')

    def print(self, cnt_paper, time_print):
        pass

    def scan_logic(self, lists):
        my_dict1 = {
            'цветной': 3,
            'чб': 1.5
        }
        time_s = my_dict1.get(self.scan_mode)
        return self.scan(lists+1, time_s)

    def __str__(self):
        return f'Параметры Сканера. Фирма: {self.name}, Стоимость: {self.price}р., Цвет: {self.color}, Скан - цвет/чб: {self.scan_mode}'

class Xerox(OrgTechnic):
    type_org = 'Xerox'
    def __init__(self, name, price, color, colorful, ink_system, ink_capacity, scan_mode):
        super().__init__(name, price, color)
        self.colorful = colorful
        self.ink_system = ink_system
        self.ink_capacity = ink_capacity
        self.scan_mode = scan_mode

    def scan(self, cnt_paper, time_scan):
        my_list = [el for el in range(1, cnt_paper, 1)]
        time_cnter = 0
        scan_list = []
        for i in my_list:
            print(f'Сканирую листов {i}')
            sleep(time_scan)
            time_cnter += time_scan
            scan_list.append(i)
        return print(f'Отсканировал листов {len(scan_list)}')

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
            self.ink_capacity -= 2
        return print(f'Напечатал листов {len(printed_list)}')

    def logic_xerox(self, lists):
        my_dict1 = {
            'цветной': 1.2,
            'чб': 0.6,
        }
        my_dict2 = {
            'лазер': 0.5,
            'струйный': 1
        }
        my_dict3 = {
            'цветной': 3,
            'чб': 1.5,
        }

        time_c = my_dict1.get(self.colorful)
        time_i = my_dict2.get(self.ink_system)
        time_s = my_dict3.get(self.scan_mode)
        time_p = time_c+time_i
        time_copy = time_p +time_s
        self.scan(lists+1, time_s)
        self.print(lists+1, time_p)
        return print(f'Откопировано {lists} листов за {int(time_copy)} секунд.')

    def __str__(self):
        return f'Параметры Xeroxa. Фирма: {self.name}, Стоимость: {self.price}р., Цвет: {self.color}, ' \
               f'Скан - цвет/чб: {self.scan_mode}, Печать - цвет/чб: {self.colorful}, Чернила: {self.ink_system}, ' \
               f'Запас чернил: {self.ink_capacity}'

class GenObj():
    def __init__(self, cnt, mode):
        self.cnt = cnt
        self.mode = mode.lower()
    def generate_params(self):
        name = ['Sony', 'Epson', 'Cannon', 'HP', 'Kyocera', 'Xerox']
        price = [3000, 4000, 5000, 6000, 9000]
        color = ['white', 'black', 'blue', 'gray']
        colorful = ['цветной', 'чб']
        ink_system = ['лазер', 'струйный']
        ink_capacity = [100, 150, 200]
        scan_mode = ['цветной', 'чб']
        print_params = [name, price, color, colorful, ink_system, ink_capacity]
        name_list = ['name', 'price', 'color', 'colorful', 'ink_system', 'ink_capacity']
        p_dict = {}
        if self.mode == 'x':
            print_params.append(scan_mode)
            name_list.append('scan_mode')
        elif self.mode == 's':
            print_params.remove(colorful)
            print_params.remove(ink_system)
            print_params.remove(ink_capacity)
            print_params.append(scan_mode)
            name_list.remove('colorful')
            name_list.remove('ink_system')
            name_list.remove('ink_capacity')
            name_list.append('scan_mode')
        for i in range(len(name_list)):
            p_dict[name_list[i]] = choice(print_params[i])
        return p_dict

    def generate_obj(self):
        list_obj = []
        if self.mode == 'p':
            for i in range(self.cnt):
                obj = Printer(**self.generate_params())
                list_obj.append(obj)
        elif self.mode == 'x':
            for i in range(self.cnt):
                obj = Xerox(**self.generate_params())
                list_obj.append(obj)
        elif self.mode == 's':
            for i in range(self.cnt):
                obj = Scaner(**self.generate_params())
                list_obj.append(obj)
        return list_obj

objects_p = GenObj(6, 'p')
print(objects_p.generate_obj())
print(objects_p.generate_obj()[0])
objects_p.generate_obj()[0].print_logic(10)

objects_s = GenObj(5, 's')
print(objects_s.generate_obj())
print(objects_s.generate_obj()[0])
objects_s.generate_obj()[0].scan_logic(4)

objects_x = GenObj(4, 'x')
print(objects_x.generate_obj())
print(objects_x.generate_obj()[0])
objects_x.generate_obj()[0].logic_xerox(3)
