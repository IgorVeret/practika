'''Задание 3 (2 балла): Опишите класс для векторов в N-мерном пространстве.
В качестве основы используйте список значений координат вектора, задаваемый list.
Обеспечьте поддержку следующих операций: сложение, вычитание (с созданием нового вектора-результата),
скалярное произведение, косинус угла, евклидова норма. Все операции, которые можно перегрузить
с помощью магических методов, должны быть реализованы именно через них. Класс должен производить
проверку консистентности аргументов для каждой операции и в случаях ошибок выбрасывать исключение
ValueError с исчерпывающим объяснением ошибки.'''

import math
class Vector:
    def __init__(self, vector_values_list):
        if len(vector_values_list) == 0:
            raise ValueError("Пустой список")

        self.v = vector_values_list

    def __check(self, other):
        if len(self.v) != len(other.v):# Проверяем длинну списков
            raise ValueError("Векторы имеют разное количество\
             координат: {} != {}".format(len(self.v), len(other.v)))
        return True
    def __add__(self,other):
        if self.__check(other):
            new_v = []#Создаем новый вектор
            for i in enumerate(self.v):
                new_v.append(self.v[i[0]]+other.v[i[0]])
        return new_v
    def __sub__(self, other):
        if self.__check(other):
            new_v = []#Создаем новый вектор
            for i in enumerate(self.v):
                new_v.append(self.v[i[0]]-other.v[i[0]])
        return new_v
    def __mul__(self,other):
        if self.__check(other):
            new_v = 0
            for i in enumerate(self.v):
                new_v+=self.v[i[0]]*other.v[i[0]]
        return new_v

    @property
    def length(self):#Вычисление длинны вектора

        l=0
        for i in self.v:
          l+=i**2
        length_vector=math.sqrt(l)
        return length_vector

try:
    vector_a = Vector([1,2,3,4,5]) #Вектор 1
    vector_b = Vector([6,7,8,9,10,]) #Вектор 2
except NameError:
    print("Работа программы некорректна. Введеный вектор имеет неподдерживаемые\
     символы или буквы.")

print('Сумма векторов',vector_a+vector_b)
print('Разность векторов', vector_a-vector_b)
print('Скалярное произведение', vector_a*vector_b)
print('Длинна вектора vector_a ',vector_a.length)
print('Длинна вектора vector_b',vector_b.length)

#Чтобы найти косинус угла между векторами нужно,
#скалярное произведение этих векторов разделить на произведение их длин.

print('Косинус угла',((vector_a*vector_b))/(vector_a.length*vector_b.length))