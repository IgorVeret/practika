'''В векторе повторить все значения n раз. Пример: для массива [1, 2, 3] и n равного 3, ответом
должен быть массив [1, 1, 1, 2, 2, 2, 3, 3, 3].'''

import numpy as np

def task_2(arr,n):
    return np.repeat(arr, n) #Функция repeat() повторяет элементы массива
print(task_2(np.array([1,2,3]), 3))