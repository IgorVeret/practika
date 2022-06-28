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
    def algebra(self):
        a_first_number = complex(a,b)# алгебраическое первое число
        a_second_number = complex(c, d)# алгебраическое второе число
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
alg_1,alg_2= number.algebra()
z=alg_1.__add__(alg_2)
print(complex(z))
# print(alg_1,alg_2)

# a_first=number.

print(number.trig_alg())