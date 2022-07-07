'''Задание 6 (5 баллов): Опишите класс для хранения двумерных числовых матриц на основе списков.
 Реализуйте поддержку индексирования, итерирования по столбцам и строкам, по-элементные математические
 операции (с помощью магических методов), операцию умножения матрицы (как метод dot класса),
 транспонирование, поиска следа матрицы, а также поиск значения её определителя, если он существует,
 в противном случае соответствующий метод должен выводить сообщение об ошибке и возвращать None.

Матрицу должно быть возможным создать из списка (в этом случае у неё будет одна строка),
списка списков, или же передав явно три числа: число строк, число столбцов и значение
по-умолчанию (которое можно не задавать, в этом случае оно принимается равным нулю).
Все операции должны проверять корректность входных данных и выбрасывать исключение с
информативным сообщением в случае ошибки.

Матрица должна поддерживать методы сохранения на диск в текстовом и бинарном файле и методы
 обратной загрузки с диска для обоих вариантов. Также она должна поддерживать метод полного
 копирования. Обе процедуры должны быть реализованы с помощью шаблона "примесь" (Mixin), т.е.
  указанные функциональности должны быть описаны в специализированных классах.

В реализации математических операций запрещается пользоваться любыми функциями,
требующими использования оператора import.'''

'''Не реализованно:
1. Умножения матрицы (как метод dot класса)
2. Матрица должна поддерживать методы сохранения на диск в текстовом и бинарном файле и методы обратной загрузки с диска для обоих вариантов.
с помощью шаблона "примесь" (Mixin) '''


class Matrix:
    def __init__(self, rows=None, n=None, m=None, default=0):
        if rows:  # Проверяем параметры ряда
            if type(rows[0]) == int:
                # self.n = 1
                # self.m = len(rows)
                self.rows = [rows]  # Однострочная матрица
                print('Одна строка', self.rows)
            else:
                self.m = len(rows[0])
                for i in enumerate(rows):
                    if len(i[1]) != self.m:
                        raise Exception('Cтроки имеют разную длину.')
                    self.n = 1 + i[0]

                self.rows = rows  # Матрица из списка

            # self.default = None
        else:  # Создаем матрицу из числа строк столбцов и значению по умолчанию
            if n and m:
                self.n = n  # Число строк
                self.m = m  # Число столбцов

                self.default = default  # Значение по умолчанию.
                row = [default] * self.m
                self.rows = [row] * n  # Матрица из числа строк и столбцов

            else:
                raise ValueError('Параметры инициализации имеют тип None.')

    def __repr__(self):
        return str(self.rows)

    #
    @property
    def track_matrix(self):  # След матрицы
        if self.n != self.m:
            raise ValueError('Matrix is not square.')
        else:
            tr = []
            for row in enumerate(self.rows):
                for i in range(len(row[1])):
                    if i == row[0]:
                        tr.append(row[1][i])
            return sum(tr)

    @property
    def transposition(self):
        new_self = []
        for i in range(len(self.rows[0])):
            axis = []
            for row in self.rows:
                axis.append(row[i])
            new_self.append(axis)

        return Matrix(new_self)

    def __determinant(self, A, total=0):
        indices = list(range(len(A)))
        if len(A) == 2 and len(A[0]) == 2:
            val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
            return val
        for fc in indices:
            As = A.copy()
            As = As[1:]
            height = len(As)

            for i in range(height):
                As[i] = As[i][0:fc] + As[i][fc + 1:]

            sign = (-1) ** (fc % 2)
            sub_det = self.__determinant(As)
            total += sign * A[0][fc] * sub_det

        return total

    @property
    def determinant(self):
        if self.n != self.m:
            raise ValueError('Необходима квадратная матрица.')
        else:
            if len(self.rows) == 1:
                return self.rows[0][0]
            else:
                return self.__determinant(self.rows)

    def __error(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Не могу добавить обект {}".format(type(other)))
        else:
            if self.n != other.n or self.m != self.m:
                raise ValueError('Разный размер матриц')
            else:
                return True

    def __add__(self, other):
        if self.__error(other):
            sum_matrix = []
            for i in range(len(self.rows)):
                new_row = [self.rows[i][j] + other.rows[i][j] for j in range(len(self.rows[i]))]
                sum_matrix.append(new_row)
        return Matrix(sum_matrix)

    def __sub__(self, other):
        if self.__error(other):
            sub_matrix = []
            for i in range(len(self.rows)):
                new_row = [self.rows[i][j] - other.rows[i][j] for j in range(len(self.rows[i]))]
                sub_matrix.append(new_row)
        return Matrix(sub_matrix)

    def __mul__(self, other):
        if self.__error(other):
            mul_matrix = []
            for i in range(len(self.rows)):
                new_row = [self.rows[i][j] * other.rows[i][j] for j in range(len(self.rows[i]))]
                mul_matrix.append(new_row)
        return Matrix(mul_matrix)

    def __truediv__(self, other):
        if self.__error(other):
            div_matrix = []
            for i in range(len(self.rows)):
                new_row = [self.rows[i][j] / other.rows[i][j] for j in range(len(self.rows[i]))]
                div_matrix.append(new_row)
        return Matrix(div_matrix)

    def save_file(self, filename, style='w'):
        with open(filename, style) as f:
            if style == 'w':
                for row in self.rows:
                    f.write(''.join([str(row), "\n"]))
            else:
                for row in self.rows:
                    f.write(bytearray(str(row) + '\n', 'utf-8'))

    def load_file(filename, style='r'):
        with open(filename, style) as out_put:
            s = out_put.readlines()
            res = [i.strip("[]\n").split(", ") for i in s]
            res_row = []
            for row in res:
                new_row = [int(i) for i in row]
                res_row.append(new_row)
            return Matrix(res_row)

    def copy(self):
        copy = Matrix(self.rows)
        return copy


class Mixed(Matrix):
    pass


# z = Matrix(a)
a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 5], [3, 7, 4, 5]])  # Матрица из списка
b = Matrix(n=4, m=4, default=2)  # Создаем матрицу из числа строк столбцов и значению по умолчанию
print(b)
c = Matrix([1, 5, 7])
print('----------------Арифметические операции-----------------')
print('Сумма матриц', a + b)
print('Разность матриц', a - b)
print('Умножение матриц', a * b)
print('Частное матриц', a / b)
print('----------------Запись файла-----------------')
print('Запись файла в текстовом формате')
a.save_file('task_06\matrix_w.txt', 'w')
print('Запись файла в бинарном формате')
a.save_file('task_06\matrix_bin.bin', 'wb')
print('----------------Чтение файла-----------------------')
w = Matrix.load_file('task_06\matrix_w.txt', 'r')
print('Чтение файла в текстовом формате', w)
w = Matrix.load_file('task_06\matrix_bin.bin', 'r')
print('Чтение файла в бинарном формате', w)
print('----------------Копирование матрицы-----------------')
print('Копирование матрицы', Mixed.copy(a))
print('----------------Определитель матрицы-----------------')
print("Определитель матрицы", a.determinant)
print('----------------Транспонирование матрицы-----------------')
print("Транспонирование матрицы", a.transposition)
print('----------------След матрицы------------------------')
print("След матрицы матрицы", a.track_matrix)
