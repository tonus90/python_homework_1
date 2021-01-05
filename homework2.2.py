list = []

number = int(input('Введи количество элементов: '))

for i in range(number):
    list.append(input('Вставить элемент списка: '))

print(list)

for i in range(0, len(list)-1, 2):
    list[i], list[i+1] = list[i+1], list[i]

print(list)