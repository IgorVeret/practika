'''Задание 16 (1.5 балла): Написать функцию, которая принимает на вход строку и извлекает
 из неё мобильные телефонные номера с помощью регулярных выражений. Функция должна поддерживать
общепринятые варианты написания номера, как со всевозможными разделителями, так и без них
 (обеспечьте поддержку не менее 10 различных случаев). Возвращаемым значением функции является
 список всех найденных в строке номеров, если их не было, нужно вернуть пустой список.'''
import re
n=input('Введите строку: ')
#Строки для тренировки
# n= 'ewew +79536761226 rewqrewew +79536761227 hddsfewew +7(953)6761229 rrwe ss 8 953 676 1230 fgfs +7(953)676-12-31 '
# n='dfjafanrerg rejtqrionfoISJIORJ JWELFNKNCKKLZrtiea c.nnrruhttankl gklasjgia'
def task_16_func(n):
    result =re.findall('(\+7|8).*?(\d{2,3}).*?(\d{2,3}).*?(\d{2}).*?(\d{2})', n)
    return result
print(task_16_func(n))