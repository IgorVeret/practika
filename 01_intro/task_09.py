'''Задание 9 (1 балл): Напишите функцию, которая получает на вход натуральное число n и
выводит первые n строк треугольника Паскаля.'''


n = int(input('Введите натуральное число: '))
def task_09_func(number):
    number = [1] + number
    for i in range(1, len(number) - 1):
        number[i] += number[i + 1]
    return number

number = []
for i in range(n):
    number = task_09_func(number)
    print(number)

