import json

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from joblib import dump

f = open('../data/x_playData.json')
x_features = list(json.load(f))
f.close()

f = open('../data/y_playData.json')
y_key = list(json.load(f))
f.close()

X_train, X_test, y_train, y_test = train_test_split(np.array(x_features), np.array(y_key), test_size=0.2, random_state=0)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(27, 356, 26), random_state=1)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
dump(clf, 'model.joblib')

print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
