# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

avg_profit_dict={}
with open('file.txt', 'r') as file:
    str_list = file.readlines()
    firms_profit = {}
    profit_list = []
    for i in str_list:
        firm_list = i.split()
        if int(firm_list[2]) > int(firm_list[3]):
            profit = int(firm_list[2]) - int(firm_list[3])
            firms_profit[firm_list[0]] = profit
            profit_list.append(profit)
    avg_profit = sum(profit_list)/len(profit_list)

    avg_profit_dict['average_profit'] = int(avg_profit)
    my_list = [firms_profit, avg_profit_dict]

with open('my_json.json', 'w') as my_json:
    json.dump(my_list, my_json)
