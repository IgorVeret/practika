
'''Задание 1.Проверить, что все элементы входного массива строго положительны.'''
import numpy as np

def task_1(arr):
  new = arr>0
  return new.all() # Обобщаем список
a = np.array([1,2,3,4,5])
b = np.array([1,-2, -3, 4,5,6])
print(task_1(a))
print(task_1(b))
