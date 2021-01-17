# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import json
result = []
my_dict = {}
with open('file.txt', 'r') as file:
    subjects_list = file.readlines()
    for i in range (len(subjects_list)):
        my_list = subjects_list[i].split()
        sub_name = my_list.pop(0)
        for n in my_list:
            try:
                hours_list = n.split('(')
                result.append(int(hours_list[0]))
            except ValueError:
                result.append(0)
        my_dict[sub_name] = sum(result)
        result.clear()

print(f'\nОбработали текстовый файл, получили словарь: {my_dict}')

with open('my_json.json', 'w') as my_json:
    json.dump(my_dict, my_json)
