'''Задание 7 (1 балл): Дан список целых чисел. Напишите функцию, которая возвращает копию этого списка,
 из которой удалены отрицательные числа, а все прочие числа возведены в квадрат. Также возвращаемая
последовательность должна быть отсортирована по убыванию. Предложите как минимум три различных решения.'''
# Вариант 1
lst_1 = [1,4,2,-3,6,7,8,9,]

z = []
def task_07_func_1(lst_1):
    for i in lst_1:
        if i > 0:
            i=i**2
            z.append(i)
task_07_func_1(lst_1)
print(sorted(z, reverse=True))

# Вариант 2
lst_2 = [1,4,2,-3,6,7,8,9,]
def task_07_func_2(lst_2):
    i = 0
    while i < len(lst_2):
        if lst_2[i]<0:
            del lst_2[i]
        else:
            i+=1
    lst_2 = sorted(list(lst_2))
    lst_2.reverse()
    result = [x ** 2 for x in lst_2]
    return result
print(task_07_func_2(lst_2))


# Вариант 3
lst_3 = [1,4,2,-3,6,7,8,9,]
def task_07_func_3(lst_3):
    spisok = filter(lambda x: x > 0, lst_3)
    spisok=sorted(list(spisok))
    spisok.reverse()
    result=[x**2 for x in spisok]

    return result

task_07_func_3(lst_3)
print(task_07_func_2(lst_3))