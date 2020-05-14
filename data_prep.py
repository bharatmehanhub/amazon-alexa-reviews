#! usr/bin/python

import numpy as np
import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


def removing_sw(list1):
    for element in list1:
        if element in stopwords.words('english'):
            list1.remove(element)
    return list1


def data_process(dataset):

    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: x.replace(r'http', ' '))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: x.replace(r'http', ' '))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: x.replace(r'£|\$', ' '))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: x.replace(r'\d+(\.\d+)?', ' '))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: re.sub('[^a-zA-Z]', ' ', x))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: x.lower().split())
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: removing_sw(x))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: ' '.join(x))

    cv = CountVectorizer()
    X = cv.fit_transform(dataset.verified_reviews).toarray()
    y = dataset.feedback

    X_train, x_test, Y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    return X_train, x_test, Y_train, y_test


def data_set_process(dataset):

    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: x.replace(r'http', ' '))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: x.replace(r'http', ' '))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: x.replace(r'£|\$', ' '))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: x.replace(r'\d+(\.\d+)?', ' '))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: re.sub('[^a-zA-Z]', ' ', x))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: x.lower().split())
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: removing_sw(x))
    dataset['verified_reviews'] = dataset['verified_reviews'].apply(lambda x: ' '.join(x))

    return dataset
