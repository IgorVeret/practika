'''Задание 4 (1.5 балла): Используя возможности библиотеки pandas
1. Cделайте join таблиц data и label_names, удалив из итоговой таблицы поле label_id
2. Посчитайте количество обучающих и тестовых данных
3. Постройте круговую диаграмму, показывающую долю каждого класса в обучающих данных'''

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_20newsgroups

X_train = fetch_20newsgroups(subset='train')
X_test = fetch_20newsgroups(subset='test')

label_names = pd.DataFrame(columns=['label_id', 'label_name'],
                           data=[(i, e) for i, e in enumerate(list(X_train.target_names))])
data = pd.DataFrame()
data['text'] = X_train.data + X_test.data
data['is_train'] = [True] * len(X_train.data) + [False] * len(X_test.data)
data['label_id'] = list(X_train.target) + list(X_test.target)
#------------------------------------------------------------------------
print("Часть 1")
'''Заберем все значения из левой таблицы, но из правой 
используем только те значения, которые есть в левой. '''
jd = data.merge(label_names, on='label_id',  how='left')
print(jd.head()) #Выведем результат
# print(joined)
jd.drop(['label_id'], axis=1, inplace=True)# Удаляем из таблицы столбец
print("Часть 2")
print(jd.head())#Выведем результат
train=pd.DataFrame()
test=pd.DataFrame()
train= len(X_train.data)
print('Количество тренировочных данных',train)
test= len(X_test.data)
print('Количество тестовых данных',test)
print("Часть 3")
#Выберем тренировочные данные
jd.loc[jd['is_train'] == True]['label_name'].value_counts().plot.pie()
plt.show()





