# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.
def quit(str):
    q=0
    list_n = str.split()
    for i in list_n:
        if i == 'q':
            q = list_n.pop(list_n.index('q'))
    return q

def summa(str):
    nums=[]
    list_n=str.split()
    for i in list_n:
        if i=='q':
            list_n.remove('q')
            i=0
        i=int(i)
        nums.append(i)
    return sum(nums)

result = 0
while True:
    str_enter = input('запишите несколько чисел через пробел: ')
    result = result+summa(str_enter)
    print(result)
    if quit(str_enter) == 'q':
        break
