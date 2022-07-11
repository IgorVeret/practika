'''Задание 6 (2 балла): Каждое уникальное слово текста представляет собой признак.
Посчитайте, сколько в обучающих текстах есть уникальных слов, отобразите гистограмму
частот встречаемости слов в обучающей коллекции, отсортировав слова по убыванию частоты
встречаемости (по оси X идут все слова из словаря коллекции в порядке убывания частоты
встречаемости, по оси Y указываются значения частот).

Для уменьшения признакового пространства словарь фильтруют. Удалите из словаря

все слова, встречающиеся более 9000-х раз
все слова, встречающиеся менее 3-х раз
все слова длиной менее 3 символов
все слова длиной более 20 символов
все слова, состоящие из одного и того же символа
Профильтруйте обучающую коллекцию по новому словарю и снова посчитайте число уникальных
слов в словаре и снова постройте гистограмму частот.'''
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
import re
import matplotlib.pyplot as plt
from collections import Counter

X_train = fetch_20newsgroups(subset='train')
X_test = fetch_20newsgroups(subset='test')

label_names = pd.DataFrame(columns=['label_id', 'label_name'],
                           data=[(i, e) for i, e in enumerate(list(X_train.target_names))])
data = pd.DataFrame()
data['text'] = X_train.data + X_test.data
data['is_train'] = [True] * len(X_train.data) + [False] * len(X_test.data)
data['label_id'] = list(X_train.target) + list(X_test.target)
jd = data.merge(label_names, on='label_id', how='left')

jd.loc[jd['is_train'] == True]['label_name']

ptrn = re.compile(r'[^a-zA-Z ]')


def preprocess(text):
    text_prep = text.lower()
    text_prep = re.sub(ptrn, ' ', text_prep)
    return text_prep.split()


def task_5():
    jd['pp_text'] = jd['text'].apply(preprocess)

task_5()

# -----------------------6 задание--------------------------------
'Используем для блокировки предупреждения библиотеки pandas'
pd.options.mode.chained_assignment = None
'''Вид словаря, который позволяет нам считать количество неизменяемых объектов
(в большинстве случаев, строк)'''
vocabulary = Counter()
train_df = jd.loc[jd['is_train'] == True]


def task_6():
    word_dict = Counter()
    train_df['pp_text'].apply(word_dict.update)
    lists = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:10]

    x, y = zip(*lists)
    plt.bar(x, y)
    plt.show()

    return word_dict


def word_filt(wrd_list):
    vc=list(filter(lambda x: x in vocabulary.keys(), wrd_list))

    return list(filter(lambda x: x in vocabulary.keys(), wrd_list))


vocabulary = task_6()  # Первый вызов
vocabulary = dict(filter(lambda x:
                         x[1] <= 9000 and  # все слова, встречающиеся более 9000-х раз
                         x[1] >= 3 and  # все слова, встречающиеся менее 3-х раз
                         len(x[0]) <= 20 and  # все слова длиной менее 3 символов
                         len(x[0]) >= 3 and  # все слова длиной более 20 символов
                         x[0] != len(x[0]) * x[0][0],  # все слова, состоящие из одного и того же символа
                         vocabulary.items()))

train_df.loc[:, 'pp_text'] = train_df['pp_text'].apply(word_filt)

vocabulary = task_6()  # Второй вызов
