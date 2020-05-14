#! usr/bin/python

import numpy as np
import pandas as pd
import data_prep
from sklearn.naive_bayes import GaussianNB


def gaussian_naive_bayes():
    dataset = pd.read_csv('amazon_alexa.tsv', delimiter='\t', quoting=3)
    X_train, x_test, Y_train, y_test = data_prep.data_process(dataset)

    clf = GaussianNB()
    clf.fit(X_train, Y_train)

    pd.crosstab(y_test, clf.predict(x_test), rownames=['True'], colnames=['Predicted'],
                margins=True).plot().get_figure().savefig('nb_result.png')


if __name__ == '__main__':
    gaussian_naive_bayes()

