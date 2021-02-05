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
        return self.str_return()

    def str_return(self):
        list_data = []
        for i in self.matrix:
            new_list = [str(el) for el in i]
            res1 = ' '.join(new_list)
            list_data.append(res1)
        res2 = '\n'.join(list_data)
        return res2

    def __add__(self, other):
        result = []
        num = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summ = self.matrix[i][j] + other.matrix[i][j]
                num.append(summ)
                if len(num) == len(self.matrix):
                    result.append(num)
                    num = []
        self.matrix = result
        return Matrix(self.matrix)


m1 = [[1, 2, 3],[4,5,6],[7,8,9]]
m2 = [[4, 5, 6],[3,3,3],[4,4,4]]
m3 = [[7, 8, 9],[5,5,5],[6,6,6]]

mat1 = Matrix(m1)
mat2 = Matrix(m2)
mat3 = Matrix(m3)
print(mat1)
# for i in m.matrix_sum():
#     print(i)
print(mat1+mat2+mat3)

# list_data = []
# for j in range(0, len(matrix)):
#     for i in matrix:
#         new_list = [str(i) for i in i]
#         res1 = ' '.join(new_list)
#         list_data.append(res1)
#     print(list_data[j])
