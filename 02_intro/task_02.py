'''Задание 2 (1 балл): Опишите класс комплексных чисел. У пользователя должна быть возможность
 создать его объект на основе числа и в алгебраической форме, и в полярной. Класс должен
 поддерживать основные математические операции (+, -, *, /) за счет перегрузки соответствующих
  магических методов. Также он должен поддерживать возможность получить число в алгебраической
 и полярной форме. Допускается использование модуля math.'''

import math

sign=int(input('Введите 0 если хотите ввести в числа в  алгебраической форме, если в полярной введите 1: '))
if sign==0:
    print('Формула комплексного числа a+bj ')
    a=float(input('Первое число введите а: '))
    b=float(input('Первое число введите b: '))
    c=float(input('Второе число введите a: '))
    d=float(input('Второе число введите b: '))
elif sign==1:
    print('Формула комплексного числа a+bj ')
    a = float(input('Первое число введите а: '))
    b = float(input('Первое число введите в радианах b: '))
    c = float(input('Второе число введите a: '))
    d = float(input('Второе число введите в радианах b: '))
#Класс получает значение и реализует преобразования как из алгебраической записи в полярную, так и обратно

class ComplexNumber:
    def __init__(self, a=0, b=0):
        self.a = a #Действительная часть
        self.b = b # Мнимая часть
    @staticmethod
    def alg_polar(a, b):# Преобразование из алгебраической в полярную форму
        a = math.sqrt(a ** 2 + b ** 2)
        b = math.atan(b / a)
        return a,b

    @staticmethod
    def polar_alg(a,b):# преобразование из полярной в алгебраическую форму
        a=a*math.cos(b)
        b = a*math.sin(b)
        return a, b
    #Перезагрузка операторов вычислений
    def __add__(self, other):
        return complex(self.a+other.a, self.b+other.b)
    def __sub__(self, other):
        return complex(self.a - other.a, self.b - other.b)
    def __mul__(self, other):
        return complex(self.a * other.a -self.b * other.b,self.a * self.b + other.b * self.a)
    def __truediv__(self, other):
        return complex(self.a / other.a, self.b / other.b)

if sign == 0:# При вводе в алгебраической форме
    one_number=ComplexNumber(a,b)
    two_number = ComplexNumber(c,d)
    print()
    print('---------Расчет в алгебраической форме------------------------------')
    print()
    print(one_number+two_number)
    print(one_number-two_number)
    print(one_number*two_number)
    print(one_number/two_number)
    print()
    print('---------Преобразование в полярную форму и расчет-----------------------')
    print()
    polar_a,polar_b = ComplexNumber.alg_polar(a,b)
    polar_c,polar_d= ComplexNumber.alg_polar(c,d)

    p_one_number=ComplexNumber(polar_a,polar_b)
    p_two_number=ComplexNumber(polar_c,polar_d)

    print(p_one_number+p_two_number)
    print(p_one_number-p_two_number)
    print(p_one_number*p_two_number)
    print(p_one_number/p_two_number)
    print()
elif sign == 1:# При вводе в полярной форме
    one_number = ComplexNumber(a, b)
    two_number = ComplexNumber(c, d)
    print()
    print('---------Расчет в полярной форме------------------------------')
    print()
    print(one_number + two_number)
    print(one_number - two_number)
    print(one_number * two_number)
    print(one_number / two_number)
    print()
    print('---------Преобразование в алгебраическую форму и расчет-----------------------')
    print()
    polar_a, polar_b = ComplexNumber.polar_alg(a, b)
    polar_c, polar_d = ComplexNumber.polar_alg(c, d)

    p_one_number = ComplexNumber(polar_a, polar_b)
    p_two_number = ComplexNumber(polar_c, polar_d)

    print(p_one_number + p_two_number)
    print(p_one_number - p_two_number)
    print(p_one_number * p_two_number)
    print(p_one_number / p_two_number)
    print()

