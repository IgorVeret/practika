import pandas as pd
from sklearn.datasets import fetch_20newsgroups

X_train = fetch_20newsgroups(subset='train')
X_test = fetch_20newsgroups(subset='test')

#label_id и label_name были перепутаны
label_names = pd.DataFrame(columns=['label_id', 'label_name'],
                           data=[(i, e) for i, e in enumerate(list(X_train.target_names))])
data = pd.DataFrame()
data['text'] = X_train.data + X_test.data
data['is_train'] = [True] * len(X_train.data) + [False] * len(X_test.data)
data['label_id'] = list(X_train.target) + list(X_test.target)
#------------------------------------------------------------------------
'''Заберем все значения из левой таблицы, но из правой 
используем только те значения, которые есть в левой. '''
jd = data.merge(label_names, on='label_id',  how='left')
print(jd.head(6)) #Выведем результат первые 6 строк
# print(joined)
jd.drop(['label_id'], axis=1, inplace=True)# Удаляем из таблицы столбец
print(jd.head(6))
train=pd.DataFrame()
test=pd.DataFrame()
train= len(X_train.data)
print('Количество тренировочных данных',train)
test= len(X_test.data)
print('Количество тестовых данных',test)



