"""Задание 3 (0.5 балла): По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В решении этой
 задачи с помощью циклов можно использовать только один цикл. Предложите как минимум два различных решения."""

number = int(input('Введите число n: '))
def task_03_func(number):
    summa = 0
    previous = 1
    for i in range(1, number + 1):
        current = previous * i
        summa += current
        previous = current
    print('Сумма факториалов равна:', summa)
task_03_func(number)
