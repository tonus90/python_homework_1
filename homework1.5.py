# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника
earn = float(input('Введите выручку компании: '))
costs = float(input('Введите издержки компании: '))
profit = earn-costs #прибыль

if (earn > costs): #если выручка больше издержек
    print(f'Компания работает с прибылью: {profit} руб.') #печатаем
elif (earn < costs): #если же  издержки больше выручки
    print(f'Компания работает в убыток: {costs-earn} руб. Бизнес нерентабелен') #печатаем это
else: #иначе (выручка равна издержкам) печатаем, что бизнес нерентабелен
    print('Компания работает в безубыток. Бизнес нерентабелен')

if (earn>costs): #если прибыль есть, то
    print(f'Рентабельность бизнеса: {(earn-costs)/earn}') #напечатаем рентабельность
    num_workers = int(input('Впишите численность работников: ')) #запросим количество работников
    print(f'Прибыль на одного сотрудника составит: {profit/num_workers} руб.') #напечатаем прибыль на каждого сотрудника(премия?)))





