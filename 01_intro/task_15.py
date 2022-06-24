'''Задание 15 (1.5 балла): Написать функцию, которая во входной строке заменяет вхождения всех
 английских заглавных букв на их номер в таблице ASCII, затем производит сплит по минимальной
 из цифр строки. Предложите как минимум два различных решения, одно из которых не должно
использовать циклы. При использовании циклов допускается не более двух проходов по строке.'''
#Вариант 1
import re

n = input('Введите строку: ')


# Строка для удобства
# n='In Google Chrome the address bar  that sits at the top of the browser  window'
def task_15_func(n):
    spisok = [] #Список
    for i in n: # Проверям на заглавные буквы и преобразуем в список
        if i.isupper():

            spisok.append(str(ord(i)))# Заменяем заглавные буквы
        elif i == ' ':
            continue # если пробел, то пропускаем
        else:
            spisok.append(i)
    stroka_new = ''.join(spisok) # Превращаем список в строку
    number_find = re.findall('[1-9]', stroka_new) # Поиск числа в строке
    min_number = min(number_find) # Находим минимальное чисо
    return stroka_new.split(sep=min_number) # Сплитуемся по минимальному числу


print(task_15_func(n))
