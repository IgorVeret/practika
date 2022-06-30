'''Задание 2 (1 балл): Опишите класс комплексных чисел. У пользователя должна быть возможность
 создать его объект на основе числа и в алгебраической форме, и в полярной. Класс должен
 поддерживать основные математические операции (+, -, *, /) за счет перегрузки соответствующих
  магических методов. Также он должен поддерживать возможность получить число в алгебраической
 и полярной форме. Допускается использование модуля math.'''

import math

'''sign=int(input('Введите 0 если хотите ввести в числа в  алгебраичесой форме, если в полярной введите 1: '))
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
    d = float(input('Второе число введите в радианах b: '))'''
#Класс получает значение и реализует преобразования как из алгебраической записи в полярную, так и обратно
sign=0
class ComplexNumber:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def complex_number(self):
        a_first_number = complex(a,b)# первое комплексное число
        a_second_number = complex(c, d)# второе комплексное число
        return a_first_number, a_second_number
    def alg_trig(self):
        t_first_number = complex(math.sqrt(a**2+b**2),math.degrees(math.atan(b/a)))
        t_second_number= complex(math.sqrt(c**2+d**2),math.degrees(math.atan(d/c)))
        # print(t_first_number,t_second_number)
        return t_first_number,t_second_number
    def trig_alg(self):
        at_first_number = complex(a*math.cos(b), a*math.sin(b))
        at_second_number= complex(c*math.cos(d), c*math.sin(d))
        # print(at_first_number, at_second_number)
        return at_first_number, at_second_number

number = ComplexNumber(a,b,c,d)

if sign ==0:
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
    print('Преобразованные  комплексные числа',alg_1,alg_2)
    add=alg_1.__add__(alg_2)
    sub=alg_1.__sub__(alg_2)
    mul=alg_1.__mul__(alg_2)
    truediv=alg_1.__truediv__(alg_2)
    print('Сложение полярных комплексных чисел', add)
    print('Вычитание полярных комплексных чисел', sub)
    print('Умножение полярных комплексных чисел', mul)
    print('Деление полярных комплексных чисел', truediv)
elif sign==1:
    alg_1,alg_2= number.complex_number() # Получаем объекты в полярной форме
    print('Полученные комплексные числа',alg_1,alg_2)
    add=alg_1.__add__(alg_2)
    sub=alg_1.__sub__(alg_2)
    mul=alg_1.__mul__(alg_2)
    truediv=alg_1.__truediv__(alg_2)
    print('Сложение полярных комплексных чисел', add)
    print('Вычитание полярных комплексных чисел', sub)
    print('Умножение полярных комплексных чисел', mul)
    print('Деление полярных комплексных чисел', truediv)
    print()
    print('---------Преобразование в алгебрраическую форму------------------------------')
    print()
    alg_1,alg_2= number.trig_alg()
    print('Преобразованные комплексные числа',alg_1,alg_2)
    add=alg_1.__add__(alg_2)
    sub=alg_1.__sub__(alg_2)
    mul=alg_1.__mul__(alg_2)
    truediv=alg_1.__truediv__(alg_2)
    print('Сложение алгебраических комплексных чисел', add)
    print('Вычитание алгебраических комплексных чисел', sub)
    print('Умножение алгебраических комплексных чисел', mul)
    print('Деление алгебраических комплексных чисел', truediv)
