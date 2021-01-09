# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    test_list = [a, b, c]
    test_list.remove(min(test_list))
    result = sum(test_list)
    return result

print(my_func(44, 11, 22))
