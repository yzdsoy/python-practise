#!/usr/bin/python


class MatrixSyntaxError(Exception):
    pass


class Matrix:
    def __init__(self, string):
        while string.find(" ") != -1:
            space = string.find(" ")
            string = string[:space]+string[space+1:]
        if string[0] != "[" or string[-1] != "]":
            raise MatrixSyntaxError
        else:
            string = string[1:len(string)-1]
        matrix = []
        if len(string) != 0:
            string += ";"
        row_number = 0
        while len(string) != 0:
            matrix.append([])
            row = string.partition(";")[0]+","
            string = string.partition(";")[2]
            while len(row) != 0:
                matrix[row_number].append(int(row.partition(",")[0]))
                row = row.partition(",")[2]
            row_number += 1
        for i in range(0, len(matrix)):
            if len(matrix[i]) != len(matrix[i-1]):
                raise MatrixSyntaxError
        self.matrix = matrix


    def __str__(self):
        a = ""
        for row in self.matrix:
            for element in row:
                a += str(element) + ","
            a = a[:len(a)-1]
            a += ";"
        a = a[:len(a)-1]
        return "[" + a + "]"

    def __add__(self, other):
        try:
            k = Matrix("[]")
            for i in range(0, len(self.matrix)):
                k.matrix.append([])
                for j in range(0, len(self.matrix[i])):
                    k.matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
            return k
        except IndexError:
            raise MatrixSyntaxError

    def __sub__(self, other):
        try:
            k = Matrix("[]")
            for i in range(0, len(self.matrix)):
                k.matrix.append([])
                for j in range(0, len(self.matrix[i])):
                    k.matrix[i].append(self.matrix[i][j] - other.matrix[i][j])
            return k
        except IndexError:
            raise MatrixSyntaxError

    def __mul__(self, other):
        try:
            if isinstance(other, int or float):
                k = Matrix("[]")
                for i in range(0, len(self.matrix)):
                    k.matrix.append([])
                    for j in range(0, len(self.matrix[i])):
                        k.matrix[i].append(self.matrix[i][j] * other)
                return k
            elif isinstance(other, Matrix):
                k = Matrix("[]")
                for i in range(0, len(self.matrix)):
                    k.matrix.append([])
                    for j in range(0, len(self.matrix)):
                        k.matrix[i].append(self.matrix[i][j] * other)
                return k
        except IndexError:
            raise MatrixSyntaxError

    def __truediv__(self, other):
        k = Matrix("[]")
        for i in range(0, len(self.matrix)):
            k.matrix.append([])
            for j in range(0, len(self.matrix[i])):
                k.matrix[i].append(self.matrix[i][j] / other)
        return k

    def __pow__(self, power):
        k = Matrix("[]")
        for i in range(0, len(self.matrix)):
            k.matrix.append([])
            for j in range(0, len(self.matrix[i])):
                k.matrix[i].append(self.matrix[i][j] ** power)
        return k

    def __eq__(self, other):
        if len(self.matrix) != len(other.matrix):
            return False
        else:
            for i in range(0, len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    return False
                else:
                    for j in range(0, len(self.matrix[i])):
                        if self.matrix[i][j] != other.matrix[i][j]:
                            return False
        return True

    def isIdentity(self):
        for i in range(0, len(self.matrix)):
            if len(self.matrix[i]) != len(self.matrix):
                return False
            else:
                for j in range(0, len(self.matrix[i])):
                    if i != j:
                        if self.matrix[i][j] != 0:
                            return False
                    else:
                        if self.matrix[i][j] != 1:
                            return False
        return True

    def isSquare(self):
        for i in range(0, len(self.matrix)):
            if len(self.matrix[i]) != len(self.matrix):
                return False
        return True

    def determinant(self):
        if len(self.matrix) == 1:
            return self.matrix[0][0]
        else:
            k = 0
            for i in range(0, len(self.matrix[0])):
                k += ((-1)**(i + 1) * self.matrix[0])
            return k

    def __getitem__(self, item):
        if isinstance(item, int):
            k = Matrix("[]")
            k.matrix.append(self.matrix[item])
            return k
        elif isinstance(item, tuple):
            return self.matrix[item[0]][item[1]]


a = Matrix("[1   ,2,3;1  ,2,3;1,2,3]")
b = Matrix("[ 2,3;2,3]")
c = Matrix("[1   ,3,3;1  ,2,3;1,2,3]")
d = Matrix("[1   ,0,0;0  ,1,0;0,0,1]")
print(a)
print(d.isIdentity())
print(d.isSquare())
print(a[1])
print(a[1, 2])
