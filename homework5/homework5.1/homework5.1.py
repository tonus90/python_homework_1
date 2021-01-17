# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
# file = open('file.txt', )

with open('file.txt', 'w') as file:
    while True:
        insert = input('Введи данные в файл: ')
        if insert == 'q':
            break
        text = file.write(f'{insert}\n')