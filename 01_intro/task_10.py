'''Задание 10 (1 балл): Напишите функцию, которая принимает на вход абсолютный путь к директории и две
 строки с расширениями файлов. В результате её выполнения у всех файлов в указанной директории,
имеющих первое расширение, расширение должно измениться на второе. В конце работы функция должна
возвращать кортеж из двух элементов:
1. сколько всего в директории файлов (именно файлов, не директорий);
2. у скольки из них расширение было изменено.'''
#https://xakep.ru/2021/08/04/python-for-newbies-3/ , https://docs-python.ru/standart-library/modul-pathlib-python/poluchit-spisok-fajlov-direktorii/
#https://chel-center.ru/python-yfc/2021/10/24/rabota-s-fajlami-v-python/
import os
import fnmatch
prev_extension='tx_'
next_extension='txt'
print(type(prev_extension))
print(type(prev_extension))
dir_path=os.chdir(r'E:/dir_root')
print(dir_path)


def task_10_func(dir_path, prev_extension, next_extension):
	total=0
	changed=0
	for fname in os.listdir(dir_path):
		total+=1
		    if fnmatch.fnmatch(fname, '*.tx_'):
			    fname.rename('*.txt')
			    changed +=1
	return total, changed
task_10_func(dir_path, prev_extension, next_extension)