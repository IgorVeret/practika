'''Задание 4 (0.5 балла): Определить, является ли введённая строка палиндромом
 (то есть одинаково читается с обеих сторон). Предложите как минимум три различных решения.'''
# Вариант 1
s= input('Введите строку s: ')
def task_04_func1(s):
    print(type(s)) # Проверка типа переменной
    if s[::-1].startswith(s):# Если палиндром
        print('Палиндром')

    else: # Если не палиндром
        print('Не палиндром')
task_04_func1(s)
#Вариант 2
arg= input('Введите строку arg: ')
def task_04_func2(arg):
    darg = arg.replace(' ',' ')
    if arg == arg[::-1]:
        print('Палиндром')
    else:
        print('Не палиндром')
task_04_func2(arg)

#Вариант 3
value= input('Введите строку value: ')
def task_04_func3(value):
    a=list(value) #преобразуем в строку
    b=list(reversed(value)) #преобразуем в строку
    if a==b:
        print('Палиндром')
    else:
        print('Не палиндром')
task_04_func3(value)

