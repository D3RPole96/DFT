import math


class Matrix:
    def __init__(self, two_dimensional_list: [[]]):
        if len(two_dimensional_list) == 0:
            raise ValueError("Matrix column lengths must be non-zero")

        row_len = len(two_dimensional_list[0])

        for row in two_dimensional_list:
            if len(row) != row_len:
                raise ValueError("Matrix row lengths must be the same")
            if len(row) == 0:
                raise ValueError("Matrix row lengths must be non-zero")

        self.matrix = two_dimensional_list
        self.__columns_len = len(self.matrix)
        self.__rows_len = len(self.matrix[0])

    def get_matrix_dimensions(self) -> (int, int):
        return self.__columns_len, self.__rows_len

    def __add__(self, other):
        if self.get_matrix_dimensions() != other.get_matrix_dimensions():
            raise ValueError("Dimensions of the current matrix and the other matrix must be the same")

        new_matrix_list = [[0]] * self.__columns_len
        for i in range(self.__columns_len):
            new_matrix_list[i] = [0] * self.__rows_len

        for row in range(self.__columns_len):
            for column in range(self.__rows_len):
                new_matrix_list[row][column] = self.matrix[row][column] + other.matrix[row][column]

        return Matrix(new_matrix_list)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            return self.__multiply_to_number(other)

        if self.get_matrix_dimensions()[1] != other.get_matrix_dimensions()[0]:
            raise ValueError("Aaa")
        else:
            length = self.get_matrix_dimensions()[1]

        new_matrix_list = [[0]] * self.get_matrix_dimensions()[0]
        for i in range(len(new_matrix_list)):
            new_matrix_list[i] = [0] * other.get_matrix_dimensions()[1]

        for row_index in range(self.get_matrix_dimensions()[0]):
            for column_index in range(other.get_matrix_dimensions()[1]):
                for k in range(length):
                    new_matrix_list[row_index][column_index] += self.matrix[row_index][k] * other.matrix[k][column_index]

        return Matrix(new_matrix_list)

    def __multiply_to_number(self, number):
        new_matrix_list = [[0]] * self.__columns_len
        for i in range(self.__columns_len):
            new_matrix_list[i] = [0] * self.__rows_len

        for row in range(self.__columns_len):
            for column in range(self.__rows_len):
                new_matrix_list[row][column] = self.matrix[row][column] * number

        return Matrix(new_matrix_list)

    def __rmul__(self, other):
        return self.__multiply_to_number(other)

    def __truediv__(self, number):
        if number == 0:
            raise ZeroDivisionError()

        return self.__multiply_to_number(1 / number)

    def get_transposed_matrix(self):
        new_matrix_list = [[0]] * self.__rows_len
        for i in range(self.__rows_len):
            new_matrix_list[i] = [0] * self.__columns_len

        for row_index in range(self.__columns_len):
            for column_index in range(self.__rows_len):
                new_matrix_list[column_index][row_index] = self.matrix[row_index][column_index]

        return Matrix(new_matrix_list)

    def exp(self):
        new_matrix_list = [[0]] * self.__columns_len
        for i in range(self.__columns_len):
            new_matrix_list[i] = [0] * self.__rows_len

        for row_index in range(self.__columns_len):
            for column_index in range(self.__rows_len):
                new_matrix_list[row_index][column_index] = math.e ** self.matrix[row_index][column_index]

        return Matrix(new_matrix_list)
