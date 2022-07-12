
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

reg = re.compile(r'[^a-zA-Z ]')


def preprocess(text):
    text_prep = text.lower()
    text_prep = re.sub(reg, ' ', text_prep)
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

    return word_dict


def word_filt(wrd_list):

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
'''Задание 7 (2 балла)'''''': Для построения моделей данные нужно перевести в числовой вид. Для этого воспользуйтесь
представлением "мешка слов", в котором признаками являются слова, а значениями - частоты
их встречаемости в документе. Построить представление мешка слов можно с помощью класса
CountVectorizer из sklearn. Подготовьте векторизатор, подав ему обучающие текстовые данные из
data (приведите тексты к формату входа векторизатора) и полученный выше словарь.

Примените полученный векторизатор к обучающим и тестовым данным, на выходе должны получиться два numpy
array (первая размерность - число объектов, вторая - число слов в словаре).'''
from sklearn.feature_extraction.text import CountVectorizer
'''векторизацией общий процесс преобразования набора текстовых документов в векторы числовых 
признаков. Эта конкретная стратегия (токенизация, подсчет и нормализация) называется представлением 
Bag of Words или Bag of n-grams. Документы описываются вхождениями слов, полностью игнорируя информацию 
об относительном положении слов в документе'''
test_df = jd.loc[jd['is_train'] == False]


def task_7():
    vectorizer = CountVectorizer(vocabulary=vocabulary.keys())
    cv_train = vectorizer.transform(train_df['text'])
    cv_test = vectorizer.transform(test_df['text'])
    print(cv_test)
    return cv_train, cv_test

X_train, X_test = task_7()
print(X_train, X_test)
