# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
#
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        # for j in range(0, len(self.matrix)):
        #     for i in self.matrix:
        #         new_list = [str(i) for i in i]
        #         res1 = ' '.join(new_list)
        #     a = " ".join(str(el) for el in self.matrix)
        #     return f'{a}\n v'
        list_data = []
        for j in range(0, len(matrix)):
            for i in matrix:
                new_list = [str(i) for i in i]
                res1 = ' '.join(new_list)
                list_data.append(res1)
            # print(list_data[j])

            return f'{[el for el in list_data]}'


my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list3 = [7, 8, 9]
matrix = [my_list1, my_list2, my_list3]
m = Matrix(matrix)
print(m)


list_data = []
for j in range(0, len(matrix)):
    for i in matrix:
        new_list = [str(i) for i in i]
        res1 = ' '.join(new_list)
        list_data.append(res1)
    print(list_data[j])