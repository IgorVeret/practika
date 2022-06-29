'''Задание 2 (1 балл): Опишите класс комплексных чисел. У пользователя должна быть возможность
 создать его объект на основе числа и в алгебраической форме, и в полярной. Класс должен
 поддерживать основные математические операции (+, -, *, /) за счет перегрузки соответствующих
  магических методов. Также он должен поддерживать возможность получить число в алгебраической
 и полярной форме. Допускается использование модуля math.'''

import math
a,b=4,5 # Ввод первого числа
c,d=6,7 # Ввод второго числа числа
class ComplexNumber:
    def __init__(self, a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def complex_number(self):
        a_first_number = complex(a,b)# первое число
        a_second_number = complex(c, d)# второе число
        return a_first_number, a_second_number
    def alg_trig(self):
        t_first_number = complex(math.sqrt(a**2+b**2),math.degrees(math.atan(b/a)))# Преобразование в из алгебраического в полярную
        t_second_number= complex(math.sqrt(c**2+d**2),math.degrees(math.atan(d/c)))# Преобразование в из алгебраического в полярную
        return t_first_number,t_second_number
    def trig_alg(self):
        at_first_number = complex(a*math.cos(b), a*math.sin(b))
        at_second_number= complex(c*math.cos(d), c*math.sin(d))
        return at_first_number, at_second_number

number = ComplexNumber(a,b,c,d)
alg_1,alg_2= number.complex_number() # Получаем объекты в алгебраической форме
print('Полученные комплексные числа',alg_1,alg_2)
add=alg_1.__add__(alg_2)
sub=alg_1.__sub__(alg_2)
mul=alg_1.__mul__(alg_2)
truediv=alg_1.__truediv__(alg_2)
print('Сложение алгебраических комплексных чисел', add)
print('Вычитание алгебраических комплексных чисел', sub)
print('Умножение алгебраических комплексных чисел', mul)
print('Деление алгебраических комплексных чисел', truediv)
print()
print('---------Преобразование в полярную форму------------------------------')
print()
alg_1,alg_2= number.alg_trig()
print('Полученные комплексные числа',alg_1,alg_2)
add=alg_1.__add__(alg_2)
sub=alg_1.__sub__(alg_2)
mul=alg_1.__mul__(alg_2)
truediv=alg_1.__truediv__(alg_2)
print('Сложение алгебраических комплексных чисел', add)
print('Вычитание алгебраических комплексных чисел', sub)
print('Умножение алгебраических комплексных чисел', mul)
print('Деление алгебраических комплексных чисел', truediv)
# print(alg_1,alg_2)

# print(alg_1,alg_2)

# a_first=number.

# print(number.trig_alg())