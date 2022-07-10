'''Задание 5 (1.5 балла): Каждый объект представляет собой текст. Чаще всего тексты предобрабатывают перед тем, как пытаться выделять из них признаки. Опишите функцию preprocess, которая получает на вход сырой текст и возвращает предобработанный. Примените эту функцию к элементу text каждого объекта и результат запишите в столбец pp_text (далее под текстом подразумевается именно содержимое этого столбца). За пределами preprocess циклами пользоваться запрещено (т.е. предобработка должна применяться средствами DataFrame). Функция должна выполнять следующий набор операций:

привести текст к нижнему регистру
заменить все символы '\n', '\t' и '\r' на пробелы
заменить в тексте все символы, не являющиеся английскими буквами, на пробелы
сделать split текста по пробелам, удалив все пустые слова
вернуть получившийся список слов
Для ускорения preprocess может использовать внешние переменные, например, скомпилированные регулярные выражения.'''
# Текст взят из задания 4
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
import re

X_train = fetch_20newsgroups(subset='train')
X_test = fetch_20newsgroups(subset='test')

label_names = pd.DataFrame(columns=['label_id', 'label_name'],
                           data=[(i, e) for i, e in enumerate(list(X_train.target_names))])

data = pd.DataFrame()
data['text'] = X_train.data + X_test.data
data['is_train'] = [True] * len(X_train.data) + [False] * len(X_test.data)
data['label_id'] = list(X_train.target) + list(X_test.target)
# ------------------------------------------------------------------------

jd = data.merge(label_names, on='label_id', how='left')

reg = re.compile(r'[^a-zA-Z ]')  # Регулярное выражение(выбираем буквы)

# Текст приводим к нижнему регистру, заменяем символы, сплитуем
def preprocess(text):
    word_processing = text.lower()
    word_processing = re.sub(reg, ' ', word_processing)
    return word_processing.split()

def task_5():
    jd['pp_text'] = jd['text'].apply(preprocess)
    return jd.head(10)

print(task_5())
