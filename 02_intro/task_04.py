'''Задание 4 (2 балл): Опишите декоратор, который принимает на вход функцию и при каждом
 её вызове печатает строку "This function was called N times", где N - число раз, которое
 это функция была вызвана на текущий момент (пока функция существует как объект, это число,
 очевидно, может только неубывать).
'''
number=int(input('Ввоедите число повторений: '))
def calls_counter(func):

    func.count = 0
    def wrap(*args):

        func.count += 1
        print('This function was called {} times'.format(func.count))

    return wrap
@calls_counter
def func(a):
    pass
for i in range(number):
    func(i)