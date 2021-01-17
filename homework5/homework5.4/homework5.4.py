# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus_nums = {
    1:'один',
    2:'два',
    3:'три',
    4:'четыре'
}

new_list = []

with open('file.txt', 'r') as file:
    num_list = file.readlines()
    for i in range(len(num_list)):
        my_list = num_list[i].split('-')
        my_list.pop()
        my_list.append(f'-{rus_nums.get(i+1)}')
        new_list.append(my_list)
        print(my_list)

with open('new_file.txt', 'w') as new_file:
    for i in new_list:
        str=''.join(i)
        new_file.writelines(f'{str}\n')