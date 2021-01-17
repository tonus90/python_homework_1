# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

salaries = []
with open('file.txt', 'r') as file:
    workers_list = file.readlines()
    for i in range(len(workers_list)-1):
        salary_list = workers_list[i].split()
        if int(salary_list[1]) < 20000:
            print(f'{salary_list[0]} имеет ЗП меньше 20.000руб')
        salaries.append(int(salary_list[1]))
    avg_salary = sum(salaries)/len(workers_list)
    print(f'средняя зарплата: {int(avg_salary)}')