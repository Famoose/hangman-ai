import json
from random import random

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

import convertHelpers
from gameController import GameController

f = open('../data/x_playData.json')
x_features = list(json.load(f))
f.close()

f = open('../data/y_playData.json')
y_key = list(json.load(f))
f.close()

X_train, X_test, y_train, y_test = train_test_split(np.array(x_features), np.array(y_key), test_size=0.2, random_state=0)
gnb = GaussianNB()
model = gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
print("Number of mislabeled points out of a total %d points : %d"
      % (X_test.shape[0], (y_test != y_pred).sum()))


correct = 0
wrong = 0
wordGuessed = 0
notGuessed = 0
for i in range(10000):
    if i%1000 == 0:
        print(i)
    gc = GameController()
    while not (gc.wordGuessed or gc.gameover):
        usableKeys = gc.getUsableKeys()
        wordBefore = gc.showWord()
        features = np.array(convertHelpers.convertFeatures(wordBefore, usableKeys))
        prediction = gnb.predict(np.array([features]))[0]
        predictedKey = convertHelpers.keys[prediction]
        #pick random if gn is dumb
        if predictedKey not in usableKeys:
            i = random.randint(0, len(usableKeys) - 1)
            predictedKey = convertHelpers.keys[i]

        success = gc.guesKey(predictedKey)
        if success:
            correct += 1
        else:
            wrong += 1
            #print('wrong')
    if(gc.wordGuessed):
        wordGuessed += 1
        #print('word guessed')
    else:
        notGuessed += 1
        #print('not guessed')

print(wordGuessed)
print(notGuessed)