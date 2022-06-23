
'''Задание 12 (1 балл): Напишите функцию, которая получает на вход путь к файлу, в котором
 в каждой строке записано одно вещественное число, а также путь к выходному файлу. Функция
 должна прочитать содержимое файла, игнорировать строки с нечётными индексами, а строки
с чётными индексами должна увеличить на минимальное из чисел, содержащихся в этом файле.
Полученные числа нужно записать в выходной файл с точностью 5 знаков после запятой.

Требуется сделать не более двух проходов по входному файлу, расход памяти на протяжении
 работы должен быть O(1) (то есть никак не зависеть от числа строк во входном файле).'''
import os
input_path = open ('task_12\stroki_in.txt', "r")
output_path= open ('task_12\stroki_out.txt', "w")

def task_12_func(input_path, output_path):# output_path
	l=[] #олучаем данные из файла
	while True: # считываем из файла
		line = input_path.readline()
		if not line:
			break
		else:
			l.append(float(line)) # Записываем в список
	min_number = min(l) #Получаем мин значение
	for i, w in enumerate(l):# Присваиваем индекс, где w - данные из считаного файла
		if i % 2 == 0: # Проверяем на четность
			number_multiply=(w*min_number) # Умножаем на мин значение
			number_multiply_round = round(number_multiply, 5) # округляем
			output_path.writelines(str(number_multiply_round)+ '\n') # записываем в файл

task_12_func(input_path, output_path)
input_path.closed
output_path.closed
