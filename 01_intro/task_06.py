'''Задание 6 (1 балл): Напишите функцию, которая принимает на вход строку и символ и возвращает:

если символ встретился в строке один раз - кортеж (индекс вхождения, None);
если два и более раз - кортеж (индекс первого вхождения, индекс последнего вхождения);
если ни разу - кортеж (None, None).
Запрещается делать более одного прохода по каждому элементу строки.'''
# во поле березка стояла
input_str = input('Введите строку: ')


input_char = input('Введите символ: ')
def task_06_func(input_str, input_char):
	count=0 # Подсчитываем количество входящих символов
	for i in input_str:

		if i == input_char:
			count += 1

	if count > 1:
		a = (len(input_str)-1)
		# print(a)
		return input_str.index(input_char), a # не получилось выводится первый вход и последний элемент
		# return cortege
	elif count==1:
		return input_str.index(input_char), None
	else:
		return None, None

print(task_06_func(input_str, input_char))
