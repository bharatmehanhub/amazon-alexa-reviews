#! usr/bin/python

import numpy as np
import pandas as pd
import data_prep
from sklearn.tree import DecisionTreeClassifier


def decision_tree():
    dataset = pd.read_csv('amazon_alexa.tsv', delimiter='\t', quoting=3)
    X_train, x_test, Y_train, y_test = data_prep.data_process(dataset)

    clf_ds = DecisionTreeClassifier(criterion='entropy', random_state=0)
    clf_ds.fit(X_train, Y_train)

    pd.crosstab(y_test, clf_ds.predict(x_test), rownames=['True'], colnames=['Predicted'],
                margins=True).plot().get_figure().savefig('dt_result.png')


if __name__ == '__main__':
    decision_tree()
