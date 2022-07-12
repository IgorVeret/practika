'''
Задание 8 (2 балла): Модель логистической регрессии хорошо работает для простых задач
классификации текстов, примените её к полученным данным. Для этого настройте модель на
обучающих данных, сделайте предсказание для тестовых и измерьте качество с помощью
метрик accuracy и F1-score с микро- и макро-усреднением. Попробуйте подобрать
оптимальное значение коэффициента регуляризации С с помощью GridSearchCV.'''
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
import re
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer

X_train = fetch_20newsgroups(subset='train')
X_test = fetch_20newsgroups(subset='test')

label_names = pd.DataFrame(columns=['label_id', 'label_name'],
                           data=[(i, e) for i, e in enumerate(list(X_train.target_names))])
data = pd.DataFrame()
data['text'] = X_train.data + X_test.data
data['is_train'] = [True] * len(X_train.data) + [False] * len(X_test.data)
data['label_id'] = list(X_train.target) + list(X_test.target)
jd = data.merge(label_names, on='label_id', how='left')
pd.options.mode.chained_assignment = None
jd.loc[jd['is_train'] == True]['label_name']

reg = re.compile(r'[^a-zA-Z ]')

def preprocess(text):
    text_prep = text.lower()
    text_prep = re.sub(reg, ' ', text_prep)
    return text_prep.split()


def task_5():
    jd['pp_text'] = jd['text'].apply(preprocess)

task_5()

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



test_df = jd.loc[jd['is_train'] == False]


def task_7():
    vectorizer = CountVectorizer(vocabulary=vocabulary.keys())
    cv_train = vectorizer.transform(train_df['text'])
    cv_test = vectorizer.transform(test_df['text'])

    return cv_train, cv_test

X_train, X_test = task_7()

#-------------------------------Задача 8------------------------------

y_train = train_df['label_name']


y_test = test_df['label_name']
model = LogisticRegression(solver='lbfgs', max_iter=1000, multi_class='multinomial')

model.fit(X_train, y_train)

predict_n = model.predict(X_test)

print(f"Test Accuracy: {accuracy_score(y_test, predict_n)}")
print(f"Test f1-score macro: {f1_score(y_test, predict_n, average='macro')}")
print(f"Test f1-score micro: {f1_score(y_test, predict_n, average='micro')}")
grid_search = GridSearchCV(LogisticRegression(solver='lbfgs', max_iter=1000, multi_class='multinomial'), cv=3,
                           param_grid={"C": [0.5, 1.0, 10.0]},
                           scoring='accuracy')
grid_search.fit(X_train, y_train)

print(f"Best accuracy:{grid_search.best_score_} with {grid_search.best_params_} adn cross-valid-n parameter=3")