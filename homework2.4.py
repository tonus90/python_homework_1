some_str = input('Введите строку из несколькиз слов, разделенных пробелами: ')

list=some_str.split(' ')

print(list)

for i in list:
    print(f'{list.index(i)+1}: {i[:10]}')
