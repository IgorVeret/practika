'''Задание 11 (2.5 балла): Часто в обработке текстов возникает задача выделения тем,
обсуждаемых в них. Одним из способов решения это задачи является кластеризация графа
совстречаемостей слов. Для текстов, находящихся в поле pp_text постройте словарь "слово"
в "слово" в "счетчик совстречаемости", для слова A и B достаточно хранить A -> B -> counter,
хранить B -> A -> counter не нужно. Счетчик увеличивается на 1, если пара слов встретилась
в одном тексте внутри окна с длиной 10 слов.'''
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
import re
from collections import Counter
from collections import defaultdict
from tqdm import tqdm

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


vocabulary = task_6()

keys = vocabulary.keys()
print(keys)

def task_11():
    dict_my = defaultdict(int)
    for val in tqdm(train_df['pp_text']):
        temp_val = []
        for elem in val:
            if elem in keys:
                temp_val.append(elem)
        for i in range(len(temp_val) - 9):
            sl = temp_val[i: i + 10]
            for k in range(10):
                for j in range(k + 1, 10):
                    fs = frozenset([sl[k], sl[j]])
                    if len(fs) != 2:
                        continue
                    dict_my[fs] += 1
    return dict_my
my_dict = task_11()
print(len(my_dict))
