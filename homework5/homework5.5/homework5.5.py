# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
int_list = []

with open('my_nums.txt', 'w') as my_nums:
    my_nums.write(input('Введите числа в строку через пробел: '))

with open('my_nums.txt', 'r') as my_nums:
    num_str = my_nums.readlines()
    num_list = (num_str[0].split())
    for i in num_list:
        int_list.append(int(i))
    print(f'Вы ввели {len(int_list)} чисел, их сумма: {sum(int_list)}')